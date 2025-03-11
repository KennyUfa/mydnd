<template>
  <div class="card-body d-flex justify-content-between">
    <Badge
      v-if="show"
      class="ui button big toggle"
      @click="state_skill(skillValue)"
    >
      {{ skill_state[skillValue] }}
    </Badge>
    <div  @click="random_save">
      <div class="card-header">
        {{ skillName }}
      </div>
      <div class="digital-check text-wrap text-center">
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
import {Badge} from '@/components/ui/badge'

const champion = useCharacterStore();
const skill_state = champion.character.skill_state;
const skills = champion.character.skills;

const emit = defineEmits(["callRandomWindow"]);

const props = defineProps({
  skillName: String,
  skillValue: String,
  stat: String,
  show: Boolean,
});

const state_skill = (skillValue) => {
  champion.switchAbilityState(skillValue)
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