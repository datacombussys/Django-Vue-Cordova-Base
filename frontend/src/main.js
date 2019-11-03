import Vue from "vue";
import './plugins/axios'
import App from "./App.vue";
import router from "./router";
import store from "./store";


import "@babel/polyfill";
import "roboto-fontface/css/roboto/roboto-fontface.css";

// Buefy
import Buefy from 'buefy'
Vue.use(Buefy)

//Popper
import "popper.js/dist/popper.js";

// // import MAIN SCSS SASS and LESS files
// import "./assets/less/main.less";
// import "./assets/sass/main.sass";
// import "./assets/scss/main.scss";

// jquery
import $ from "jquery";

//Framework7
import Framework7 from 'framework7/framework7.esm.bundle.js';
import Framework7Vue from 'framework7-vue/framework7-vue.esm.bundle.js'

// Import F7 Styles
import 'framework7/css/framework7.css';

// Import Icons and App Custom Styles -Framework7
import './css/icons.css';
import './css/app.css';

Framework7.use(Framework7Vue)


global.$ = $;

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
