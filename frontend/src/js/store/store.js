import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);

//Import and Use Axios
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import { Users } from './users';

export default new Vuex.Store({
	modules: {
		Users
	},
  state: {
    
    blogs: []
  },
  mutations: {
    fetchBlogs(state, payload) {
      console.log("fetchBlogs mutations");
      state.blogs = payload;
    }
  },
  actions: {
    fetchBlogs(context) {
      axios.get("http://localhost:8000/api/blog/").then(response => {
        console.log(response.data, "fetch data actions");
        context.commit("fetchBlogs", response.data);
      });
    }
  },
  getters: {
    getBlogs(state) {
      console.log(state.blogs, "from getter blog");
      return state.blogs;
    }
  }
})