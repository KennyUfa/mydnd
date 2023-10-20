<template>
  <div class="card-body">
    <div class="card-header">
      {{ skillName }}
    </div>
    <div class="card-info">
      <div v-if="champion.listInfo.skill_char_state[skillValue] === 1">
        <button
          v-if="show"
          class="ui button big toggle"
          @click="stateProtect(skillValue)"
        >
          {{ champion.listInfo.skill_char_state[skillValue] }}
        </button>
        {{ Math.floor((champion.listInfo[stat] - 10) / 2) }}
      </div>
      <div v-else-if="champion.listInfo.skill_char_state[skillValue] === 2">
        <button
          v-if="show"
          class="ui button big toggle"
          @click="stateProtect(skillValue)"
        >
          {{ champion.listInfo.skill_char_state[skillValue] }}
        </button>
        {{
          Math.floor((champion.listInfo[stat] - 10) / 2) +
          champion.listInfo.possession_bonus
        }}
      </div>

      <div v-else>
        <button
          v-if="show"
          class="ui button big toggle"
          @click="stateProtect(skillValue)"
        >
          {{ champion.listInfo.skill_char_state[skillValue] }}
        </button>
        {{
          Math.floor((champion.listInfo[stat] - 10) / 2) * 2 +
          champion.listInfo.possession_bonus
        }}
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import store from "../../store";

export default {
  name: "AbilityFrame",
  props: ["skillName", "skillValue", "stat", "show"],
  computed: mapState(["champion"]),
  methods: {
    stateProtect(skill) {
      store.commit("champion/switchAbilityState", skill);
    },
  },
};
</script>

<style scoped></style>
