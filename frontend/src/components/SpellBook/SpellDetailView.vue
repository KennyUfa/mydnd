<template>
  <div>
    <div>{{ $store.state.spellbook.spell_detail.name }}</div>
    <div>{{ $store.state.spellbook.spell_detail.lvl }}</div>
    <div>{{ $store.state.spellbook.spell_detail.class_actor }}</div>
    <div>{{ $store.state.spellbook.spell_detail.components }}</div>
    <div>{{ $store.state.spellbook.spell_detail.distance }}</div>
    <div>{{ $store.state.spellbook.spell_detail.time_cast }}</div>
    <div>{{ $store.state.spellbook.spell_detail.timing }}</div>
    <div>{{ $store.state.spellbook.spell_detail.origin }}</div>
    <div>{{ $store.state.spellbook.spell_detail.instruction }}</div>
  </div>
</template>

<script>
export default {
  name: "SpellDetailView"
}
</script>

<style scoped>

</style>