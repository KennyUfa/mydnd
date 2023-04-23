import api from "./api";

class InventoryApi {
  async getInventoryDetail(id) {
    const response = await api.get("dnd/item/" + id);
    if (response.data) {
      return response.data;
    } else {
      console.log(response);
    }
  }
}

export default new InventoryApi();
