import RandomApi from "@/services/random.service";

export const getrand = {
  namespaced: true,
  state: {},
  actions: {
    getRandomProtect({ rootGetters, commit }, params) {
      const championId = rootGetters["champion/getChampionId"];
      const skillValue = params.skillValue;
      const statValue = params.stat;

      return RandomApi.getRandomSave(skillValue, championId, statValue).then(
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
