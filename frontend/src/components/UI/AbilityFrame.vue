<template>
    <div class="card-body d-flex justify-content-between" @click="random_save()">
      <button
        v-if="show"
        class="ui button big toggle"
        @click="stateProtect(skillValue)"
      >
        {{ champion.listInfo.skill_char_state[skillValue] }}
      </button>
      <div class="card-header">
        {{ skillName }}
      </div>
      <div class="digital-check text-wrap text-center">
        <div v-if="champion.listInfo.skill_char_state[skillValue] === 1">
          {{ Math.floor((champion.listInfo[stat] - 10) / 2) }}
        </div>
        <div v-else-if="champion.listInfo.skill_char_state[skillValue] === 2">
          {{
            Math.floor((champion.listInfo[stat] - 10) / 2) +
            champion.listInfo.possession_bonus
          }}
        </div>
        <div v-else>
          {{
            Math.floor((champion.listInfo[stat] - 10) / 2) * 2 +
            champion.listInfo.possession_bonus
          }}
        </div>
      </div>
    </div>
</template>

<script>
import {mapState} from "vuex";
import store from "../../store";

export default {
  name: "AbilityFrame",
  props: ["skillName", "skillValue", "stat", "show"],
  computed: mapState(["champion"]),
  methods: {
    stateProtect(skill) {
      store.commit("champion/switchAbilityState", skill);
    },
    random_save() {
      let params = {
        skillValue: this.skillValue,
        stat: this.stat,
      };

      this.$store
        .dispatch("getrand/getRandomAbility", params)
        .then((responseData) => {
          this.$emit("callRandomWindow", responseData);
        })
        .catch((error) => {
          // обработка ошибки при запросе
          console.error("Error fetching data:", error);
        });
    },
  },
};
</script>

<style scoped>
.digital-check{
    border: 1px solid #606b85;
    border-radius: 5px;
    cursor: pointer;
    min-width: 46px;
    padding: 4px 0 3px;
    transition: background-color .1s
}
</style>