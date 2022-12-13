import api from "./api";

class ChampionApi {
  async getChampionData() {
    const response = await api
      .get("dnd/character");
    if (response.data) {
        return response.data;
    }
  }}

  export default new ChampionApi();