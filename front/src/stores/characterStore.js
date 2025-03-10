import {defineStore} from 'pinia';
import api from "@/services/api.js";
import {useClassInformationStore} from "@/stores/classStore.js";

export const useCharacterStore = defineStore('character', {
    state: () => {
        return {
            isLoading: false,
            character_id: null,
            character: {},
            origin_list: [],
            world_outlook_list: [],
        };
    },
    getters: {
        get_character_id(state) {
            return state.character_id
        },
    },
    actions: {
        async fetchCharacter(characterId) {
            this.isLoading = true; // Начало загрузки
            try {
                console.log("fetch character")
                const class_store = useClassInformationStore();
                const response = await api.get("dnd/character/" + characterId + "/");
                this.character = response.data; // Обновляем список персонажей
                this.character_id = characterId;
                class_store.setClassInfo(response.data.champion_class)
                localStorage.setItem("champion_id", characterId);
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
                this.error = error.message || 'Произошла ошибка';
            } finally {
                this.isLoading = false; // Завершение загрузки
            }
        },
        async fetchOriginList() {
            try {
                const response = await api.get("dnd/origin-list/");
                this.origin_list = response.data; // Обновляем список персонажей
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async changeOrigin(data) {
            try {
                const response = await api.patch("dnd/character/" + this.character_id + "/origin/", data);
                this.character.origin = response.data;
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async fetchWorldOutlookList() {
            try {
                const response = await api.get("dnd/world-outlook-list/");
                this.world_outlook_list = response.data; // Обновляем список персонажей
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async changeWorldOutlook(data) {
            try {
                const response = await api.patch("dnd/character/" + this.character_id + "/world-outlook/", data);
                this.character.world_outlook = response.data;
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async patchMainInfo() {
            const data = {
                name_champion: this.character.name_champion,
                level: this.character.level,
            }
            try {
                const class_store = useClassInformationStore();
                const response = await api.patch("dnd/character/" + this.character_id + "/", data);
                this.character = response.data;
                class_store.setClassInfo(response.data.champion_class)
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
    },
})
