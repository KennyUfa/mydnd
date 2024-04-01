import api from "./api";

class RandomApi {
  async getRandomSave(skillValue, championId, statValue) {
    const data = { skillValue, championId, statValue };
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
