<template>
  <div class="card-body">
    <div class="card-header">Инициатива</div>
    <div class="card-info">
      {{ Math.floor(($store.state.champion.listInfo.dexterity - 10) / 2) }}
    </div>
  </div>
</template>

<script>
export default {
  name: "InitiativeView",
};
</script>

<style scoped></style>
