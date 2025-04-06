import api from "@/services/api.js";
import {useCharacterStore} from "@/stores/characterStore.js";
import {defineStore} from "pinia";

export const useInventoryStore = defineStore("Inventory", {
    state: () => ({
        item_list: [],
        item_details: NaN,
        rarity_list: {
            'Обычный': 1,
            'Редкий': 3,
            'Очень редкий': 4,
            'Легендарный': 5,
            'Артефакт': 6,
            'Редкость варьируется': 7,
            'Редкость не определена': 8,
            'Необычный': 2,
        },
        searchListRarity: []
    }),
    actions: {
        async getInventory(search = "") {
            const response = await api.get("dnd/items", {
                params: {
                    'search': search,
                    'rarity': this.searchListRarity,
                }
            });
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
        async patchInventoryItem() {
            const characterStore = useCharacterStore();
            const response = await api.patch('dnd/character/' + characterStore.get_character_id + '/inventory/', characterStore.character.my_items);
            characterStore.character.my_items = response.data;
        },
        async getDescriptionItem(item) {
            const response = await api.get('dnd/items/' + item.id + '/');
            this.item_details = response.data;
        }
    }
});