import { createStore } from "vuex";
import { auth } from "./auth.module";
import { champion } from "./champion.module";
import { spellbook } from "./spellbook.module";

const store = createStore({
  modules: {
    auth,
    champion,
    spellbook
  },
});

export default store;