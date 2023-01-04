<template>
  <div class="container">
    <list-champions></list-champions>
    <form-addchampion></form-addchampion>
  </div>
</template>

<script>
import ListChampions from "../components/AccountList/ListChampions.vue";
import FormAddchampion from "../components/AccountList/FormAddсhampion.vue";


export default {
  components:{
    ListChampions,FormAddchampion
  },
//   data() {
//     return {
//       create_champion: {
//         name_champion: "",
//         lvl: 1,
//       },
//     };
//   },
//
//   methods: {
//     async getCharacters() {
//       const response = await api.get("dnd/character/");
//       if (response.data) {
//         return (this.mychampions = response.data);
//       } else {
//         console.log(response);
//       }
//     },
//     async createChampion() {
//       const response = await api.post("dnd/character/", {
//         name_champion: this.create_champion.name_champion,
//         lvl: this.create_champion.lvl,
//       });
//       if (response.data) {
//         return this.mychampions.push(response.data);
//       } else {
//         console.log(response);
//       }
//     },
//     async DeleteChampion(id) {
//       const response = await api.delete("dnd/character/" + id + "/");
//       console.log(response.data);
//       this.mychampions.pop(this.mychampions.id == id);
//     },
//     ChampionLink(id) {
//       this.$store.commit("champion/change", id);
//       this.$router.push({path: "/charlist"});
//     },
//   },
};
</script>

<style scoped>
.champion {
  border: solid 1px black;
}
</style>>
