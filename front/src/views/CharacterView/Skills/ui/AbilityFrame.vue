<template>
    <div
            :class="[
        'bg-amber-100 border-amber-200  rounded-lg p-2 text-slate-900',
        skill_state[skillValue] === 3 ? 'bg-amber-400 border-amber-600' :
        skill_state[skillValue] === 2 ? 'bg-amber-800 border-amber-400' : ''
    ]">
    <div class="flex flex-row items-center justify-between"
         @click="random_save">
        <div class="font-stretch-ultra-condensed text-xl font-bold text-center">
            {{ skillName }}
        </div>
        <div class="">
            <div v-if="skill_state[skillValue] === 1">
                {{ Math.floor((skills[stat] - 10) / 2) }}
            </div>
            <div v-else-if="skill_state[skillValue] === 2">
                {{
                    Math.floor((skills[stat] - 10) / 2) +
                    champion.character.possession_bonus
                }}
            </div>
            <div v-else>
                {{
                    Math.floor((skills[stat] - 10) / 2) * 2 +
                    champion.character.possession_bonus
                }}
            </div>
        </div>
    </div>
    </div>
</template>

<script setup>
import {useCharacterStore} from "@/stores/characterStore";
import {computed} from "vue";

const champion = useCharacterStore();
const skill_state = computed(() => champion.character.skill_state);
const skills = computed(() => champion.character.skills);


const emit = defineEmits(["callRandomWindow"]);

const props = defineProps({
    skillName: String,
    skillValue: String,
    stat: String,
});

const random_save = () => {
    const data = {
        abilityValueName: props.skillValue,
        statValue: props.stat,
        championId: champion.character.id,
    };
    champion.getRandomAbility(data).then((response) => {
        emit("callRandomWindow", response); // Эмитим данные наверх
    });
};
</script>