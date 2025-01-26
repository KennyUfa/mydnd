<template>
  <div class="container">
    <button v-if="!show" v-on:click="show = !show">изменить</button>
    <button v-if="show" v-on:click="patchProtectSkills">применить</button>
    <div>Навыки</div>
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 ">
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Атлетика"
        stat="strength"
        skillValue="athletics"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Акробатика"
        stat="dexterity"
        skillValue="acrobatics"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Ловкость рук"
        stat="dexterity"
        skillValue="sleight_of_hand"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Скрытность"
        stat="dexterity"
        skillValue="stealth"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Магия"
        stat="intelligence"
        skillValue="arcana"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="История"
        stat="intelligence"
        skillValue="history"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Анализ"
        stat="intelligence"
        skillValue="investigation"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Природа"
        stat="intelligence"
        skillValue="nature"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Религия"
        stat="intelligence"
        skillValue="religion"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Уход за животными"
        stat="wisdom"
        skillValue="animal_handling"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Проницательность"
        stat="wisdom"
        skillValue="insight"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Медицина"
        stat="wisdom"
        skillValue="medicine"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Внимательность"
        stat="wisdom"
        skillValue="perception"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Выживание"
        stat="wisdom"
        skillValue="survival"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Обман"
        stat="charisma"
        skillValue="deception"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Запугивание"
        stat="charisma"
        skillValue="intimidation"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Выступление"
        stat="charisma"
        skillValue="performance"
        v-bind:show="show"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="callRandomWindow"
        skillName="Убеждение"
        stat="charisma"
        skillValue="persuasion"
        v-bind:show="show"
      ></ability-frame>
    </div>
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

    callRandomWindow(data) {
      this.$emit("callRandomWindow", data);
    },
  },
};
</script>
