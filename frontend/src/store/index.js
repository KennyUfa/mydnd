import { createStore } from "vuex";
import { auth } from "./auth.module";
import { champion } from "./champion.module";
import { spellbook } from "./spellbook.module";
import { item } from "./item.module";

const store = createStore({
  modules: {
    auth,
    champion,
    spellbook,
    item
  },
});

export default store;