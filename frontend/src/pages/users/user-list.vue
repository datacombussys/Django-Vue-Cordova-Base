<template>
  <f7-page name="user-list">
    <f7-navbar title="User Table" back-link="Back"></f7-navbar>
    <!-- Page content-->
    <f7-block-title medium>Block with Special (inset) Formatting</f7-block-title>
    <f7-block strong inset>
      <p>Donec et nulla auctor massa pharetra adipiscing ut sit amet sem. Suspendisse molestie velit vitae mattis tincidunt. Ut sit amet quam mollis, vulputate turpis vel, sagittis felis.</p>
    </f7-block>

    <f7-row>
      <!--- Left Column --->
      <f7-col width="100" medium="50">
        
        <!-- Form for Submission -->
        <form class="list" id="my-form">
          <f7-list no-hairlines-md>
          <f7-list-input
            label="Author"
            floating-label
            type="text"
            placeholder="Author Name"
            clear-button
          >
            <f7-icon icon="bookmark" slot="media"></f7-icon>
          </f7-list-input>

          <f7-list-input
            label="Password"
            floating-label
            type="password"
            placeholder="Your password"
            clear-button
          >
            <f7-icon icon="demo-list-icon" slot="media"></f7-icon>
          </f7-list-input>

          <f7-list-input
            label="E-mail"
            floating-label
            type="email"
            placeholder="Your e-mail"
            clear-button
          >
            <f7-icon icon="demo-list-icon" slot="media"></f7-icon>
          </f7-list-input>

          <f7-list-input label="URL" floating-label type="url" placeholder="URL" clear-button>
            <f7-icon icon="demo-list-icon" slot="media"></f7-icon>
          </f7-list-input>

          <f7-list-input
            label="Phone"
            floating-label
            type="tel"
            placeholder="Your phone number"
            clear-button
          >
            <f7-icon icon="demo-list-icon" slot="media"></f7-icon>
          </f7-list-input>

          <f7-list-input
            label="Resizable"
            floating-label
            type="textarea"
            resizable
            placeholder="Bio"
          >
            <f7-icon icon="demo-list-icon" slot="media"></f7-icon>
          </f7-list-input>
        </f7-list>
        <div class="block">
          <p class="row">
             <button class="button col">Reset</button>
            <button class="col button button-raised button-fill">Submit</button>
            
          </p>
        </div>
        </form>
        
      </f7-col>

      <!--- Right Column --->
      <f7-col width="100" medium="50">

        <!-- Data Table Begin -->
        <div class="card data-table">
          <div class="card-header"> 
            <div class="data-table-title">User List</div>
            <div class="data-table-actions">
            <a class="link icon-only">
                <i class="icon f7-icons if-not-md">more_vertical_round</i>
                <i class="icon material-icons md-only">more_vert</i>
            </a>
            </div>
          </div class="card-content">
          <div>
          </div>
          <table>
            <thead>
              <tr>
                <th class="sortable-cellS">
                  <span class="table-head-label">ID</span>
                  
                </th>
                <th class="input-cell sortable-cell">
                  <span class="table-head-label">Author</span>
                  <div class="input">
                    <input type="text" placeholder="Filter" />
                  </div>
                </th>
                <th class="input-cell sortable-cell">
                  <span class="table-head-label">Title</span>
                  <div class="input">
                    <input type="text" placeholder="Filter" />
                  </div>
                </th>
                <th class="input-cell sortable-cell">
                  <span class="table-head-label">Content</span>
                  <div class="input">
                    <input type="text" placeholder="Filter" />
                  </div>
                </th>
                <th class="input-cell sortable-cell">
                  <span class="table-head-label">Last Updated</span>
                  <div class="input">
                    <input type="text" placeholder="Filter" />
                  </div>
                </th>
                <th class="input-cell sortable-cell">
                  <span class="table-head-label">Slug</span>
                  <div class="input">
                    <input type="text" placeholder="Filter" />
                  </div>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="blog in blogs" :key="blogs.id">
                <td>{{ blog.id }}</td>
                <td>{{ blog.author }}</td>
                <td>{{ blog.title }}</td>
                <td>{{ blog.content }}</td>
                <td>{{ blog.last_updated }}</td>
                <td>{{ blog.slug }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- END Data Table -->
      </f7-col>
    </f7-row>

    <f7-block-title medium>Block with Special (inset) Formatting</f7-block-title>
    <f7-block strong inset>
      <p>Donec et nulla auctor massa pharetra adipiscing ut sit amet sem. Suspendisse molestie velit vitae mattis tincidunt. Ut sit amet quam mollis, vulputate turpis vel, sagittis felis.</p>
    </f7-block>

    <f7-block-title medium>Block with Special (inset) Formatting</f7-block-title>
    <f7-block strong inset>
      <p>Donec et nulla auctor massa pharetra adipiscing ut sit amet sem. Suspendisse molestie velit vitae mattis tincidunt. Ut sit amet quam mollis, vulputate turpis vel, sagittis felis.</p>
    </f7-block>

    <f7-block-title medium>Block with Special (inset) Formatting</f7-block-title>
    <f7-block strong inset>
      <p>Donec et nulla auctor massa pharetra adipiscing ut sit amet sem. Suspendisse molestie velit vitae mattis tincidunt. Ut sit amet quam mollis, vulputate turpis vel, sagittis felis.</p>
    </f7-block>
    
  </f7-page>
</template>

<script>
import { mapState } from "vuex";

export default {
  data: function() {
    return {
      loading: false,
      effect: null,
			myblogs: [
        {
          id: 1,
          author: "Ian Christensen",
          title: "The new age of computing",
          content: "let me start by saying that programming is...",
          last_updated: "2019-08-05",
          slug: "New Programs"
        },
        {
          id: 2,
          author: "Billy Mantly",
          title: "The art of teaching",
          content: "The secret to ganing knowloedge consists of the following...",
          last_updated: "2019-08-05",
          slug: "Making it Happen"
        },
        {
          id: 3,
          author: "George Strait",
          title: "Welcome to this world",
          content: "let me play you domr music...",
          last_updated: "2019-08-05",
          slug: "Music Galore"
        },
        {
          id: 4,
          author: "John the Baptist",
          title: "The coming of Christ",
          content: "Get ready becasue things are about to change...",
          last_updated: "2019-08-05",
          slug: "New Life"
        },
        {
          id: 5,
          author: "Benjamin Franklin",
          title: "How I invented the telegraph",
          content: "It was a complete fluke becasue I was trying to make a light bulb...",
          last_updated: "2019-08-05",
          slug: "Lets talk it over"
        },
        {
          id: 6,
          author: "Donald Trump",
          title: "The most powerful lunatic in the world",
          content: "The path to the top is paved by the people I walk on...",
          last_updated: "2019-08-05",
          slug: "Get out of the way!"
        },
      ]
    };
  },
  methods: {
    load: function(effect) {
      var self = this;
      if (self.loading) return;
      self.effect = effect;
      self.loading = true;
      setTimeout(() => {
        self.loading = false;
      }, 3000);
    }
	},
	computed: mapState(["blogs"]),
  beforeCreate() {
    this.$store.dispatch("fetchBlogs");
  },
  created() {
    this.$store.watch(
      (state, getters) => getters.getBlogs,
      payload => {
        console.log(payload, "created response");
      }
    );
  }
};
</script>