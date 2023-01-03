import DndListService from "../services/charlist.service.js";

export const champion = {
  namespaced: true,
  state: {
    levl: 1,
    listInfo: NaN,
  },
  actions: {
    getData({ commit }) {
      return DndListService.getChampionData().then(
        (data) => {
          commit("dataSuccess", data);
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
    dataSuccess(state, data) {
      state.listInfo = data;
    },
    dataFailure(state) {
      state.listInfo = null;
    },
    updateName_champion(state, name_champion) {
      state.listInfo.name_champion = name_champion;

    },
}
}