<template>
  <div class="card-body" @click="random_save()">
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
    <div
      class="card-info"
      v-bind:style="{ 'background-color': '#d8c13b' }"
      v-else
    >
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
  data() {
    return {
      showToast: false,
      result: "",
    };
  },
  methods: {
    stateProtect(skill) {
      store.commit("champion/switchProtectState", skill);
    },
    random_save() {
      let params = {
        skillValue: this.skillValue,
        stat: this.stat,
      };

      this.$store
        .dispatch("getrand/getRandomProtect", params)
        .then((responseData) => {
          this.$emit("callRandomWindow", responseData);
        })
        .catch((error) => {
          // обработка ошибки при запросе
          console.error("Error fetching data:", error);
        });
    },
    async handleButtonClick() {
      try {
        this.result = 10;
        this.showToast = true;
      } catch (error) {
        console.error("Ошибка при выполнении запроса:", error);
      }
    },
  },
};
</script>

<style scoped></style>
