import DndListService from "../services/charlist.service.js";

const initialChampion_id = JSON.parse(localStorage.getItem("champion_id"))

export const champion = {
    namespaced: true,

    state: {
        classlist: NaN,
        racelist: NaN,
        prehistorylist: NaN,
        worldoutlooklist: NaN,
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
                    // commit("dataSuccess", data);
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
        loadPreHistory({commit, state}) {
            return DndListService.getPreHistory().then(
                (data) => {
                    commit("preHistoryListEdit", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        loadWorldOutlook({commit, state}) {
            return DndListService.getWorldOutlook().then(
                (data) => {
                    commit("WorldOutlookListEdit", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        postSkills({commit, state}) {
            const data = {
                "strength": state.listInfo.strength,
                'id': state.listInfo.id,
                "dexterity": state.listInfo.dexterity,
                "constitution": state.listInfo.constitution,
                "intelligence": state.listInfo.intelligence,
                "wisdom": state.listInfo.wisdom,
                "charisma": state.listInfo.charisma,
            };
            return DndListService.postSkills(data).then(
                (data) => {
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        postBackground({commit, state}) {
            const data = {
                "background": state.listInfo.background
            };
            return DndListService.postBackground(data, state.champion_id).then(
                (data) => {
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchProtectSkills({commit, state}) {
            const data = {
                "protect_char_state": state.listInfo.protect_char_state
            };
            return DndListService.postBackground(data, state.champion_id).then(
                (data) => {
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchAbilitySkills({commit, state}) {
            const data = {
                "skill_char_state": state.listInfo.skill_char_state
            };
            return DndListService.postBackground(data, state.champion_id).then(
                (data) => {
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchMainInfo({commit, state}) {
            const data = {
                "name_champion": state.listInfo.name_champion,
                'lvl': state.listInfo.lvl,
                "pre_history": state.listInfo.pre_history,
                "world_outlook": state.listInfo.world_outlook,
            };
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => {
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchPossessionBonus({commit, state}) {
            const data = {
                "possession_bonus": state.listInfo.possession_bonus,
            };
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => {
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        }, patchProtectionClass({commit, state}) {
            const data = {
                "protection_class": state.listInfo.protection_class,
            };
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => {
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        }, patchSpeed({commit, state}) {
            const data = {
                "speed": state.listInfo.speed,
            };
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => {
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchInspirationFrame({commit, state}) {
            const data = {
                "inspiration": state.listInfo.inspiration,
            };
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => {
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText)
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchHit({commit, state}) {
            const data = {
                "max_hit": state.listInfo.max_hit,
                "temp_hit": state.listInfo.temp_hit,
                "current_hit": state.listInfo.current_hit,
            };
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => {
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
        addSpell({commit, state}, id) {
            state.listInfo.spells_id.push(id);
            const data = {
                "spells_id": state.listInfo.spells_id
            };
            return DndListService.spellPatch(data, state.champion_id).then(
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
        deleteSpell({commit, state}, id) {
            let res = state.listInfo.spells_id.filter(value => id !== value);
            const data = {
                "spells_id": res
            };
            return DndListService.spellPatch(data, state.champion_id).then(
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
        heal({commit, state}, hit) {
            commit("mutHealHit", hit);
            const data = {
                "current_hit": state.listInfo.current_hit,
            };
            return DndListService.spellPatch(data, state.champion_id).then(
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
        damage({commit, state}, hit) {
            commit("mutDamageHit", hit);
            const data = {
                "current_hit": state.listInfo.current_hit,
                "temp_hit": state.listInfo.temp_hit,
            };
            return DndListService.spellPatch(data, state.champion_id).then(
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
        changeClass({commit}, selected) {
            return commit("mutChangeClass", selected);
        },
        changeRace({commit}, selected) {
            return commit("mutChangeRace", selected);
        },
        changeLvl({commit}, selected) {
            return commit("mutChangeLvl", selected);
        },
        changePreHistory({commit}, selected) {
            return commit("mutChangePreHistory", selected);
        },
        changeWorldOutlook({commit}, selected) {
            return commit("mutWorldOutlook", selected);
        },
    },
    mutations: {
        dataSuccess(state, data) {
            state.listInfo = data;
        },
        dataFailure(state) {
            state.listInfo = null;
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
        preHistoryListEdit(state, data) {
            state.prehistorylist = data
        },
        WorldOutlookListEdit(state, data) {
            state.worldoutlooklist = data
        },
        mutChangeClass(state, data) {
            state.create_champion.champion_class = data
        },
        mutChangePreHistory(state, data) {
            state.listInfo.pre_history = data
        },
        mutWorldOutlook(state, data) {
            state.listInfo.world_outlook = data
        },
        mutChangeRace(state, data) {
            state.create_champion.race = data
        },
        mutChangeLvl(state, data) {
            state.create_champion.lvl = data
        },
        mutHealHit(state, hit) {
            let state_hit = state.listInfo.current_hit + hit;
            if (state_hit > state.listInfo.max_hit) {
                state.listInfo.current_hit = state.listInfo.max_hit
            } else {
                state.listInfo.current_hit = state_hit
            }
        },
        mutDamageHit(state, hit) {
            let state_hit = state.listInfo.temp_hit - hit;
            if (state_hit > -1) {
                state.listInfo.temp_hit = state_hit
            } else {
                if (state_hit < 0) {
                    state.listInfo.temp_hit = 0
                    let new_state_hit = state.listInfo.current_hit + state_hit;
                    if (new_state_hit < state.listInfo.current_hit) {
                        state.listInfo.current_hit = 0
                    } else {
                        state.listInfo.current_hit = new_state_hit
                    }
                } else {
                    state.listInfo.temp_hit = state_hit
                }
            }
        },
        updateName(state, data) {
            state.listInfo.name_champion = data
        },
        switchProtectState(state, skill) {
            switch (state.listInfo.protect_char_state[skill]) {
                case 1:
                    state.listInfo.protect_char_state[skill] = 2;
                    break;
                case 2:
                    state.listInfo.protect_char_state[skill] = 1;
                    break;
            }
        },
        switchAbilityState(state, skill) {
            switch (state.listInfo.skill_char_state[skill]) {
                case 1:
                    state.listInfo.skill_char_state[skill] = 2;
                    break;
                case 2:
                    state.listInfo.skill_char_state[skill] = 3;
                    break;
                case 3:
                    state.listInfo.skill_char_state[skill] = 1;
                    break;
            }
        }
    },
    getters: {
        getInspiration(state) {
            return state.listInfo.inspiration
        }
    }
};
