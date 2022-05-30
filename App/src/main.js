import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from "./router/index"
import VueTheMask from 'vue-the-mask'

createApp(App).use(router).use(VueTheMask).mount('#app')
