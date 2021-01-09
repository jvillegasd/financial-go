import Vue from 'vue'
import VueRouter from 'vue-router'
import Landing from '../views/Landing.vue'
import Sign_in from '../views/Sign_in.vue'

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
      title: "Financial Go | Sign in",
      metaTags: [
        {
          name: "description",
          content: "Sign in a new user."
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
