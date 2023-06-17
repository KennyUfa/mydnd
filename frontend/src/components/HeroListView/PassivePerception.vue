<template>
  <div class="col card stat justify-content-center align-items-center">
    пассивная мудрость
    {{ 10 + Math.floor(($store.state.champion.listInfo.wisdom - 10) / 2) }}
  </div>
</template>

<script>
export default {
  name: "PassivePerception",
};
</script>

<style scoped></style>
