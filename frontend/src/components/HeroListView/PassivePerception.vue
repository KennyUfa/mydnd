<template>
  <div class="col-2">
    <div class="card stat">
      <p>
        пассивная мудрость
        {{ 10 + Math.floor(($store.state.champion.listInfo.wisdom - 10) / 2) }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "PassivePerception",
};
</script>

<style scoped></style>
