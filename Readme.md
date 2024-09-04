# CyberSpectort Test Elauriche Nickson 

This project includes a Django REST API for managing CSIRTs (Computer Security Incident Response Teams) and a Vue.js frontend for displaying and interacting with CSIRTs on a map of Africa.

## Project Structure

- **cyberspectortest/**: Django backend project folder.
- **cyberspectortest-frontend/**: Vue.js frontend project folder.
- **docker-compose.yml**: Docker Compose configuration for running the project.
- **Dockerfile**: Dockerfile for Django and Vue.js applications.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Docker: [Get Docker](https://www.docker.com/get-started)
- Docker Compose: Comes pre-installed with Docker Desktop

## Setup and Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/3l4un1ck/Elauriche-CyberSpector-Test.git
cd Elauriche-CyberSpector-Test
```

### 2. Build the Docker Containers

Build the Docker images for both the Django API and the Vue.js frontend:

```bash
docker-compose build
```

### 3. Run the Docker Containers

Start the services using Docker Compose:

```bash
docker-compose up
```

This will start both the Django API and the Vue.js frontend.

### 4. Access the Applications

	•	Django API: Visit http://localhost:8000/ to access the Django API.
	•	Vue.js Frontend: Visit http://localhost:8080/ to access the Vue.js frontend.

## Customization

	•	Django Settings: You can customize the Django settings in csirt_project/settings.py.
	•	Vue.js Configuration: Modify Vue.js configuration and components within the csirt-frontend/ directory.

## Deployment to Production

For production deployment, you may want to:

	•	Use Gunicorn or another WSGI server instead of Django’s development server.
	•	Serve the Vue.js frontend with a production-ready server like Nginx.
	•	Configure SSL certificates if deploying to a cloud service or server.

## Troubleshooting

If you encounter any issues, check the logs for more information: