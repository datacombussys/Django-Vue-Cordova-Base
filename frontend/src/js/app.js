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
import '../css/icons.css';
import '../css/app.less';

// Import App Component
import App from '../components/app.vue';

//Import Vuex and Store
import store from "./store/store";

// Init Framework7-Vue Plugin
Framework7.use(Framework7Vue);


// Init App
new Vue({
	el: '#app',
	store,
  render: (h) => h(App),

  // Register App Component
  components: {
		app: App,
  },
});