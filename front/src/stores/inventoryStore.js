import {defineStore} from "pinia";
import api from "@/services/api.js";


export const useInventoryStore = defineStore("Inventory", {
    state: () => ({
        item_list: [],
    }),
    actions: {
        async getInventory(search = "") {
            const response = await api.get("dnd/items?search=" + search);
            this.item_list = response.data;
        }
    }
});