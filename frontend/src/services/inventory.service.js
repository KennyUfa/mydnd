import api from "./api";

class InventoryApi {
    async getInventoryList(search = '') {
        const response = await api.get("dnd/item/");
        if (response.data) {
            return response.data;
        } else {
            console.log(response);
        }
    };

    async getInventoryDetail(id) {
        const response = await api.get("dnd/item/" + id);
        if (response.data) {
            return response.data;
        } else {
            console.log(response);
        }
    };
}

export default new InventoryApi();