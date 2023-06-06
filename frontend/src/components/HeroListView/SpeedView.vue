<template>
  <div class="col">
    <div class="p-1 border bg-light">
      Скорость
      {{ $store.state.champion.listInfo.speed }}
      <button
        class="col"
        @click="($store.state.champion.listInfo.speed += 5), patch()"
        :disabled="$store.state.champion.listInfo.speed > 60"
      >
        +
      </button>
      <button
        class="col"
        @click="($store.state.champion.listInfo.speed -= 5), patch()"
        :disabled="$store.state.champion.listInfo.speed < 1"
      >
        -
      </button>
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

<style scoped></style>
