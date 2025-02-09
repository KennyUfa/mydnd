<template>
  <form @submit.prevent>
    <input
      type="text"
      v-model="this.$store.state.list_characters.name_champion"
      placeholder="Имя персонажа"
    />

    <div class="btn-group">
      <button type="button" class="btn btn-danger">
        {{
          this.$store.state.list_characters.champion_class.name ||
          "Выбери класс"
        }}
      </button>
      <button
        type="button"
        @click="loadClassList"
        class="btn btn-danger dropdown-toggle dropdown-toggle-split"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      ></button>
      <ul class="dropdown-menu">
        <a
          v-if="!this.$store.state.list_characters.classlist"
          class="dropdown-item"
          href="#"
        >
          Загрузка</a
        >
        <div
          v-else
          v-for="classHero in this.$store.state.list_characters.classlist"
          :key="classHero"
        >
          <a class="dropdown-item" href="#"
             @click="changeClass(classHero)">{{
              classHero.name
            }}</a>
        </div>
      </ul>
    </div>

    <div class="btn-group">
      <button type="button" class="btn btn-danger">
        {{ this.$store.state.list_characters.race.name || 'Выбери расу' }}
      </button>
      <button
        type="button"
        @click="loadRaceList"
        class="btn btn-danger dropdown-toggle dropdown-toggle-split"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      ></button>
      <ul class="dropdown-menu">
        <a
          v-if="!this.$store.state.list_characters.racelist"
          class="dropdown-item"
          href="#"
        >
          Загрузка</a
        >
        <div
          v-else
          v-for="classHero in this.$store.state.list_characters.racelist"
          :key="classHero"
        >
          <a
            class="dropdown-item"
            href="#"
            @click="changeRace(classHero)"
          >{{ classHero.name }}</a
          >
        </div>
      </ul>
    </div>

    <div class="btn-group">
      <button type="button" class="btn btn-danger">
        {{ this.$store.state.list_characters.lvl }}
      </button>
      <button
        type="button"
        class="btn btn-danger dropdown-toggle dropdown-toggle-split"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      ></button>
      <ul class="dropdown-menu">
        <div v-for="n in 20" :key="n">
          <a class="dropdown-item" @click="changeLvl(n)" href="#">{{ n }}</a>
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
      this.$store.dispatch("list_characters/createChampion");
    },
    loadClassList() {
      this.$store.dispatch("list_characters/loadClassList");
    },
    loadRaceList() {
      this.$store.dispatch("list_characters/loadRaceList");
    },
    changeClass(selected) {
      this.$store.dispatch("list_characters/changeClass", selected);
    },
    changeRace(selected) {
      this.$store.dispatch("list_characters/changeRace", selected);
    },
    changeLvl(selected) {
      this.$store.dispatch("list_characters/changeLvl", selected);
    },
  },
};
</script>

<style scoped></style>
