import SpellBookService from "../services/spellBook.service";

export const spellbook = {
    namespaced: true,

    state: {
        spellList:NaN,
        spell_detail: NaN,
    },
    actions: {
        getData({commit, state}) {
            return SpellBookService.getSpellList('').then(
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
        getDetailSpell({commit, state,},id) {
            return SpellBookService.getSpellDetail(id).then(
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
            state.spellList = data;
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