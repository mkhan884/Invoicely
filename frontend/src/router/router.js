import { createWebHistory, createRouter } from 'vue-router'
import LoginPage from '../components/LoginPage.vue'
import RegistrationPage from '../components/RegistrationPage.vue'
import Dashboard from '@/components/Dashboard.vue'
import store from '../store/store'

const routes = [
  { path: '/signup', component: RegistrationPage },
  { path: '/login', component: LoginPage },
  { path: '/:profileId/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '', redirect: '/login' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // If the route requires authentication, check if the user is authenticated
    if (store.state.isAuthenticated) {
      // If authenticated, proceed with navigation
      next()
    } else {
      // If not authenticated, redirect to the login page
      next('/login')
    }
  } else {
    // For routes that don't require authentication, proceed with navigation
    next()
  }
})

export default router
