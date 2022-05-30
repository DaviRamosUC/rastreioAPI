import { createRouter, createWebHistory } from 'vue-router'
import Home from '/src/components/Home.vue'
import Codigos from '/src/components/Codigos.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/codigos',
    name: 'Codigos',
    component: Codigos,
  }
]
const router = createRouter({
  history: createWebHistory(),
  routes,
})
export default router