import api from "./api";

class RandomApi {
  async getRandomSave(protectValueName, championId, statValue) {
    const data = { protectValueName, championId, statValue };
    // console.log(data);
    const response = await api.post("dnd/random_protect/", data);
    if (response.data) {
      // console.log(response.data.total);
      return response.data;
    } else {
      console.log(response);
    }
  }

  async getRandomAbility(abilityValueName, championId, statValue) {
    const data = { abilityValueName, championId, statValue };
    // console.log(data);
    const response = await api.post("dnd/random_protect/", data);
    if (response.data) {
      // console.log(response.data.total);
      return response.data;
    } else {
      console.log(response);
    }
  }
}

export default new RandomApi();
