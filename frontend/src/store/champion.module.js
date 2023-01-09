import DndListService from "../services/charlist.service.js";


const initialChampion_id = JSON.parse(localStorage.getItem("champion_id"))

export const champion = {
    namespaced: true,

    state: {
        classlist: NaN,
        racelist: NaN,
        isLoading: false,
        mychampions: [],
        lvl: 1,
        champion_id: initialChampion_id,
        listInfo: NaN,
        create_champion: {
            name_champion: "",
            lvl: 1,
            race: "Выберите рассу",
            champion_class: "Выбрать класс",
        },
    },

    actions: {
        getData({commit, state}) {
            return DndListService.getChampionData(state.champion_id).then(
                (data) => {
                    localStorage.setItem("champion_id", state.champion_id)
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
                    commit("dataSuccess", data);
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
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        // загрузка выбора класса героя
        loadClassList({commit, state}) {
            return DndListService.getClassList().then(
                (data) => {
                    commit("classListEdit", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        loadRaceList({commit, state}) {
            return DndListService.getRaceList().then(
                (data) => {
                    commit("raceListEdit", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
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
        }
    },
    mutations: {
        dataSuccess(state, data) {
            state.listInfo = data;
            state.isLoading = true;
        },
        dataFailure(state) {
            state.listInfo = null;
        },

        // Статус загрузки
        isLoadingStart(state) {
            state.isLoading = false;
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
            state.mychampions = state.mychampions.filter((ch) => ch.id !== id)
            state.isLoading = true;
        },
        CreateMychampions(state, data) {
            state.mychampions.push(data)
        },
        classListEdit(state, data) {
            state.classlist = data
        },
        raceListEdit(state, data) {
            state.racelist = data
        },
        mutChangeClass(state, data) {
            state.create_champion.champion_class = data
        },
        mutChangeRace(state, data) {
            state.create_champion.race = data
        },
        mutChangeLvl(state, data) {
            state.create_champion.lvl = data
        },
    },
};
