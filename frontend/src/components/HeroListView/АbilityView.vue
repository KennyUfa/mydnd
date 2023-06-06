<template>
  <button v-if="!show" v-on:click="show = !show">изменить</button>
  <button v-if="show" v-on:click="patchProtectSkills">применить</button>

  <ability-frame
    skillName="Атлетика"
    stat="strength"
    skillValue="athletics"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Акробатика"
    stat="dexterity"
    skillValue="acrobatics"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Ловкость рук"
    stat="dexterity"
    skillValue="sleight_of_hand"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Скрытность"
    stat="dexterity"
    skillValue="stealth"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Магия"
    stat="intelligence"
    skillValue="arcana"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="История"
    stat="intelligence"
    skillValue="history"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Анализ"
    stat="intelligence"
    skillValue="investigation"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Природа"
    stat="intelligence"
    skillValue="nature"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Религия"
    stat="intelligence"
    skillValue="religion"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Уход за животными"
    stat="wisdom"
    skillValue="animal_handling"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Проницательность"
    stat="wisdom"
    skillValue="insight"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Медицина"
    stat="wisdom"
    skillValue="medicine"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Внимательность"
    stat="wisdom"
    skillValue="perception"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Выживание"
    stat="wisdom"
    skillValue="survival"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Обман"
    stat="charisma"
    skillValue="deception"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Запугивание"
    stat="charisma"
    skillValue="intimidation"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Выступление"
    stat="charisma"
    skillValue="performance"
    v-bind:show="show"
  ></ability-frame>
  <ability-frame
    skillName="Убеждение"
    stat="charisma"
    skillValue="persuasion"
    v-bind:show="show"
  ></ability-frame>
  <div class="">
    <h6 class="card-title" style="text-align: center">Навыки</h6>
  </div>
</template>

<script>
import AbilityFrame from "../UI/AbilityFrame.vue";

export default {
  data() {
    return {
      show: false,
    };
  },
  components: { AbilityFrame },
  name: "AbilityView",
  methods: {
    patchProtectSkills() {
      this.$store.dispatch("champion/patchAbilitySkills");
      this.show = !this.show;
    },
  },
};
</script>

<style scoped></style>
