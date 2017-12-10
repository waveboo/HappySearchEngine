import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import Home from './components/Home'

Vue.use(VueRouter)

const routes = [{
  path: '/',
  component: Home
},{
  path: '/home',
  component: Home
}]

const router = new VueRouter( {
  routes
})

new Vue({
  router,
  ...App
}).$mount('#app')
// new Vue({
//   el: '#app',
//   render: h => h(App)
// })
