import {createWebHistory, createRouter} from "vue-router";
import LoginView from "./components/LoginView.vue";
import CharList from "./components/CharList.vue";
import CharactersView from "./components/CharactersView.vue";
import store from "./store";


const routes = [
    {
        path: "/",
        component: LoginView,
    },
    {
        path: "/charlist",
        component: CharList,
        async beforeEnter(to, from, next) {
            console.log('start')
            const res = await store.dispatch("champion/getData");
            console.log(store.state.champion.listInfo);
            if (store.state.champion.listInfo) {
                next()
            }
        }
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
