import api from "./api";

class ChampionApi {
  async getChampionData(id) {
    const response = await api.get("dnd/character/" + id + "/");
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async getChampionsList() {
    const response = await api.get("dnd/character/");
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async deleteChampion(id) {
    const response = await api.delete("dnd/character/" + id + "/");
    if (response.data) {
      return response.data;
    } else {
      return "delet" + id;
    }
  }

  async createPostChampion(data) {
    console.log(data);
    const response = await api.post("dnd/character/", data);
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async getClassList() {
    const response = await api.get("dnd/classlist/");
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async getPreHistory() {
    const response = await api.get("dnd/prehistory/");
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async getRaceList() {
    const response = await api.get("dnd/racelist/");
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async getWorldOutlook() {
    const response = await api.get("dnd/looklist/");
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async postSkills(data) {
    const response = await api.patch("dnd/character/" + data.id + "/", data);
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async postBackground(data, id) {
    const response = await api.patch("dnd/character/" + id + "/", data);
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async patchMainInfo(data, id) {
    const response = await api.patch("dnd/character/" + id + "/", data);
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }
  async spellPatch(data, id) {
    const response = await api.patch("dnd/character/" + id + "/", data);
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }
}

export default new ChampionApi();
