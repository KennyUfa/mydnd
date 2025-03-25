<template>
    <div class="bg-white text-slate-900 border-2 border-red-600 rounded-lg p-2 mb-3">
        <div class="md-2">
            <button  v-if="protect_state[skillValue] === 1"
                    class="bg-sky-300 rounded-lg w-full flex items-center justify-center"
                    @click="switchProtectState(skillValue)">
                {{ protect_state[skillValue] }}
            </button>
            <button  v-if="protect_state[skillValue] === 2"
                    class="bg-sky-900 text-white rounded-lg w-full flex items-center justify-center"
                    @click="switchProtectState(skillValue)">
                {{ protect_state[skillValue] }}
            </button>
        </div>
        <div>
            <div class="card-header">
                {{ skillName }}
            </div>
            <div class="digital-check text-wrap text-center">
                <div v-if="protect_state[skillValue] === 1">
                    {{ Math.floor((skills[stat] - 10) / 2) }}
                </div>
                <div v-else>
                    {{
                        Math.floor((skills[stat] - 10) / 2) +
                        champion.character.possession_bonus
                    }}
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import {useCharacterStore} from "@/stores/characterStore.js";

const champion = useCharacterStore();
const protect_state = champion.character.protect_state;
const skills = champion.character.skills;


const props = defineProps({
    skillName: String,
    skillValue: String,
    stat: String,
});


const switchProtectState = (skillValue) => {
    champion.switchProtectState(skillValue)
}

</script>
<style scoped>

</style>