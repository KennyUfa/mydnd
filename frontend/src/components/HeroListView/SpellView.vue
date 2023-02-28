<template>
  <div class="card">
    <div class="card-header">Заклинания
      <router-link to="/spellbook" class="btn btn-primary">Книга
        заклинаний
      </router-link>
    </div>
    <div class="card-body">

      <div
          class="spellbook border border-primary"
          v-for="spell in this.$store.state.champion.listInfo.spells"
          v-bind:key="spell"
      >
        <router-link :to="'/spellbook/' + spell.id">
          <div class="champ">
            {{ spell.name }}
            {{ spell.lvl }}
            {{ spell.class_actor }}
          </div>
        </router-link>
        <button
            type="button"
            class="btn btn-danger"
            @click="deleteSpell(spell.id)">-
        </button>

      </div>

    </div>

  </div>

</template>

<script>
export default {
  name: "SpellView",
  methods: {
    deleteSpell(id) {
      this.$store.dispatch("champion/deleteSpell", id);
    }
  }
}
</script>

<style scoped>

</style>