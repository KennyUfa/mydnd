<template>
  <div class="card">
    <div class="card-header">
      снаряжение
      <router-link to="/database" class="btn btn-primary">
        База вещей
      </router-link>
    </div>
    <router-link to="/inventary" class="btn btn-primary">
      Инвентарь
    </router-link>
  </div>
  <div class="card-body">
    <h5 class="card-title">СНАРЯЖЕНИЕ</h5>
    <button class="button button1">мм</button>
    <button class="button button1">см</button>
    <button class="button button1">зм</button>
    <button class="button button1">эм</button>
    <button class="button button1">пм</button>
  </div>
</template>

<script>
export default {
  name: "InventoryView",
};
</script>
<style scoped></style>
