<template>
  <div class="col">
    <button v-if="!show" v-on:click="show = !show">{{ this.show }} не
      видно
    </button>
    <button v-else v-on:click="postBackground">{{ this.show }}видно</button>

    <background-info backgroundName="черты характера"
                     v-model:backgroundValue="$store.state.champion.listInfo.background.personality_traits"
                     v-bind:show="show"
    ></background-info>
    <background-info backgroundName="ИДЕАЛЫ"
                     v-model:backgroundValue="$store.state.champion.listInfo.background.ideals"
                     v-bind:show="show"
    ></background-info>
    <background-info backgroundName="ПРИВЯЗАННОСТИ"
                     v-model:backgroundValue="$store.state.champion.listInfo.background.bonds"
                     v-bind:show="show"
    ></background-info>
    <background-info backgroundName="СЛАБОСТИ"
                     v-model:backgroundValue="$store.state.champion.listInfo.background.flaws"
                     v-bind:show="show"
    ></background-info>
  </div>
</template>

<script>
import BackgroundInfo from "../UI/BackgroundInfo.vue";

export default {
  components: {
    BackgroundInfo
  },
  name: "BackgroundView",

  data() {
    return {
      show: false,
    }
  },
  methods: {
    postBackground() {
      this.$store.dispatch("champion/postBackground");
      this.show = !this.show
    },
  }
}
</script>

<style scoped>

</style>