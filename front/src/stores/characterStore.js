import {defineStore} from 'pinia';
import api from "@/services/api.js";
import {useClassInformationStore} from "@/stores/classStore.js";
import {useRaceStore} from "@/stores/raceStore.js";
import {useBackground} from "@/stores/BackgroundStore.js";
import {useSpellBook} from "@/stores/SpellBookStore.js";

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
                const class_store = useClassInformationStore();
                const race_store = useRaceStore();
                const background = useBackground();
                const spellbook = useSpellBook();

                const response = await api.get("character/" + characterId + "/");
                this.character = response.data; // Обновляем список персонажей
                this.character_id = characterId;
                class_store.setClassInfo(response.data.champion_class)
                class_store.setArchetype(response.data.archetype)
                race_store.setRace(response.data.race)
                background.setBackground(response.data.background)
                spellbook.setSpellbook(response.data.spell_slots)

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
                const race_store = useRaceStore();
                const class_store = useClassInformationStore();
                const background = useBackground();
                const spellbook = useSpellBook();
                const response = await api.patch("dnd/character/" + this.character_id + "/", data);
                this.character = response.data;
                class_store.setClassInfo(response.data.champion_class)
                class_store.setArchetype(response.data.archetype)
                background.setBackground(response.data.background)
                race_store.setRace(response.data.race)
                spellbook.setSpellbook(response.data.spell_slots)
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async postSkills() {
            const data = {
                strength: this.character.skills.strength,
                dexterity: this.character.skills.dexterity,
                constitution: this.character.skills.constitution,
                intelligence: this.character.skills.intelligence,
                wisdom: this.character.skills.wisdom,
                charisma: this.character.skills.charisma,
                id: this.character.skills.id,
            };
            try {
                const response = await api.patch("character/" + this.character_id + "/skills/", data);
                this.character.skills = response.data;

            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }

        },
        async getRandomAbility(data) {
            try {
                const response = await api.post("dnd/random-skill/", data);
                return response.data

            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async switchAbilityState(data) {
            this.character.skill_state[data] = (this.character.skill_state[data] % 3) + 1;
        },
        async updateCharacterHit(max_hit, temp_hit) {
            try {
                const response = await api.patch("dnd/character/" + this.character_id + "/max_hit/", {
                    max_hit: max_hit,
                    temp_hit: temp_hit
                });
                this.character.hit = response.data;
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async switchProtectState(data) {
            this.character.protect_state[data] = this.character.protect_state[data] === 1 ? 2 : 1;
        },
        async patchAbilityState() {
            const data = {
                skill_state: this.character.skill_state
            }
            try {
                const response = await api.patch("character/" + this.character_id + "/skill_state/", data);
                this.character.skill_state = response.data;
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async patchProtectSkills() {
            const data = {
                protect_state: this.character.protect_state
            }
            try {
                const response = await api.patch("character/" + this.character_id + "/protect_state/", data);
                this.character.protect_state = response.data;
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async patchPossessionBonus() {
            try {
                await api.patch("dnd/character/" + this.character_id + "/possession_bonus/", {'possession_bonus': this.character.possession_bonus});
            } catch (error) {
                console.error('Ошибка patchPossessionBonus:', error);
            }

        },
        async patchInspirationFrame() {
            try {
                await api.patch("dnd/character/" + this.character_id + "/inspiration_frame/", {'inspiration': this.character.inspiration});
            } catch (error) {
                console.error('Ошибка patchInspirationFrame:', error);
            }

        },
        async patchProtectionClass() {
            try {
                await api.patch("dnd/character/" + this.character_id + "/protection_class/", {'protection_class': this.character.protection_class});
            } catch (error) {
                console.error('Ошибка patchProtectionClass:', error);
            }

        },
        async patchSpeed() {
            try {
                await api.patch("dnd/character/" + this.character_id + "/speed/", {'speed': this.character.speed});
            } catch (error) {
                console.error('Ошибка patchSpeed:', error);
            }

        },
        async heal(heal) {
            try {
                const response = await api.patch("dnd/character/" + this.character_id + "/heal/", {heal: heal});
                this.character.current_hit = response.data.current_hit;
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async damage(damage) {
            try {
                const response = await api.patch("dnd/character/" + this.character_id + "/damage/", {damage: damage});
                this.character.current_hit = response.data.current_hit;
                this.character.temp_hit = response.data.temp_hit;
            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        },
        async rollDice(d4, d6, d8, d10, d12, d20) {
            try {
                const response = await api.post("dnd/random-dice/", {
                    'd4': d4,
                    'd6': d6,
                    'd8': d8,
                    'd10': d10,
                    'd12': d12,
                    'd20': d20
                });
                return response.data

            } catch (error) {
                console.error('Ошибка при получении списка персонажей:', error);
            }
        }
    }
})
