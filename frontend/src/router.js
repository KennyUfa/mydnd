import { createWebHistory, createRouter } from "vue-router";
import LoginView from "./components/LoginView.vue";
import CharList from './components/CharList.vue'

const routes = [

  {
    path: "/",
    component: LoginView,
  },
  {
    path: "/charlist",
    component: CharList,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;