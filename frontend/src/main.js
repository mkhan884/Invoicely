import './assets/style.css'
import router from './router/router'

import { createApp } from 'vue'
import App from './App.vue'
import store from './store/store'

createApp(App).use(router).use(store).mount('#app')
