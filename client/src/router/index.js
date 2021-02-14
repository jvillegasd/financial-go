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
    name: 'dashboard',
    component: DashboardLayout,
    children: []
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  linkExactActiveClass: 'active',
  routes
})

export default router
