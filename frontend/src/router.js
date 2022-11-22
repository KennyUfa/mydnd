
import { createWebHistory, createRouter } from "vue-router";
import Login from './components/Login.vue';
import CharlistView from './components/CharlistView.vue';

const routes = [
    {
      path: "/charlist",
      name: "charlist",
      component: CharlistView,
    },
    {
      path: "/login",
      component: Login,
      alias:'/'
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
  });

export default router;