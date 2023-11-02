import DndListService from "../services/charlist.service.js";

export const origin = {
  namespaced: true,
  state: {
    originlist: NaN,
  },
  actions: {
    loadOrigin({ commit }) {
      return DndListService.getOrigin().then(
        (data) => {
          commit("OriginListEdit", data);
          console.log("listorigin");
          return Promise.resolve(data);
        },
        (error) => {
          console.log(error.request.responseText);
          commit("dataFailure");
          return Promise.reject(error);
        }
      );
    },
    changeOrigin({ commit, rootState }, id_origin) {
      console.log("changeorigin");
      const character_id = {
        character_id: rootState.champion.champion_id, // Получить текущее значение champion_id из модуля champion
      };
      return DndListService.originPatch(id_origin, character_id).then(
        (data) => {
          commit("champion/dataSuccess", data, { root: true });
          return Promise.resolve(data);
        },
        (error) => {
          commit("dataFailure");
          return Promise.reject(error);
        }
      );
    },
  },
  mutations: {
    OriginListEdit(state, data) {
      state.originlist = data;
    },

    dataFailure(state) {
      console.log(state);
    },
  },
  getters: {},
};
