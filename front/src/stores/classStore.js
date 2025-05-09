import {defineStore} from "pinia";
import {useCharacterStore} from "@/stores/characterStore.js";
import api from "@/services/api.js";

export const useClassInformationStore = defineStore("classInformation", {
    state: () => ({
        class_info: null,
        archetype: null,
        archetype_list: [],
    }),
    actions: {
        setClassInfo(data) {
            this.class_info = data;
        },
        setArchetype(data) {
            this.archetype = data;
        },
        async updateHideOriginal(data) {
            const characterStore = useCharacterStore();
            try {
                const response = await api.patch(
                    "class/" + characterStore.get_character_id + "/custom-ability/hide-original/",
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
                    "class/" + characterStore.get_character_id + "/custom-ability/hide-custom/",
                    ability
                );
                const ab = this.allAbilities.find(ability => ability.id === response.data.ability);
                ab.custom_description.id = response.data.id;
                ab.custom_description.custom_description = response.data.custom_description;
                ab.custom_description.hide_original = response.data.hide_original;
                ab.custom_description.hide_custom = response.data.hide_custom;
            } catch (error) {
                console.error("Ошибка при обновлении данных updateHideOriginal:", error);
            }
        },
        async updateCustomDescriptionOnServer(custom_description) {
            try {
                const response = await api.patch(
                    "class/custom-ability/update/" + custom_description.id + "/",
                    custom_description
                );
            } catch (error) {
                console.error("Ошибка при обновлении данных updateHideOriginal:", error);
            }
        },
        async loadArchetypes() {
            try {
                const response = await api.get("class/class-archetype-list/" + this.class_info.id + "/");
                this.archetype_list = response.data;
                this.archetype_list.push({name: "без подкласса"})
            } catch (error) {
                console.error('Ошибка при получении списка archetypes:', error);
            }
        },
        async changeArchetype(id) {
            const characterStore = useCharacterStore();
            console.log(id);
            if (id.name === "без подкласса") {
                console.log("удаляем архетип");
                const response = await api.delete("class/" + characterStore.get_character_id + "/archetype-change/");
                this.archetype = null;
            } else {
                try {
                    const response = await api.patch("class/" + characterStore.get_character_id + "/archetype-change/", id);
                    this.archetype = response.data;
                } catch (error) {
                    console.error('Ошибка при смене архетипа: error', error);
                }
            }

        },
    },
    getters: {
        ArchAbilities() {
            const abilitiesMap = new Map(); // Используем Map для уникальности

            // Функция для добавления способностей
            const addAbilities = (sourceName, abilities, level) => {
                if (abilities && Array.isArray(abilities)) {
                    abilities.forEach(ability => {
                        const uniqueKey = `${ability.name}-${sourceName}`; // Уникальный ключ
                        if (!abilitiesMap.has(uniqueKey)) {
                            abilitiesMap.set(uniqueKey, {
                                ...ability,
                                source: sourceName,
                                isEditing: false,
                                level: level,
                            });
                        }
                    });
                }
            };


            // Добавляем способности архетипа
            if (this.archetype && Array.isArray(this.archetype.levels)) {
                this.archetype.levels.forEach(level => {
                    if (level.abilities && Array.isArray(level.abilities)) {
                        addAbilities(`${this.archetype.name}`, level.abilities, level.level); // Источник: архетип
                    }
                });
            }

            // Преобразуем Map обратно в массив
            return Array.from(abilitiesMap.values());
        },

        ClassAbilities() {
            const abilitiesMap = new Map(); // Используем Map для уникальности

            // Функция для добавления способностей
            const addAbilities = (sourceName, abilities, level) => {
                if (abilities && Array.isArray(abilities)) {
                    abilities.forEach(ability => {
                        const uniqueKey = `${ability.name}-${sourceName}`; // Уникальный ключ
                        if (!abilitiesMap.has(uniqueKey)) {
                            abilitiesMap.set(uniqueKey, {
                                ...ability,
                                source: sourceName,
                                isEditing: false,
                                level: level,
                            });
                        }
                    });
                }
            };

            // Добавляем способности основного класса
            if (this.class_info && Array.isArray(this.class_info.levels)) {
                this.class_info.levels.forEach(level => {
                    if (level.abilities && Array.isArray(level.abilities)) {
                        addAbilities(this.class_info.name, level.abilities, level.level); // Источник: основной класс
                    }
                });
            }

            // Преобразуем Map обратно в массив
            return Array.from(abilitiesMap.values());
        }
    }
});