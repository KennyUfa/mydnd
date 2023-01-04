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

    async postRename(name) {
        const response = await api.get("dnd/character");
        if (response.data) {
            return response.data;
        } else {
            console.log(response);
        }
    }

    async getCharacters() {
        const response = await api.get("dnd/character");
        if (response.data) {
            return response.data;
        } else {
            console.log(response);
        }
    }

    async getChampionsList() {
        const response = await api.get("dnd/character/");
        if (response.data) {
            return response.data
        } else {
            console.log(response);
        }
    }

    async deleteChampion(id) {
        console.log(id);
        const response = await api.delete("dnd/character/" + id + "/");
        if (response.data) {
            return response.data
        } else {
            console.log(response);
        }

    }
}

export default new ChampionApi();
