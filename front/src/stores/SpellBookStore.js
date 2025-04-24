import {defineStore} from "pinia";
import api from "@/services/api.js";
import {useCharacterStore} from "@/stores/characterStore.js";

export const useSpellBook = defineStore("spellbook", {
    state: () => ({
        my_spellbook: {},
        sortByClass: [],
        sortByArchetype: [],
        searchQuery: '',
        spells: [],
        archetype_list: [],
        spell_details: NaN,
    }),
    actions: {
        async setSpellbook(data) {
            this.my_spellbook = data;
        },
        async searchSpells() {
            try {
                const response = await api.get('/spellbook/search/', {
                    params: {
                        class_actor: this.sortByClass,
                        archetype: this.sortByArchetype,
                        // search: this.searchQuery
                    }
                });

                this.spells = response.data;
            } catch (error) {
                console.error('Ошибка при поиске заклинаний:', error);
            }
        },
        async addSpell(spell, level_slots) {

            this.my_spellbook.slot_levels[level_slots].spells.push(spell);
            const characterStore = useCharacterStore();
            const data = {
                level_slots: level_slots,
                spell: spell.id,
            }
            const response = await api.patch('/spellbook/' + characterStore.get_character_id + '/patch/', data)
        },
        async removeSpell(spell_slot, spellIndex, spell_id) {
            const characterStore = useCharacterStore();
            const data = {
                level_slots: spell_slot,
                spell: spell_id,
                spell_index: spellIndex
            }
            const response = await api.delete('/spellbook/' + characterStore.get_character_id + '/patch/', {params: data})
        },
        async patchLevelSlots(level_slots) {
            const characterStore = useCharacterStore();
            const data = {
                level_slots: level_slots,
            }
            const response = await api.patch('/spellbook/' + characterStore.get_character_id + '/slot/patch/', data)
        },
        async getArchetypeList() {
            if (this.sortByClass.length === 0) {
                this.archetype_list = [];
                return;
            } else {
                const response = await api.get('/archetypes/', {params: {class_actor: this.sortByClass}});
                this.archetype_list = response.data;
            }
        },
        async getSpellDetails(id) {
            this.spell_details = NaN;
            const response = await api.get('/spellbook/details/' + id);
            return this.spell_details = response.data;

        }
    },

});