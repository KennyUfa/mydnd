import { createStore } from "vuex";
import { auth } from "./auth.module";
import { champion } from "./champion.module";
import { spellbook } from "./spellbook.module";
import { item } from "./item.module";
import { origin } from "./origin.module";
import { getrand } from "./getrand.module";

const store = createStore({
  modules: {
    auth,
    champion,
    spellbook,
    item,
    origin,
    getrand,
  },
});
export default store;
