<template>
  <form @submit.prevent>
    <input
        type="text"
        v-model="this.$store.state.champion.create_champion.name_champion"
        placeholder="Имя персонажа"
    />
    <input
        type="text"
        v-model="this.$store.state.champion.create_champion.lvl"
        placeholder="lvl"
    />
    <div class="btn-group">
      <button type="button"
              class="btn btn-danger">
        {{ this.$store.state.champion.create_champion.champion_class }}
      </button>
      <button type="button" @click="loadClassList"
              class="btn btn-danger dropdown-toggle dropdown-toggle-split"
              data-bs-toggle="dropdown" aria-expanded="false">
        <span class="visually-hidden">Переключатель выпадающего списка</span>
      </button>

      <ul class="dropdown-menu">
        <a v-if="!this.$store.state.champion.classlist" class="dropdown-item"
           href="#">
          Загрузка</a>
        <div v-else v-for="classHero in this.$store.state.champion.classlist">
          <a class="dropdown-item" href="#"
             @click="changeClass(classHero.champion_class)">{{
              classHero.champion_class
            }}</a>
        </div>

      </ul>

    </div>

  </form>
  <button class="btn btn-primary" @click="createChampion">
    создать нового чемпиона
  </button>
</template>

<script>

export default {
  name: "FormAddсhampion",
  methods: {
    createChampion() {
      this.$store.dispatch("champion/createChampion");
    },
    loadClassList() {
      this.$store.dispatch("champion/loadClassList");
    },
    changeClass(selected) {
      this.$store.dispatch("champion/changeClass",selected);
    },
  },
};
</script>

<style scoped>
</style>