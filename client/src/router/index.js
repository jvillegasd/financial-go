import Vue from 'vue'
import VueRouter from 'vue-router'
import Landing from '../views/Landing.vue'
import SignIn from '../views/Sign_in.vue'
import SignUp from '../views/Sign_up.vue'
import DashboardLayout from '../layout/DashboardLayout.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: Landing,
    meta: {
      title: "Financial Go",
      metaTags: [
        {
          name: "description",
          content: "The landing page of this app."
        }
      ]
    }
  },
  {
    path: '/sign_in',
    name: 'Sign in',
    component: SignIn,
    meta: {
      title: "Financial Go | Login",
      metaTags: [
        {
          name: "description",
          content: "Sign in a new user."
        }
      ]
    }
  },
  {
    path: '/sign_up',
    name: 'Sign up',
    component: SignUp,
    meta: {
      title: "Financial Go | Sign up",
      metaTags: [
        {
          name: "description",
          content: "Sign up a new user."
        }
      ]
    }
  },
  {
    path: '/dashboard',
    component: DashboardLayout,
    children: [
      {
        path: '',
        component: () => import('../views/dashboard/Main.vue'),
        meta: {
          title: "Financial Go | Dashboard",
          metaTags: [
            {
              name: "dashboard",
              description: "General data about the current user."
            }
          ]
        }
      },
      {
        path: '/transactions',
        component: () => import('../views/dashboard/Transactions.vue'),
        meta: {
          title: "Financial Go | Transactions",
          metaTags: [
            {
              name: "transactions",
              description: "Transaction data of the current user."
            }
          ]
        }
      },
      {
        path: '/invoices',
        component: () => import('../views/dashboard/Invoices.vue'),
        meta: {
          title: "Financial Go | Invoices",
          metaTags: [
            {
              name: "invoices",
              description: "Invoices data of the current user."
            }
          ]
        }
      },
      {
        path: '/wallets',
        component: () => import('../views/dashboard/Wallets.vue'),
        meta: {
          title: "Financial Go | Wallets",
          metaTags: [
            {
              name: "wallets",
              description: "Information about every wallet the current user registered."
            }
          ]
        }
      },
      {
        path: '/settings',
        component: () => import('../views/dashboard/Settings.vue'),
        meta: {
          title: "Financial Go | Settings",
          metaTags: [
            {
              name: "settings",
              description: "Dashboard settings."
            }
          ]
        }
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  linkExactActiveClass: 'active',
  routes
})

export default router
