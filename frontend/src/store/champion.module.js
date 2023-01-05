import DndListService from "../services/charlist.service.js";

export const champion = {
    namespaced: true,

    state: {
        mychampions: [],
        lvl: 1,
        champion_id: 1,
        listInfo: NaN,
        create_champion: {
            name_champion: "",
            lvl: 1,
            champion_class:"",
        },
    },

    actions: {
        getData({commit, state}) {
            return DndListService.getChampionData(state.champion_id).then(
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
        getChampions({commit, state}) {
            return DndListService.getChampionsList(state.champion_id).then(
                (data) => {
                    commit("updateMychampions", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        deleteChampion({commit, state}, id) {
            return DndListService.deleteChampion(id).then(
                (data) => {
                    commit("DeleteMychampions", id);
                    return Promise.resolve(data);
                },
                (error) => {
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        createChampion({commit, state}) {
            return DndListService.createPostChampion(state.create_champion).then(
                (data) => {
                    commit("CreateMychampions", data);
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
        change(state, id) {
            state.champion_id = id;
        },
        updateMychampions(state, mychampions) {
            state.mychampions = mychampions;
        },
        DeleteMychampions(state, id) {
            state.mychampions=state.mychampions.filter((ch) => ch.id !== id)
        },
        CreateMychampions(state, data) {
            console.log('create mut');
            state.mychampions.push(data)
        },
    },
};
