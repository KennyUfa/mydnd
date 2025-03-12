<template>
  <div class="card-body d-flex justify-content-between">
    <Badge
      v-if="show"
      class="ui button big toggle"
      @click="switchProtectState(skillValue)"
    >
      {{ protect_state[skillValue] }}
    </Badge>
    <div @click="random_save()">
      <div class="card-header">
        {{ skillName }}
      </div>
      <div class="digital-check text-wrap text-center">
        <div v-if="protect_state[skillValue] === 1">
          {{ Math.floor((skills[stat] - 10) / 2) }}
        </div>
        <div v-bind:style="{ 'background-color': '#d8c13b' }" v-else>
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
import {Badge} from '@/components/ui/badge'

const champion = useCharacterStore();
const protect_state = champion.character.protect_state;
const skills = champion.character.skills;

const emit = defineEmits(["callRandomWindow"]);

const props = defineProps({
  skillName: String,
  skillValue: String,
  stat: String,
  show: Boolean,
});


const switchProtectState = (skillValue) => {
  console.log(skillValue)
  champion.switchProtectState(skillValue)
}

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
