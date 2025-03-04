import DndListService from "../services/charlist.service.js";

const initialChampion_id = JSON.parse(localStorage.getItem("champion_id"));
export const champion = {
    namespaced: true,
    state: {
        isLoading: false,
        champion_id: initialChampion_id,
        listInfo: {
            name: "",
            race: {
                name: "",
                id: 0,
            },
            champion_class: {},
            lvl: 1,
            world_outlook: {},
            current_hit: 0,
            max_hit: 0,
            temp_hit: 0,
            my_items: [],
            origin: {
                name: "",
                id: 0,
            }
        },
        worldoutlooklist: [],

    },

    actions: {
        getData({commit, state}) {
            return DndListService.getChampionData(state.champion_id).then(
                (data) => {
                    localStorage.setItem("champion_id", state.champion_id);
                    commit("dataSuccess", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        loadWorldOutlook({commit}) {
            return DndListService.getWorldOutlook().then(
                (data) => {
                    commit("WorldOutlookListEdit", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        postSkills({commit, state}) {
            const data = {
                strength: state.listInfo.strength,
                id: state.listInfo.id,
                dexterity: state.listInfo.dexterity,
                constitution: state.listInfo.constitution,
                intelligence: state.listInfo.intelligence,
                wisdom: state.listInfo.wisdom,
                charisma: state.listInfo.charisma,
            };
            return DndListService.postSkills(data).then(
                (data) => Promise.resolve(data),
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        postBackground({commit, state}) {
            const data = {background: state.listInfo.background};
            return DndListService.postBackground(data, state.champion_id).then(
                (data) => Promise.resolve(data),
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        postProficienciesAndLanguages({commit, state}) {
            const data = {ProficienciesAndLanguages: state.listInfo.ProficienciesAndLanguages};
            return DndListService.postBackground(data, state.champion_id).then(
                (data) => Promise.resolve(data),
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchProtectSkills({commit, state}) {
            const data = {protect_char_state: state.listInfo.protect_char_state};
            return DndListService.postBackground(data, state.champion_id).then(
                (data) => Promise.resolve(data),
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchAbilitySkills({commit, state}) {
            const data = {skill_state: state.listInfo.skill_state};
            return DndListService.postBackground(data, state.champion_id).then(
                (data) => Promise.resolve(data),
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchMainInfo({commit, state}) {
            const data = {
                name_champion: state.listInfo.name_champion,
                level: state.listInfo.level,
            };
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => {
                    commit("dataSuccess", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchPossessionBonus({commit, state}) {
            const data = {possession_bonus: state.listInfo.possession_bonus};
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => Promise.resolve(data),
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchProtectionClass({commit, state}) {
            const data = {protection_class: state.listInfo.protection_class};
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => Promise.resolve(data),
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchSpeed({commit, state}) {
            const data = {speed: state.listInfo.speed};
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => Promise.resolve(data),
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchInspirationFrame({commit, state}) {
            const data = {inspiration: state.listInfo.inspiration};
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => Promise.resolve(data),
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchHit({commit, state}) {
            const data = {
                max_hit: state.listInfo.max_hit,
                temp_hit: state.listInfo.temp_hit,
                current_hit: state.listInfo.current_hit,
            };
            return DndListService.patchMainInfo(data, state.champion_id).then(
                (data) => Promise.resolve(data),
                (error) => {
                    console.log(error.request.responseText);
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },

        addSpell({commit, state}, id) {
            state.listInfo.spells_id.push(id);
            const data = {spells_id: state.listInfo.spells_id};
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
            const data = {spells_id: state.listInfo.spells_id.filter((value) => id !== value)};
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
        addItem({commit, state}, id_item) {
            const data = {item_id: id_item};
            return DndListService.itemPost(data, state.champion_id).then(
                (data) => {
                    commit("itemSuccess", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        patchItem({commit, state}) {
            const data = {my_items: state.listInfo.my_items};
            return DndListService.itemPatch(data, state.champion_id).then(
                (data) => {
                    commit("itemsSuccess", data);
                    return Promise.resolve(data);
                },
                (error) => {
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );
        },
        deleteItem({commit, state}, id) {
            const data = {items_id: state.listInfo.items_id.filter((value) => id !== value)};
            return DndListService.itemPatch(data, state.champion_id).then(
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
            const data = {current_hit: state.listInfo.current_hit};
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
                current_hit: state.listInfo.current_hit,
                temp_hit: state.listInfo.temp_hit,
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
        changeWorldOutlook({commit, state}, selected) {
            return DndListService.worldOutlookPatch(selected, state.champion_id).then(
                (data) => {
                    commit("champion/mutWorldOutlook", selected, {root: true});
                    return Promise.resolve(data);
                },
                (error) => {
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );

        },
        updateHideOriginal({commit, state}, ability_id) {
            const data = {
                custom_ability_id: ability_id.customAbilityId,
                original_ability_id: ability_id.OriginalAbilityId
            };
            return DndListService.UpdateAbilityHideOriginal(data, state.champion_id).then(
                (response) => {
                    commit("updateCustomDescription", {
                        abilityId: ability_id.OriginalAbilityId,
                        updatedData: {
                            id: response.id,
                            custom_description: response.custom_description,
                            hide_original: response.hide_original
                        }
                    });
                    return Promise.resolve(response);
                },
                (error) => {
                    commit("dataFailure");
                    return Promise.reject(error);
                }
            );

        }
    },
    mutations: {

        dataSuccess(state, data) {
            state.listInfo = data;
        }
        ,
        updateCustomDescription(state, payload) {
            const {abilityId, updatedData} = payload;

            // Ищем способность в массиве levels
            for (const level of state.listInfo.champion_class.levels) {
                const ability = level.abilities.find(ability => ability.id === abilityId);
                if (ability) {
                    // Обновляем custom_description
                    ability.custom_description = updatedData;
                    break;
                }
            }
        }
        ,
        itemSuccess(state, data) {
            state.listInfo.my_items.push(data);
        }
        ,
        originSuccess(state, data) {
            state.listInfo.origin = data.name;
        }
        ,
        change(state, id) {
            state.champion_id = id;
            localStorage.setItem("champion_id", state.champion_id);
        }
        ,
        itemsSuccess(state, data) {
            state.listInfo.my_items = data;
        }
        ,
        dataFailure(state) {
            state.listInfo = null;
        }
        ,
        WorldOutlookListEdit(state, data) {
            state.worldoutlooklist = data;
        }
        ,
        mutWorldOutlook(state, data) {
            state.listInfo.world_outlook = data.name;
        }
        ,
        mutHealHit(state, hit) {
            state.listInfo.current_hit = Math.min(state.listInfo.current_hit + hit, state.listInfo.max_hit);
        }
        ,
        mutDamageHit(state, hit) {
            let state_hit = state.listInfo.temp_hit - hit;
            if (state_hit >= 0) {
                state.listInfo.temp_hit = state_hit;
            } else {
                state.listInfo.temp_hit = 0;
                state.listInfo.current_hit = Math.max(state.listInfo.current_hit + state_hit, 0);
            }
        }
        ,
        updateName(state, data) {
            state.listInfo.name_champion = data;
        }
        ,
        switchProtectState(state, skill) {
            state.listInfo.protect_state[skill] = state.listInfo.protect_state[skill] === 1 ? 2 : 1;
        }
        ,
        switchAbilityState(state, skill) {
            state.listInfo.skill_state[skill] = (state.listInfo.skill_state[skill] % 3) + 1;
        }
        ,
    },
    getters: {
        getChampionId(state) {
            return state.champion_id;
        },
        getChampionClass(state) {
            return state.listInfo.champion_class;
        },
    },
};