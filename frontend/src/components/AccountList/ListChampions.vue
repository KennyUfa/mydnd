<template>
  <transition-group name="list-champions">
    <div
      class="champion row"
      v-for="mychampion in this.$store.state.champion.mychampions"
      v-bind:key="mychampion"
    >
      <button @click="championLink(mychampion.id)">
        <div class="champ">name -{{ mychampion.name_champion }}</div>
        <div class="champ">
          class - {{ mychampion.champion_class.champion_class }}
        </div>
        <div class="champ">lvl - {{ mychampion.lvl }}</div>
      </button>
      <button class="btn btn-primary" @click="deleteChampion(mychampion.id)">
        Delete
      </button>
    </div>
  </transition-group>
</template>
<script>
export default {
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
      this.$router.push({ path: "/charlist" });
    },
  },
};
</script>

<style scoped>
.champion {
  border: solid 1px black;
}

.list-champions-item {
  display: inline-block;
  margin-right: 10px;
}

.list-champions-enter-active,
.list-champions-leave-active {
  transition: all 1s ease;
}

.list-champions-enter-from,
.list-champions-leave-to {
  opacity: 0;
  transform: translateY(30px);
}
</style>
