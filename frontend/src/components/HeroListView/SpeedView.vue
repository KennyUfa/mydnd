<template>
  <div class="card-body">
    <div class="card-header">
      Скорость
      {{ $store.state.champion.listInfo.speed }}
    </div>
    <div class="card-info">
      <div id="skill-info">
        <button
          class="btn btn-outline-primary"
          @click="($store.state.champion.listInfo.speed += 5), patch()"
          :disabled="$store.state.champion.listInfo.speed > 60"
        >
          +
        </button>
        <button
          class="btn btn-outline-primary"
          @click="($store.state.champion.listInfo.speed -= 5), patch()"
          :disabled="$store.state.champion.listInfo.speed < 1"
        >
          -
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SpeedView",
  data() {
    return {
      count: 1,
      timer: 0,
      polling: null,
    };
  },
  methods: {
    patch() {
      this.destroyInterval();
      this.count += 1;
      this.createTimer();
    },
    pollData() {
      this.polling = setTimeout(() => {
        this.$store.dispatch("champion/patchSpeed");
      }, 2000);
    },
    destroyInterval() {
      if (this.polling) {
        clearInterval(this.polling);
      }
    },
    createTimer() {
      this.pollData();
    },
  },
};
</script>

<style scoped>
.card-body {
  border: solid 1px black;
  border-radius: 10px;
  background-color: #faf0b6;
}
</style>
