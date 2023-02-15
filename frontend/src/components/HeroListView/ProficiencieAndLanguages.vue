<template>
  <div class="card-body stat">
    <button v-if="!show" v-on:click="show = !show">{{ this.show }} не
      видно
    </button>
    <button v-else v-on:click="postProficienciesAndLanguages">{{ this.show }}видно</button>
    <p v-if="!show">
      {{ $store.state.champion.listInfo.ProficienciesAndLanguages }}
    </p>
    <textarea v-else
              v-model="$store.state.champion.listInfo.ProficienciesAndLanguages"></textarea>
    <p class="card-text">ПРОЧИЕ ВЛАДЕНИЯ И ЯЗЫКИ</p>
  </div>
</template>

<script>
export default {
  name: "ProficiencieAndLanguages",
  data() {
    return {
      show: false,
    }
  },
  methods: {
    postProficienciesAndLanguages() {
      this.$store.dispatch("champion/postProficienciesAndLanguages");
      this.show = !this.show
    },
  }
}
</script>

<style scoped>

</style>