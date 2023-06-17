<template>
  <div class="col card stat justify-content-center align-items-center">
    Инициатива
    {{ Math.floor(($store.state.champion.listInfo.dexterity - 10) / 2) }}
  </div>
</template>

<script>
export default {
  name: "InitiativeView",
};
</script>

<style scoped></style>
