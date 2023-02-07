<template>
  <div class="card">
    <div class="card-header">Заклинания</div>
    <div class="card-body">
      <router-link to="/spellbook" class="btn btn-primary">Книга
        заклинаний
      </router-link>
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
      </div>

    </div>

  </div>

</template>

<script>
export default {
  name: "SpellView"
}
</script>

<style scoped>

</style>