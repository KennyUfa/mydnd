import {defineStore} from "pinia";
import {useCharacterStore} from "@/stores/characterStore.js";
import api from "@/services/api.js";

export const useClassInformationStore = defineStore("classInformation", {
    state: () => ({
        class_info: null, // Здесь будет храниться ссылка на character.class_info
    }),
    actions: {
        setClassInfo(data) {
            this.class_info = data; // Устанавливаем ссылку на данные
        },
        async updateHideOriginal(data) {
            const characterStore = useCharacterStore();
            try {
                const response = await api.patch(
                    "/dnd/characters/" + characterStore.get_character_id + "/custom-ability/hide-original/",
                    data
                );
                // for (const level of this.class_info.levels) {
                //     // const ability = level.abilities.find(ability => ability.id === abilityId);
                //     if (ability) {
                //         // Обновляем custom_description
                //         ability.custom_description = response;
                //         break;
                //     }
                // }
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
                // for (const level of this.class_info.levels) {
                //     const ability = level.abilities.find(ability => ability.id === abilityId);
                //     if (ability) {
                //         // Обновляем custom_description
                //         ability.custom_description = response;
                //         break;
                //     }
                // }
            } catch (error) {
                console.error("Ошибка при обновлении данных updateHideOriginal:", error);
            }
        },
        async updateCustomDescriptionOnServer(custom_description) {
            try {
                const response = await api.patch(
                    "/dnd/character/custom-ability/update/"+custom_description.id+"/",
                    custom_description
                );
            } catch (error) {
                console.error("Ошибка при обновлении данных updateHideOriginal:", error);
            }
        }

    },
    getters: {
        allAbilities() {
            const abilitiesMap = new Map(); // Используем Map для уникальности
            this.class_info.levels.forEach(level => {
                level.abilities.forEach(ability => {
                    if (!abilitiesMap.has(ability.name)) {
                        abilitiesMap.set(ability.name, ability);
                    }
                });
            });
            if (this.class_info.archetypes && Array.isArray(this.class_info.archetypes)) {
                this.class_info.archetypes.forEach(archetype => {
                    if (archetype.levels && Array.isArray(archetype.levels)) {
                        archetype.levels.forEach(level => {
                            if (level.abilities && Array.isArray(level.abilities)) {
                                level.abilities.forEach(ability => {
                                    if (!abilitiesMap.has(ability.name)) {
                                        abilitiesMap.set(ability.name + archetype.name, ability);
                                    }
                                });
                            }
                        });
                    }
                });
            }
            return Array.from(abilitiesMap.values());
        },
    }
});