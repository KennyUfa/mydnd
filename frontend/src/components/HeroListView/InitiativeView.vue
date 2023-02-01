<template>
  <div class="col">
    <div class="p-1 border bg-light">Инициатива {{
        Math.floor(($store.state.champion.listInfo.dexterity - 10) / 2)
      }}
    </div>
  </div>
</template>

<script>
export default {
  name: "InitiativeView"
}
</script>

<style scoped>

</style>