<template>
  <div class="container">
    <div class="champion row" v-for="r in this.res" v-bind:key="r">
      <div class="champ">{{ r.name_champion }}</div>
      <div class="champ">{{ r.champion_class }}</div>
      <div class="champ">{{ r.lvl }}</div>
    </div>
    <button class="btn btn-primary" @click="createChampion">
      создать нового чемпиона
    </button>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  data() {
    return {
      champions: [{ champ: 1 }, { champ: 3 }, { champ: 2 }],
      res: [],
    };
  },
  created() {
    this.res = this.getCharacters();
  },
  methods: {
    async getCharacters() {
      const response = await api.get("dnd/character");
      if (response.data) {
        return (this.res = response.data);
      } else {
        console.log(response);
      }
    },
  },
};
</script>

<style scoped>
.champion {
  border: solid 1px black;
}
</style>>
