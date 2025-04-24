import {defineStore} from 'pinia';
import api from '@/services/api.js';


export const useCharacterList = defineStore('characterList', {
    state: () => ({
        characterList: [], // Начальное значение — пустой массив
        isLoading: false,  // Флаг загрузки
        error: null,       // Ошибка
    }),
    actions: {
        addCharacter(character) {
            this.characterList.push(character);
        },
        async fetchCharacterList() {
            this.isLoading = true; // Начало загрузки
            try {
                const response = await api.get("character/character-list/");
                this.characterList = response.data; // Обновляем список персонажей
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
                this.error = error.message || 'Произошла ошибка';
            } finally {
                this.isLoading = false; // Завершение загрузки
            }
        },
        async deleteChampion(id) {
            try {
                await api.delete(`character/delete/${id}/`);
                this.characterList = this.characterList.filter(champion => champion.id !== id);
            } catch (error) {
                console.error('Ошибка при удалении персонажа:', error);
                this.error = error.message || 'Произошла ошибка';
            }
        },
    },

});