import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/Index.vue'
import AddView from '@/views/AddCSIRTForm.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/add',
        name: 'add',
        component: AddView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
