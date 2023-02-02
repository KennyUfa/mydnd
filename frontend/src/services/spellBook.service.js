import api from "./api";

class SpellBookApi {
    async getSpellList(search = '') {
        const response = await api.get("dnd/spell?search=" + search);
        if (response.data) {
            return response.data;
        } else {
            console.log(response);
        }
    };

    async getSpellDetail(id) {
        const response = await api.get("dnd/spell/" + id);
        if (response.data) {
            return response.data;
        } else {
            console.log(response);
        }
    };
}

export default new SpellBookApi();