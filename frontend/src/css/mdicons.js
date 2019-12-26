// Import Vue
import Vue from "vue";
import { mdiAccount } from '../../node_modules/@mdi/font/scss/materialdesignicons.scss';

Vue.component('b-icon', mdiAccount);


import Buefy from 'buefy'
Vue.use(Buefy, {
  defaultIconComponent: 'b-icon',
});