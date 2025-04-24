import {defineStore, storeToRefs} from 'pinia';
import api from '@/services/api.js';
import {useCharacterList} from "@/stores/list_characters.module.js";


export const useCreateCharacter = defineStore('createChampion', {
    state: () => ({
        class_list: [],
        race_list: [],
        error: null,
        isLoading: false,// Ошибка
        Character: {},

    }),
    actions: {
        async fetchClassList() {
            this.isLoading = true; // Начало загрузки
            try {
                const response = await api.get("class/class-list/");
                this.class_list = response.data; // Обновляем список персонажей
                this.isLoading = false; // Завершение загрузки
            } catch (error) {
                console.error('Ошибка при получении списка классов:', error);
            }
        },
        async fetchRaceList() {
            this.isLoading = true; // Начало загрузки
            try {
                const response = await api.get("race/race-list/");
                this.race_list = response.data; // Обновляем список персонажей
                this.isLoading = false; // Завершение загрузки
            } catch (error) {
                console.error('Ошибка при получении списка классов:', error);
            }
        },
        async createCharacter(data) {

            try {
                const response = await api.post("character/create/", data);
                const characterListStore = useCharacterList();
                characterListStore.addCharacter(response.data);
                this.Character = response.data;
            } catch (error) {
                console.error('Ошибка при создании персонажа:', error);
                throw error;
            }
        },
    }
});