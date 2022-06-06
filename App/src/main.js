import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from "./router/index"
import VueTheMask from 'vue-the-mask'
import Toast, { POSITION } from "vue-toastification";
import "vue-toastification/dist/index.css";

createApp(App)
  .use(router)
  .use(VueTheMask)
  .use(Toast, { position: POSITION.TOP_LEFT })
  .mount('#app')
