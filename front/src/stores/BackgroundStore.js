import {defineStore} from "pinia";
import api from "@/services/api.js";
import {useCharacterStore} from "@/stores/characterStore.js";

export const useBackground = defineStore("background", {
        state: () => ({
            background: null,
            background_list: [],
        }),
        actions: {
            setBackground(data) {
                this.background = data; // Устанавливаем ссылку на данные
            },
            async loadBackgrounds() {
                try {
                    const response = await api.get("dnd/background-list/");
                    this.background_list = response.data;
                } catch (error) {
                    console.error('Ошибка при получении списка archetypes:', error);
                }
            },
            async changeBackground(id) {
                const characterStore = useCharacterStore();
                try {
                    const response = await api.patch("dnd/character/" + characterStore.get_character_id + "/background-change/", id);
                    this.background = response.data;
                } catch (error) {
                    console.error('Ошибка при смене архетипа: error', error);
                }
            },
            async changeOptions(options) {
                try {
                    const response = await api.patch("dnd/character/" + useCharacterStore().get_character_id + "/background-options/", options);
                    this.background = response.data
                } catch (error) {
                    console.error('Ошибка при смене опций: error', error);
                }
            },
            async change(origin) {
                try {
                    const response = await api.patch("dnd/character/" + useCharacterStore().get_character_id + "/background-origin/", origin);

                    console.log(response)
                    this.background.selected_origins = response.data
                } catch (error) {
                    console.error('Ошибка при смене опций: error', error);
                }
            },

        }
    })
;