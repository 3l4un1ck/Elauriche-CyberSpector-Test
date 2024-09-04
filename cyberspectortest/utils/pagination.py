from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
import urllib.parse as urlparse
from urllib.parse import parse_qs
from django.core.paginator import InvalidPage

class NotFound(APIException):
    status_code = status.HTTP_200_OK
    default_detail = 'Not found.'
    default_code = 'not_found'
    

def getPage(url):
    if url is None:
        return None
    parsed = urlparse.urlparse(url)
    if "page" not in parse_qs(parsed.query):
        return 1
    ret = parse_qs(parsed.query)['page']
    if isinstance(ret, list):
        return int(ret[0])
    elif isinstance(ret, str):
        return int(ret)
    elif isinstance(ret, int):
        return ret
    else:
        return ret


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 12
    invalid_page_message = 'Invalid page.'
    
    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)
        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            msg = {
                'current_page':page_number,
                'max_page_size': self.max_page_size,
                'data':[]
            }
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)


    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'next_num': getPage(self.get_next_link()),
                'previous_num': getPage(self.get_previous_link())
            },
            'current_page':self.page.number,
            'max_page_size': self.max_page_size,
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'data': data
        })