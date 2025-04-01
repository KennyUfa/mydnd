<template>
    <div class="bg-white text-slate-900 border-2 border-red-600 rounded-lg p-2 mb-3">
        <div class="mb-2">
            <button v-if="skill_state[skillValue] === 1"
                    class="bg-sky-300 rounded-lg w-full flex items-center justify-center"
                    @click="switchAbilityState(skillValue)">
                <div class="text-center">базовое умение</div>
            </button>
            <button v-if="skill_state[skillValue] === 2"
                    class="bg-sky-600 rounded-lg w-full flex items-center justify-center text-white"
                    @click="switchAbilityState(skillValue)">
                <div class="text-center">владение</div>
            </button>
            <button v-if="skill_state[skillValue] === 3 "
                    class="bg-sky-900 rounded-lg w-full flex items-center justify-center text-white"
                    @click="switchAbilityState(skillValue)">
                <div class="text-center">мастерство</div>
            </button>
        </div>


        <div class="flex flex-row justify-between">
            <div class="font-bold italic">
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
const emit = defineEmits(["callRandomWindow"]);


const skill_state = computed(() => champion.character.skill_state);
const skills = computed(() => champion.character.skills);

const props = defineProps({
    skillName: String,
    skillValue: String,
    stat: String,
});

const switchAbilityState = (skillValue) => {
    champion.switchAbilityState(skillValue)
    console.log(skill_state[skillValue])
}
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