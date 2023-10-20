<template>
  <div class="card-body">
    <div class="card-header">
      {{ skillName }}
    </div>
    <div
      class="card-info"
      v-if="champion.listInfo.protect_char_state[skillValue] === 1"
    >
      <button
        v-if="show"
        class="ui button big toggle"
        @click="stateProtect(skillValue)"
      >
        {{ champion.listInfo.protect_char_state[skillValue] }}
      </button>
      {{ Math.floor((champion.listInfo[stat] - 10) / 2) }}
    </div>
    <div class="card-info" v-else>
      <button
        v-if="show"
        class="ui button big toggle"
        @click="stateProtect(skillValue)"
      >
        {{ champion.listInfo.protect_char_state[skillValue] }}
      </button>
      {{
        Math.floor((champion.listInfo[stat] - 10) / 2) +
        champion.listInfo.possession_bonus
      }}
    </div>
  </div>
</template>

<script>
import store from "../../store";
import { mapState } from "vuex";

export default {
  name: "ProtectState",
  props: ["skillName", "skillValue", "stat", "show"],
  computed: mapState(["champion"]),
  methods: {
    stateProtect(skill) {
      store.commit("champion/switchProtectState", skill);
    },
  },
};
</script>

<style scoped></style>
