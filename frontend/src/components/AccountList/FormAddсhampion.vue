<template>
  <form @submit.prevent>
    <input
        type="text"
        v-model="create_champion.name_champion"
        placeholder="namechampion"
    />
    <input type="text" v-model="create_champion.lvl" placeholder="lvl"/>
    <button class="btn btn-primary" @click="createChampion">
      создать нового чемпиона
    </button>
  </form>
</template>

<script>
import api from "@/services/api";

export default {
  name: "FormAddсhampion",
  data() {
    return {
      create_champion: {
        name_champion: "",
        lvl: '',
      },
    };
  },
  methods: {
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
      this.$router.push({path: "/charlist"});
    },
  },
}
</script>

<style scoped>

</style>