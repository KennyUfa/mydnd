<template>
  <div
      class="champion row"
      v-for="mychampion in this.$store.state.champion.mychampions"
      v-bind:key="mychampion"
  >
    <button @click="ChampionLink(mychampion.id)">
      <div class="champ">name -{{ mychampion.name_champion }}</div>
      <div class="champ">class - {{ mychampion.champion_class }}</div>
      <div class="champ">lvl - {{ mychampion.lvl }}</div>
    </button>
    <button class="btn btn-primary" @click="deleteChampion(mychampion.id)">
      Delete
    </button>
  </div>
</template>
<script>

export default {
  name: "ListChampions",
  created() {
    this.$store.dispatch("champion/getChampions");
  },
  methods: {
    deleteChampion(id) {
      this.$store.dispatch("champion/deleteChampion",{id});
    }
  }
}
</script>

<style scoped>
.champion {
  border: solid 1px black;
}
</style>