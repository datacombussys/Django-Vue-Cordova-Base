// Import Vue
import Vue from "vue";
import axios from "../../node_modules/axios/lib/axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);


var token = localStorage.getItem('token');

axios.defaults.baseURL = "http://localhost:8000";
// axios.defaults.headers.common['Authorization'] = "Token " + token;
axios.defaults.headers.post['Content-Type'] = 'application/json';

