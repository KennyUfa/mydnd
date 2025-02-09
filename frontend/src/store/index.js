import { createStore } from "vuex";
import { auth } from "./auth.module";
import { champion } from "./champion.module";
import { spellbook } from "./spellbook.module";
import { item } from "./item.module";
import { origin } from "./origin.module";
import { getrand } from "./getrand.module";
import { list_characters } from "./list_characters.module";

const store = createStore({
  modules: {
    auth,
    list_characters,
    champion,
    spellbook,
    item,
    origin,
    getrand,
  },
});
export default store;
