import { createWebHistory, createRouter } from 'vue-router'
import LoginPage from '../components/LoginPage.vue'
import RegistrationPage from '../components/RegistrationPage.vue'

const routes = [
  { path: '/signup', component: RegistrationPage },
  { path: '/login', component: LoginPage },
  { path: '', redirect: '/login' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
