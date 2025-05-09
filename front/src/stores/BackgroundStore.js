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
                    const response = await api.get("background/background-list/");
                    this.background_list = response.data;
                } catch (error) {
                    console.error('Ошибка при получении списка archetypes:', error);
                }
            },
            async changeBackground(id) {
                const characterStore = useCharacterStore();
                try {
                    const response = await api.patch("background/" + characterStore.get_character_id + "/background-change/", id);
                    this.background = response.data;
                } catch (error) {
                    console.error('Ошибка при смене архетипа: error', error);
                }
            },
            async changeOptions(options) {
                try {
                    const response = await api.patch("background/" + useCharacterStore().get_character_id + "/background-options/", options);
                    const newSelectedOption = response.data;
                    const featureToUpdate = this.background.features.find(
                        (feature) => feature.id === newSelectedOption.feature
                    );
                    featureToUpdate.selected_options = newSelectedOption;
                } catch (error) {
                    console.error('Ошибка при смене опций: error', error);
                }
            },
            async change(origin) {
                try {
                    const response = await api.patch("background/" + useCharacterStore().get_character_id + "/background-origin/", origin);
                    this.background.selected_origins = response.data
                } catch (error) {
                    console.error('Ошибка при смене опций: error', error);
                }
            },

        }
    })
;