<template>
  <div
      v-if="this.$store.state.champion.isLoading"
      class="champion row"
      v-for="mychampion in this.$store.state.champion.mychampions"
      v-bind:key="mychampion"
  >
    <button @click="championLink(mychampion.id)">
      <div class="champ">name -{{ mychampion.name_champion }}</div>
      <div class="champ">class - {{ mychampion.champion_class }}</div>
      <div class="champ">lvl - {{ mychampion.lvl }}</div>
    </button>
    <button class="btn btn-primary" @click="deleteChampion(mychampion.id)">
      Delete
    </button>
  </div>
  <div v-else>Идет загрузка</div>
</template>
<script>

export default {
  data() {
    return {
    }
  },

  name: "ListChampions",
  mounted() {
    this.$store.dispatch("champion/getChampions");
  },
  methods: {
    deleteChampion(id) {
      this.$store.dispatch("champion/deleteChampion", id);
    },
    championLink(id) {
      this.$store.commit("champion/change", id);
      this.$router.push({path: "/charlist"});
    },
  }
}
</script>

<style scoped>
.champion {
  border: solid 1px black;
}
</style>