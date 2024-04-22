import { createWebHistory, createRouter } from 'vue-router'
import LoginPage from '../components/LoginPage.vue'
import RegistrationPage from '../components/RegistrationPage.vue'
import Dashboard from '@/components/Dashboard.vue'
import store from '../store/store'
import Customers from '@/components/Customers.vue'
import Invoices from '@/components/Invoices.vue'
import Business from '@/components/Business.vue'
import LandingPage from '@/components/LandingPage.vue'
import NotFoundPage from '@/components/NotFoundPage.vue'
import NewSidebar from '@/components/NewSidebar.vue'

const routes = [
  { path: '/signup', component: RegistrationPage },
  { path: '/login', component: LoginPage },
  { path: '/:profileId/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/:profileId/customers', component: Customers, meta: { requiresAuth: true } },
  { path: '/:profileId/invoices', component: Invoices, meta: { requiresAuth: true } },
  {
    path: '/:profileId/business',
    component: Business,
    meta: { requiresAuth: true }
  },
  { path: '', component: LandingPage },
  { path: '/:pathMatch(.*)', component: NotFoundPage },
  { path: '/test', component: NewSidebar }
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
