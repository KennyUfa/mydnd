<template>

  <button v-if="!show" v-on:click="show = !show">
    {{ this.show }} не видно
  </button>
  <button v-if="show" v-on:click="postSkills">{{ this.show }} видно</button>
  <div class="wrapper">
    <skill-button
      skillName="Сила"
      v-model:skill-value="champion.listInfo.strength"
      v-bind:show="show"
    ></skill-button>
    <skill-button
      skillName="Ловкость"
      v-model:skill-value="champion.listInfo.dexterity"
      v-bind:show="show"
    ></skill-button>
    <skill-button
      skillName="Телосложение"
      v-model:skill-value="champion.listInfo.constitution"
      v-bind:show="show"
    ></skill-button>
    <skill-button
      skillName="Интиллект"
      v-model:skill-value="champion.listInfo.intelligence"
      v-bind:show="show"
    ></skill-button>
    <skill-button
      skillName="Мудрость"
      v-model:skill-value="champion.listInfo.wisdom"
      v-bind:show="show"
    ></skill-button>
    <skill-button
      skillName="Харизма"
      v-model:skill-value="champion.listInfo.charisma"
      v-bind:show="show"
    ></skill-button>
  </div>
</template>

<script>
import { mapState } from "vuex";
import SkillButton from "../UI/SkillButton.vue";

export default {
  components: {
    SkillButton,
  },
  data() {
    return {
      show: false,
    };
  },
  name: "SkillsView",
  computed: mapState(["champion"]),
  methods: {
    postSkills() {
      this.$store.dispatch("champion/postSkills");
      this.show = !this.show;
    },
  },
};
</script>

<style scoped>
.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 5px;
}
</style>
