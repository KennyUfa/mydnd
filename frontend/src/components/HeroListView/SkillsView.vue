<template>
  <button v-if="!show" v-on:click="show = !show">{{ this.show }} не
    видно
  </button>
  <button v-if="show" v-on:click="postSkills">{{ this.show }} видно</button>

  <div class="card">
    <skill-button skillName="Сила"
                  v-model:skillValue="champion.listInfo.strength"
                  v-bind:show="show"
    ></skill-button>
    <skill-button skillName="Ловкость"
                  v-model:skillValue="champion.listInfo.dexterity"
                  v-bind:show="show"
    ></skill-button>
    <skill-button skillName="Телосложение"
                  v-model:skillValue="champion.listInfo.constitution"
                  v-bind:show="show"
    ></skill-button>
    <skill-button skillName="Интиллект"
                  v-model:skillValue="champion.listInfo.intelligence"
                  v-bind:show="show"
    ></skill-button>
    <skill-button skillName="Мудрость"
                  v-model:skillValue="champion.listInfo.wisdom"
                  v-bind:show="show"
    ></skill-button>
    <skill-button skillName="Харизма"
                  v-model:skillValue="champion.listInfo.charisma"
                  v-bind:show="show"
    ></skill-button>

  </div>
</template>

<script>
import {mapState} from "vuex";
import SkillButton from "../UI/SkillButton.vue";

export default {
  components: {
    SkillButton
  },
  data() {
    return {
      show: false,
    }
  },
  name: "SkillsView",
  computed: mapState(['champion']),
  methods: {
    postSkills() {
      this.$store.dispatch("champion/postSkills");
      this.show = !this.show
    },
  }
}
</script>

<style scoped>
</style>