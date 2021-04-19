import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './assets/styles/tailwind.css';
import vsTable from 'vuesax';
import vsPagination from 'vuesax';
import 'vuesax/dist/vuesax.css';

Vue.use(vsTable);
Vue.use(vsPagination);

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
