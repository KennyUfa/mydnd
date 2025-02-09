import { createWebHistory, createRouter } from "vue-router";
import LoginView from "@/components/LoginView";
import CharList from "./components/CharList.vue";
import CharactersView from "./components/CharactersView.vue";
import store from "./store";
import SpellBookView from "./components/SpellBook/SpellBookView.vue";
import SpellDetailView from "./components/SpellBook/SpellDetailView.vue";
import Inventory from "./components/Inventory/InventoryView.vue";

const routes = [
  {
    path: "/",
    component: LoginView,
  },
  {
    path: "/spellbook",
    component: SpellBookView,
    beforeEnter: (to, from, next) => {
      if (store.state.spellbook.spellList) {
        next();
      } else {
        return store.dispatch("spellbook/getData").then(() => {
          if (store.state.spellbook.spellList) {
            next();
          }
        });
      }
    },
  },
  {
    path: "/spellbook/:id",
    component: SpellDetailView,
    props: true,
    async beforeEnter(to, from, next) {
      await store.dispatch("spellbook/getDetailSpell", to.params.id);
      if (store.state.spellbook.spell_detail) {
        next();
      }
    },
  },
  {
    path: "/charlist",
    component: CharList,
    async beforeEnter(to, from, next) {
      await store.dispatch("champion/getData");
      if (store.state.champion.listInfo) {
        next();
      }
    },
  },
  {
    path: "/database",
    component: Inventory,
    beforeEnter: (to, from, next) => {
      if (store.state.item.itemList) {
        next();
      } else {
        return store.dispatch("item/getData").then(() => {
          if (store.state.item.itemList) {
            next();
          }
        });
      }
    },
  },
  {
    path: "/database/:id",
    component: SpellDetailView,
    props: true,
    async beforeEnter(to, from, next) {
      await store.dispatch("database/getDetail", to.params.id);
      if (store.state.spellbook.spell_detail) {
        next();
      }
    },
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
