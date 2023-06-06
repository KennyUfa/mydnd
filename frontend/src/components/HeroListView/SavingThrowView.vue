<template>
  <button v-if="!show" v-on:click="show = !show">изменить</button>
  <button v-if="show" v-on:click="patchProtectSkills">применить</button>

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
  <div class="">
    <h6 class="card-title" style="text-align: center">Спасброски</h6>
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

<style scoped></style>
