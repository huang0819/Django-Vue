import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

axios.defaults.baseURL = 'http://127.0.0.1:8000'
createApp(App).use(store).use(router, axios).mount('#app')