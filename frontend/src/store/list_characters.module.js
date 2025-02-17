import DndListService from "../services/charlist.service.js";

const initialChampion_id = JSON.parse(localStorage.getItem("champion_id"));

export const list_characters = {
    namespaced: true,
    state: {
        classlist: [],
        racelist: [],
        champion_id: initialChampion_id,
        name_champion: "",
        lvl: 1,
        race: {},
        champion_class: {},
        my_champions: [],
    },
    actions: {
        deleteChampion({commit}, id) {
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
        createChampion({commit, state}) {
            const data = {
                'name_champion': state.name_champion,
                'level': state.lvl,
                'race': state.race,
                'champion_class': state.champion_class,
            }
            return DndListService.createPostChampion(data).then(
                (data) => {
                    commit("CreateMychampions", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        loadClassList({commit}) {
            return DndListService.getClassList().then(
                (data) => {
                    commit("classListEdit", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        loadRaceList({commit}) {
            return DndListService.getRaceList().then(
                (data) => {
                    commit("raceListEdit", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        changeClass({commit}, selected) {
            return commit("mutChangeClass", selected);
        },
        changeRace({commit}, selected) {
            return commit("mutChangeRace", selected);
        },
        changeLvl({commit}, selected) {
            return commit("mutChangeLvl", selected);
        },
    },
    mutations: {
        updateMychampions(state, champions) {
            state.my_champions = champions;
        },
        DeleteMychampions(state, id) {
            state.my_champions = state.my_champions.filter((ch) => ch.id !== id);
            state.isLoading = true;
        },

        CreateMychampions(state, data) {
            state.my_champions.push(data);
        },
        classListEdit(state, data) {
            state.classlist = data;
        },
        raceListEdit(state, data) {
            state.racelist = data;
        },
        mutChangeClass(state, data) {
            state.champion_class = data;
        },
        mutChangeRace(state, data) {
            state.race = data;
        },
        mutChangeLvl(state, data) {
            state.lvl = data;
        },
    }
}
