<template>
  <div class="bg-white text-slate-900 border-2 border-red-600 rounded-lg p-2">
    <div class="flex flex-row justify-between" @click="random_save">
      <div class="">
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

const champion = useCharacterStore();
const skill_state = champion.character.skill_state;
const skills = champion.character.skills;

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