<template>
  <div class="container">
    <div
      class="champion row"
      v-for="mychampion in this.mychampions"
      v-bind:key="mychampion"
    >
      <button @click="ChampionLink(mychampion.id)">
        <div class="champ">name -{{ mychampion.name_champion }}</div>
        <div class="champ">class - {{ mychampion.champion_class }}</div>
        <div class="champ">lvl - {{ mychampion.lvl }}</div>
        <button class="btn btn-primary" @click="DeleteChampion(mychampion.id)">
          Delete
        </button>
      </button>
    </div>

    <form @submit.prevent>
      <input
        type="text"
        v-model="create_champion.name_champion"
        placeholder="namechampion"
      />
      <input type="text" v-model="create_champion.lvl" placeholder="lvl" />
      <button class="btn btn-primary" @click="createChampion">
        создать нового чемпиона
      </button>
    </form>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  data() {
    return {
      mychampions: [],
      create_champion: {
        name_champion: "",
        lvl: 1,
      },
    };
  },
  created() {
    this.res = this.getCharacters();
  },
  methods: {
    async getCharacters() {
      const response = await api.get("dnd/character/");
      if (response.data) {
        return (this.mychampions = response.data);
      } else {
        console.log(response);
      }
    },
    async createChampion() {
      const response = await api.post("dnd/character/", {
        name_champion: this.create_champion.name_champion,
        lvl: this.create_champion.lvl,
      });
      if (response.data) {
        return this.mychampions.push(response.data);
      } else {
        console.log(response);
      }
    },
    async DeleteChampion(id) {
      const response = await api.delete("dnd/character/" + id + "/");
      console.log(response.data);
      this.mychampions.pop(this.mychampions.id == id);
    },
    ChampionLink(id) {
      this.$store.commit("champion/change", id);
      this.$router.push({ path: "/charlist" });
    },
  },
};
</script>

<style scoped>
.champion {
  border: solid 1px black;
}
</style>>
