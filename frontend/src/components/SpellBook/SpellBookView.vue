<template>
  <h2>SpellBook</h2>
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

  </div>
</template>

<script>
export default {
  name: "SpellBookView",
  props: {
    id: {
      type: String,
      default: null,
    },
  },
  methods: {
    Log(event) {
      console.log(event);
    },
    detailSpell(id) {
      console.log(id);
    },
  }
}
</script>

<style scoped>

</style>