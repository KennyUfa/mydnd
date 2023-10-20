<template>
  <div class="card-body">
    <div class="card-header">Пассивная мудрость</div>
    <div class="card-info">
      {{ 10 + Math.floor(($store.state.champion.listInfo.wisdom - 10) / 2) }}
    </div>
  </div>
</template>

<script>
export default {
  name: "PassivePerception",
};
</script>

<style scoped></style>
