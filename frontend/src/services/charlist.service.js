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
    const response = await api.get("dnd/characterlist/");
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async deleteChampion(id) {
    const response = await api.delete("dnd/characters/delete/" + id + "/");
    if (response.data) {
      return response.data;
    } else {
      return "delete" + id;
    }
  }

  async createPostChampion(data) {
    console.log(data);
    const response = await api.post("dnd/characters/create/", data);
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

  async getOrigin() {
    console.log("loadlistorigin");
    const response = await api.get("dnd/originlist/");
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

  async originPatch(origin, id_character) {
    const data = { origin_id: origin.id};
    const response = await api.patch(
      "/dnd/characters/" + id_character.character_id + "/origin/",
      data
    );
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }
async worldOutlookPatch(world_outlook, id_character) {
    const data = { world_outlook_id: world_outlook.id};
    const response = await api.patch(
      "/dnd/characters/" + id_character + "/world-outlook/",
      data
    );
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }
  async itemPost(data, id) {
    const response = await api.post(
      "/dnd/characters/" + id + "/inventory/",
      data
    );
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async itemPatch(data, id) {
    const response = await api.patch(
      "/dnd/characters/" + id + "/inventory/",
      data
    );
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }

  async UpdateAbilityHideOriginal(data, champion_id){
    const response = await api.patch(
      "/dnd/characters/" + champion_id + "/custom-ability/hide-original/",
      data
    );
    if (response.data) {
      return response.data;
    } else {
      console.log('UpdateAbilityHideOriginal',response);
    }
  }
}

export default new ChampionApi();
