import { createWebHistory, createRouter } from "vue-router";
import LoginView from "./components/LoginView.vue";
import CharList from './components/CharList.vue'

const routes = [

  {
    path: "/login",
    component: LoginView,
  },
  {
    path: "/",
    component: CharList,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;