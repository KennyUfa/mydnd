import InventoryApi from "../services/inventory.service";

export const item = {
  namespaced: true,

  state: {
    itemList: NaN,
    item_detail: NaN,
  },
  actions: {
    getData({ commit }, search) {
      return InventoryApi.getInventoryList(search).then(
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
    getDetailItem({ commit }, id) {
      return InventoryApi.getInventoryDetail(id).then(
        (data) => {
          commit("dataDetailSuccess", data);
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
      state.itemList = data;
    },
    dataDetailSuccess(state, data) {
      state.item_detail = data;
    },
    dataFailure(state) {
      state.itemList = [];
      console.log("dataFailure");
    },
  },
  getters: {},
};
