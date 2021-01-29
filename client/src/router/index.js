import Vue from 'vue'
import VueRouter from 'vue-router'
import Landing from '../views/Landing.vue'
import Sign_in from '../views/Sign_in.vue'
import Sign_up from '../views/Sign_up.vue'

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
    component: Sign_in,
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
    component: Sign_up,
    meta: {
      title: "Financial Go | Sign up",
      metaTags: [
        {
          name: "description",
          content: "Sign up a new user."
        }
      ]
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
