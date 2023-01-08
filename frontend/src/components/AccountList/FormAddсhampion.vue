<template>
  <form @submit.prevent>
    <input
        type="text"
        v-model="this.$store.state.champion.create_champion.name_champion"
        placeholder="Имя персонажа"
    />

    <div class="btn-group">
      <button type="button"
              class="btn btn-danger">
        {{ this.$store.state.champion.create_champion.champion_class }}
      </button>
      <button type="button" @click="loadClassList"
              class="btn btn-danger dropdown-toggle dropdown-toggle-split"
              data-bs-toggle="dropdown" aria-expanded="false">
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


    <div class="btn-group">
      <button type="button"
              class="btn btn-danger">
        {{ this.$store.state.champion.create_champion.race }}
      </button>
      <button type="button" @click="loadRaceList"
              class="btn btn-danger dropdown-toggle dropdown-toggle-split"
              data-bs-toggle="dropdown" aria-expanded="false">
      </button>
      <ul class="dropdown-menu">
        <a v-if="!this.$store.state.champion.racelist" class="dropdown-item"
           href="#">
          Загрузка</a>
        <div v-else v-for="classHero in this.$store.state.champion.racelist">
          <a class="dropdown-item" href="#"
             @click="changeRace(classHero.race)">{{
              classHero.race
            }}</a>
        </div>
      </ul>
    </div>

    <div class="btn-group">
      <button type="button"
              class="btn btn-danger">
        {{ this.$store.state.champion.create_champion.lvl }}
      </button>
      <button type="button"
              class="btn btn-danger dropdown-toggle dropdown-toggle-split"
              data-bs-toggle="dropdown" aria-expanded="false">
      </button>
      <ul class="dropdown-menu">
        <div v-for="n in 20" :key="n">
          <a class="dropdown-item" @click="changeLvl(n)"
             href="#">{{ n }}</a>
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
    loadRaceList() {
      this.$store.dispatch("champion/loadRaceList");
    },
    changeClass(selected) {
      this.$store.dispatch("champion/changeClass", selected);
    },
    changeRace(selected) {
      this.$store.dispatch("champion/changeRace", selected);
    },
    changeLvl(selected) {
      this.$store.dispatch("champion/changeLvl", selected);
    },
  },
};
</script>

<style scoped>
</style>