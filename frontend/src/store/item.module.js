import InventoryApi from "../services/inventory.service";

export const item = {
    namespaced: true,

    state: {
        itemList: NaN,
    },
    actions: {
        getData({commit, state}, search) {
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
        getDetailSpell({commit, state,}, id) {
            return InventoryApi.getSpellDetail(id).then(
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
            state.spell_detail = data;
        },
        dataFailure(state) {
            state.spellList = [];
            console.log('dataFailure')
        },
    },
    getters: {}
}