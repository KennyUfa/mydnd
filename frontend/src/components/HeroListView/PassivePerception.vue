<template>
  <div class="card-body stat">
    <p class="card-text">
      пассивная мудрость
      {{ 10 + Math.floor(($store.state.champion.listInfo.wisdom - 10) / 2) }}
    </p>
  </div>
</template>

<script>
export default {
  name: "PassivePerception",
};
</script>

<style scoped></style>
