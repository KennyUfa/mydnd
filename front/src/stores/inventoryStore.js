import {defineStore} from "pinia";
import api from "@/services/api.js";
import {useCharacterStore} from "@/stores/characterStore.js";

export const useInventoryStore = defineStore("Inventory", {
    state: () => ({
        item_list: [],
    }),
    actions: {
        async getInventory(search = "") {
            const response = await api.get("dnd/items?search=" + search);
            this.item_list = response.data;
        },
        async patchItem(data) {
            const characterStore = useCharacterStore();
            const response = await api.post('dnd/character/' + characterStore.get_character_id + '/inventory/' + data.id + '/');
            characterStore.character.my_items.push(response.data);

        },
        async deleteItem(data) {
            const characterStore = useCharacterStore();
            const response = await api.delete('dnd/character/' + characterStore.get_character_id + '/inventory/' + data + '/');
            characterStore.character.my_items = characterStore.character.my_items.filter(
                (item) => item.item.id !== data
            );
        },
        async patchInventaryItem() {
            const characterStore = useCharacterStore();
            const response = await api.patch('dnd/character/' + characterStore.get_character_id + '/inventory/', characterStore.character.my_items);
            characterStore.character.my_items = response.data;
        },
    }
});