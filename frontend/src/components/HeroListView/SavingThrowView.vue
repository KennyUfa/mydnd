<template>
  <button v-if="!show" v-on:click="show = !show">изменить</button>
  <button v-if="show" v-on:click="patchProtectSkills">применить</button>
  <div class="card-body">
    <div class="card-header">Спасброски</div>
    <div class="wrapper">
      <protect-state
        skillName="Сила"
        stat="strength"
        skillValue="protect_state_strength"
        v-bind:show="show"
      ></protect-state>
      <protect-state
        skillName="Ловкость"
        stat="dexterity"
        skillValue="protect_state_dexterity"
        v-bind:show="show"
      ></protect-state>
      <protect-state
        skillName="Телосложение"
        stat="constitution"
        skillValue="protect_state_constitution"
        v-bind:show="show"
      ></protect-state>
      <protect-state
        skillName="Интеллект"
        stat="intelligence"
        skillValue="protect_state_intelligence"
        v-bind:show="show"
      ></protect-state>
      <protect-state
        skillName="Мудрость"
        stat="wisdom"
        skillValue="protect_state_wisdom"
        v-bind:show="show"
      ></protect-state>
      <protect-state
        skillName="Харизма"
        stat="charisma"
        skillValue="protect_state_charisma"
        v-bind:show="show"
      ></protect-state>
    </div>
  </div>
</template>

<script>
import ProtectState from "../UI/ProtectState.vue";

export default {
  components: { ProtectState },
  data() {
    return {
      show: false,
    };
  },
  name: "SavingThrowView",
  methods: {
    patchProtectSkills() {
      this.$store.dispatch("champion/patchProtectSkills");
      this.show = !this.show;
    },
  },
};
</script>

<style scoped>
.card-body {
  margin-top: 5px;
}
.wrapper {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 5px;
}
@media (max-width: 720px) {
  .wrapper {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>
