import api from "./api";

class ChampionApi {
    async getChampionData(id) {
        console.log(id)
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
            return 'delet'+id
        }
    }

    async createPostChampion(data) {

        const response = await api.post("dnd/character/", data);
        if (response.data) {
            return response.data;
        } else {
            console.log(response);
        }
    }

    async getClassList() {
        const response = await api.get("dnd/bc/");
        if (response.data) {
            return response.data;
        } else {
            console.log(response);
        }
    }
}

export default new ChampionApi();
