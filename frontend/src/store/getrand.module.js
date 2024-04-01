import RandomApi from "@/services/random.service";

export const getrand = {
  namespaced: true,
  state: {},
  actions: {
    getRandomProtect({ rootGetters, commit }, params) {
      const championId = rootGetters["champion/getChampionId"];
      const protectValueName = params.skillValue;
      const statValue = params.stat;

      return RandomApi.getRandomSave(
        protectValueName,
        championId,
        statValue
      ).then(
        (data) => {
          return Promise.resolve(data);
        },
        (error) => {
          console.log(error.request.responseText);
          commit("dataFailure");
          return Promise.reject(error);
        }
      );
    },
    getRandomAbility({ rootGetters, commit }, params) {
      const championId = rootGetters["champion/getChampionId"];
      const abilityValueName = params.skillValue;
      const statValue = params.stat;

      return RandomApi.getRandomAbility(
        abilityValueName,
        championId,
        statValue
      ).then(
        (data) => {
          return Promise.resolve(data);
        },
        (error) => {
          console.log(error.request.responseText);
          commit("dataFailure");
          return Promise.reject(error);
        }
      );
    },
  },
  mutations: {},
  getters: {},
};
