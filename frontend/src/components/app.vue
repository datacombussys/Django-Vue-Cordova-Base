<template>
<f7-app :params="f7params" >

  <!-- Left panel with cover effect-->
  <f7-panel left cover theme-dark>
    <f7-view>
      <f7-page>
        <f7-navbar title="Left Panel"></f7-navbar>
          <f7-list>
            <f7-list-item link="/admin/" title="Dashboard"
            view=".view-main" panel-close>
              <f7-icon slot="media" f7="gauge"></f7-icon>
            </f7-list-item>
            <f7-list-item link="/admin/class-settings/'" title="Class Settings"
            view=".view-main" panel-close>
              <f7-icon slot="media" f7="gear"></f7-icon>
            </f7-list-item>
            <f7-list-item link="/admin/create-class/" title="Create Classes"
            view=".view-main" panel-close>
              <f7-icon slot="media" f7="plus_circle_fill"></f7-icon>
            </f7-list-item>
            <f7-list-item link="/admin/orders/" title="Orders List"
            view=".view-main" panel-close>
              <f7-icon slot="media" f7="square_list_fill"></f7-icon>
            </f7-list-item>
            <f7-list-item link="/admin/notifications/" title="Notifications"
            view=".view-main" panel-close>
              <f7-icon slot="media" f7="bell_fill"></f7-icon>
            </f7-list-item>
            <f7-list-item link="/admin/email/" title="Email Templates"
            view=".view-main" panel-close>
              <f7-icon slot="media" f7="envelope_fill"></f7-icon>
            </f7-list-item>
            <f7-list-item link="/admin/users/" title="Users"
            view=".view-main" panel-close>
              <f7-icon slot="media" f7="person_3_fill"></f7-icon>
            </f7-list-item>
          </f7-list>
     
      </f7-page>
    </f7-view>
  </f7-panel>


  <!-- Your main view, should have "view-main" class -->
  <f7-view main class="safe-areas" url="/"></f7-view>

  <f7-login-screen id="my-login-screen">
    <f7-view>
      <f7-page login-screen>
        <f7-login-screen-title>Login</f7-login-screen-title>
        <f7-list form>
          <f7-list-input
            type="text"
            name="username"
            placeholder="Your username"
            :value="username"
            @input="username = $event.target.value"
          ></f7-list-input>
          <f7-list-input
            type="password"
            name="password"
            placeholder="Your password"
            :value="password"
            @input="password = $event.target.value"
          ></f7-list-input>
        </f7-list>
        <f7-list>
          <f7-list-button title="Sign In" login-screen-close @click="alertLoginData"></f7-list-button>
          <f7-block-footer>
            Some text about login information.<br>Click "Sign In" to close Login Screen
          </f7-block-footer>
        </f7-list>
      </f7-page>
    </f7-view>
  </f7-login-screen>
</f7-app>
</template>



<script>

  import routes from '../js/routes.js';

  export default {
    data() {
      return {
        // Framework7 Parameters
        f7params: {
          name: 'ABC So-Cal', // App name
          theme: 'auto', // Automatic theme detection
          // App root data
          data: function () {
            return {
              user: {
                firstName: 'Ian',
                lastName: 'Christensen',
              },

            };
          },

          // App routes
          routes: routes,
          // Register service worker -temporarily disabled
          // serviceWorker: {
          //   path: '/service-worker.js',
          // },
        },

        // Login screen data
        username: '',
        password: '',
      }
    },
    methods: {
      alertLoginData() {
        this.$f7.dialog.alert('Username: ' + this.username + '<br>Password: ' + this.password);
      }
    },
    mounted() {
      this.$f7ready((f7) => {

        // Call F7 APIs here
      });
    }
  }
</script>