import { createWebHistory, createRouter } from "vue-router";
import LoginView from "./components/LoginView.vue";
import CharList from "./components/CharList.vue";
import CharactersView from "./components/CharactersView.vue";

const routes = [
  {
    path: "/",
    component: LoginView,
  },
  {
    path: "/charlist",
    component: CharList,
  },
  {
    path: "/characters",
    component: CharactersView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
