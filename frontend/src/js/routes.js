import HomePage from '../pages/home.vue';
import Summary from '../pages/class_registration/summary.vue';
import Checkout from '../pages/checkout/checkout.vue';
import Admin from '../pages/admin_panel/admin.vue';

import AdminClassSetting from '../pages/admin_panel/class_settings.vue';
import AdminCreateClass from '../pages/admin_panel/create_class.vue';
import AdminNotifications from '../pages/admin_panel/notifications.vue';
import AdminOrderList from '../pages/admin_panel/order_list.vue';
import AdminEmail from '../pages/admin_panel/email.vue';
import AdminUsers from '../pages/admin_panel/users.vue';

import NotFoundPage from '../pages/404.vue';

var routes = [
  {
    path: '/',
    component: HomePage,
  },
  {
    path: '/summary/',
    component: Summary,
  },
  {
    path: '/checkout/',
    component: Checkout,
  },
 {
    path: '/admin/',
    component: Admin,
  },
  {
    path: '/admin/class-settings/',
    component: AdminClassSetting,
  },
  {
    path: '/admin/create-class/',
    component: AdminCreateClass,
  },
  {
    path: '/admin/notifications/',
    component: AdminNotifications,
  },
  {
    path: '/admin/orders/',
    component: AdminOrderList,
  },
  {
    path: '/admin/email/',
    component: AdminEmail,
  },
  {
    path: '/admin/users/',
    component: AdminUsers,
  },

  {
    path: '(.*)',
    component: NotFoundPage,
  },
];

export default routes;
