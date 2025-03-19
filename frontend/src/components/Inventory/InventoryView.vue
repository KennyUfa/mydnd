<template>
  <div>
    <h2>Предметы</h2>
    <router-link to="/charlist">Лист персонажа</router-link>
    <form id="search">Search <input name="query" v-model="search" /></form>
    <div
      class="spellbook border border-primary"
      v-for="items in this.$store.state.item.itemList"
      v-bind:key="items"
    >
      <div
        class="spellbook border border-primary"
        v-for="item in items"
        v-bind:key="item"
      >
        {{ item.name }}
        {{ item.damage }}
        ( {{ item.damage_universal }} )
        <ul id="v-for-object" class="demo">
          <li v-for="value in item.properties" :key="value">
            {{ value.name }}
          </li>
        </ul>
        {{ item.type.description }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InventoryView",
  data() {
    return {
      search: "",
      polling: null,
    };
  },
  props: {
    id: {
      type: String,
      default: null,
    },
  },
  watch: {
    search() {
      this.patchSearch();
    },
  },
  methods: {
    patchSearch() {
      this.destroyInterval();
      this.createTimer();
    },
    pollData() {
      this.polling = setTimeout(() => {
        this.$store.dispatch("spellbook/getData", this.search);
      }, 2000);
    },
    destroyInterval() {
      if (this.polling) {
        clearInterval(this.polling);
      }
    },
    createTimer() {
      this.pollData();
    },
    addSpell(id) {
      this.$store.dispatch("champion/addSpell", id);
    },
    deleteSpell(id) {
      this.$store.dispatch("champion/deleteSpell", id);
    },
  },
};
</script>

<style scoped></style>
