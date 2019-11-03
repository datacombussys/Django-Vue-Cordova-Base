import Vue from "vue";
import './plugins/axios'
import App from "./App.vue";
import router from "./router";
import store from "./store";


import "@babel/polyfill";
import "roboto-fontface/css/roboto/roboto-fontface.css";


//Popper
import "popper.js/dist/popper.js";

// // import MAIN SCSS SASS and LESS files
// import "./assets/less/main.less";
// import "./assets/sass/main.sass";
// import "./assets/scss/main.scss";

// jquery
import $ from "jquery";
global.$ = $;

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
