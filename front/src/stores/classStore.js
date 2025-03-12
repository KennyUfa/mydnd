import {defineStore} from "pinia";
import {useCharacterStore} from "@/stores/characterStore.js";
import api from "@/services/api.js";

export const useClassInformationStore = defineStore("classInformation", {
    state: () => ({
        class_info: null, // Здесь будет храниться ссылка на character.class_info
        archetype: null,
        archetype_list: [],
    }),
    actions: {
        setClassInfo(data) {
            this.class_info = data; // Устанавливаем ссылку на данные
        },
        setArchetype(data) {
            this.archetype = data; // Устанавливаем ссылку на данные
        },
        async updateHideOriginal(data) {
            const characterStore = useCharacterStore();
            try {
                const response = await api.patch(
                    "/dnd/characters/" + characterStore.get_character_id + "/custom-ability/hide-original/",
                    data
                );
            } catch (error) {
                console.error("Ошибка при обновлении данных updateHideOriginal:", error);
            }
        },
        async updateHideCustomAbility(ability) {
            const characterStore = useCharacterStore();
            try {
                const response = await api.patch(
                    "/dnd/characters/" + characterStore.get_character_id + "/custom-ability/hide-custom/",
                    ability
                );
            } catch (error) {
                console.error("Ошибка при обновлении данных updateHideOriginal:", error);
            }
        },
        async updateCustomDescriptionOnServer(custom_description) {
            try {
                const response = await api.patch(
                    "/dnd/character/custom-ability/update/" + custom_description.id + "/",
                    custom_description
                );
            } catch (error) {
                console.error("Ошибка при обновлении данных updateHideOriginal:", error);
            }
        },
        async loadArchetypes() {
            try {
                const response = await api.get("dnd/class-archetype-list/" + this.class_info.id + "/");
                this.archetype_list = response.data;
            } catch (error) {
                console.error('Ошибка при получении списка archetypes:', error);
            }
        },
        async changeArchetype(id) {
            const characterStore = useCharacterStore();
            try {
                const response = await api.patch("dnd/character/" + characterStore.get_character_id + "/archetype-change/", id);
                this.archetype = response.data;
            } catch (error) {
                console.error('Ошибка при смене архетипа: error', error);
            }
        },
    },
    getters: {
        allAbilities() {
            const abilitiesMap = new Map(); // Используем Map для уникальности

            // Функция для добавления способностей
            const addAbilities = (sourceName, abilities) => {
                if (abilities && Array.isArray(abilities)) {
                    abilities.forEach(ability => {
                        const uniqueKey = `${ability.name}-${sourceName}`; // Уникальный ключ
                        if (!abilitiesMap.has(uniqueKey)) {
                            abilitiesMap.set(uniqueKey, {
                                ...ability,
                                source: sourceName
                            });
                        }
                    });
                }
            };

            // Добавляем способности основного класса
            if (this.class_info && Array.isArray(this.class_info.levels)) {
                this.class_info.levels.forEach(level => {
                    if (level.abilities && Array.isArray(level.abilities)) {
                        addAbilities('class', level.abilities); // Источник: основной класс
                    }
                });
            }

            // Добавляем способности архетипа
            if (this.archetype && Array.isArray(this.archetype.levels)) {
                this.archetype.levels.forEach(level => {
                    if (level.abilities && Array.isArray(level.abilities)) {
                        addAbilities(`archetype-${this.archetype.name}`, level.abilities); // Источник: архетип
                    }
                });
            }

            // Преобразуем Map обратно в массив
            return Array.from(abilitiesMap.values());
        }
    }
});