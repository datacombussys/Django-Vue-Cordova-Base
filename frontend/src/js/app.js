// Import Vue
import Vue from 'vue';

//Import Custom Fonts
import "../fonts/fonts.less";

// Import Framework7
import Framework7 from './framework7-custom.js';

// Import Framework7-Vue Plugin
import Framework7Vue from 'framework7-vue/framework7-vue.esm.bundle.js';

// Import Framework7 Styles
import '../css/framework7-custom.less';

// Import Icons and App Custom Styles
require("@/css/icons.css");
require("@/css/mdicons");
import "../css/app.less";

// Import App Component
import App from '../components/app.vue';

//Import Vuex and Store
import store from "./store/store";
require("@/js/store/subscribers");

// Init Framework7-Vue Plugin
Framework7.use(Framework7Vue);

//Import and Use Axios
var axios = require('@/js/axios');

//Import and Register Gobally Vee Vaidate
import Vuelidate from 'vuelidate';
Vue.use(Vuelidate);

// Init App
new Vue({
  el: '#app',
  store,
  axios,
  render: (h) => h(App),

  // Register App Component
  components: {
    app: App
  },
});