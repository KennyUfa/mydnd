import { createStore } from "vuex";
import { auth } from "./auth.module";
import { champion } from "./champion.module";

const store = createStore({
  modules: {
    auth,
    champion,
  },
});

export default store;