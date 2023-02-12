<template>
  <h2>SpellBook</h2>
  <router-link to="/charlist">Лист персонажа</router-link>
  <form id="search">
    Search <input name="query" v-model="search">
  </form>
  <div
      class="spellbook border border-primary"
      v-for="spell in this.$store.state.spellbook.spellList"
      v-bind:key="spell"
  >
    <router-link :to="'/spellbook/' + spell.id">
      <div class="champ">
        {{ spell.name }}
        {{ spell.lvl }}
        {{ spell.class_actor }}
      </div>
    </router-link>
    <button type="button" class="btn btn-success" @click="addSpell(spell.id)">+
    </button>
    {{this.$store.state.champion.listInfo.spells_id}}
    {{spell.id}}
    <button
        v-if="this.$store.state.champion.listInfo.spells_id.includes(spell.id)"
            type="button"
            class="btn btn-danger"
            @click="deleteSpell(spell.id)">-
    </button>
  </div>
</template>

<script>
export default {
  name: "SpellBookView",
  data() {
    return {
      search: '',
      polling: null
    }
  },
  props: {
    id: {
      type: String,
      default: null,
    },
  },
  watch: {
    search() {
      this.patchSearch()
    }
  },
  methods: {
    patchSearch() {
      this.destroyInterval();
      this.createTimer();
    },
    pollData() {
      this.polling = setTimeout(() => {
        this.$store.dispatch("spellbook/getData", this.search);
      }, 2000)
    },
    destroyInterval() {
      if (this.polling) {
        clearInterval(this.polling)
      }
    },
    createTimer() {
      this.pollData()
    },
    addSpell(id) {
      this.$store.dispatch("champion/addSpell", id);
    },
    deleteSpell(id) {
      this.$store.dispatch("champion/deleteSpell", id);
    }
  }
}
</script>

<style scoped>

</style>