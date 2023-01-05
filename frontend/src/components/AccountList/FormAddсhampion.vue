<template>
  <form @submit.prevent>
    <input
      type="text"
      v-model="this.$store.state.champion.create_champion.name_champion"
      placeholder="namechampion"
    />
    <input
      type="text"
      v-model="this.$store.state.champion.create_champion.lvl"
      placeholder="lvl"
    />
    <input
      type="text"
      v-model="this.$store.state.champion.create_champion.champion_class"
      placeholder="class_champion"
  />
    <button class="btn btn-primary" @click="createChampion">
      создать нового чемпиона
    </button>
  </form>
</template>

<script>

export default {
  name: "FormAddсhampion",
  methods: {
    createChampion() {
      this.$store.dispatch("champion/createChampion");
    },
  },
};
</script>

<style scoped>
</style>