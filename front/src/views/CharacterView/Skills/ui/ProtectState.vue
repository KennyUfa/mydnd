<template>
    <div :class="[
            'text-slate-900 border-2 rounded-lg p-2 flex flex-row justify-between',
            protect_state[skillValue] === 1 ? 'bg-amber-100 border-amber-200'
             : 'bg-amber-200 border-amber-600'
        ]"
         @click="random_save()">
        <div class="">
            {{ skillName }}
        </div>
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
</template>

<script setup>
import {useCharacterStore} from "@/stores/characterStore.js";
import {computed} from "vue";

const champion = useCharacterStore();


const protect_state = computed(() => champion.character.protect_state);
const skills = computed(() => champion.character.skills);

const emit = defineEmits(["callRandomWindow"]);

const props = defineProps({
    skillName: String,
    skillValue: String,
    stat: String,
});


const random_save = () => {
    const data = {
        protectValueName: props.skillValue,
        statValue: props.stat,
        championId: champion.character.id,
    };
    champion.getRandomAbility(data).then((response) => {
        emit("callRandomWindow", response); // Эмитим данные наверх
    });
};

</script>

<style scoped></style>
