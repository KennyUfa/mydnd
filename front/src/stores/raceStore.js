import {defineStore} from "pinia";
import api from "@/services/api.js";
import {useCharacterStore} from "@/stores/characterStore.js";

export const useRaceStore = defineStore("race_information", {
        state: () => ({
            race: null, // Здесь будет храниться ссылка на character.class_info
            race_list: [],
            sub_race_list: [],
        }),
        actions: {
            setRace(data) {
                this.race = data; // Устанавливаем ссылку на данные
            },
            async loadSubRace() {
                try {
                    const response = await api.get("dnd/race/sub-race-list/" + this.race.id + "/");
                    this.sub_race_list = response.data;
                } catch (error) {
                    console.error('Ошибка при получении списка archetypes:', error);
                }
            },
            async changeSubRace(id) {
                const characterStore = useCharacterStore();
                try {
                    const response = await api.patch("dnd/race/character/" + characterStore.get_character_id + "/sub-race-change/", id);
                    this.race.sub_race = response.data;
                } catch (error) {
                    console.error('Ошибка при смене архетипа: error', error);
                }
            },
        },
    })
;