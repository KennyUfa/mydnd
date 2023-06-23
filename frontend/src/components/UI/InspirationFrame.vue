<template>
  <div class="col card stat">
    <h5 class="card-title">
      Вдохновение {{ $store.state.champion.listInfo.inspiration }}
    </h5>
    <div class="container">
      <div class="row justify-content-center align-items-center g-2">
        <button
          class="col"
          @click="$store.state.champion.listInfo.inspiration++, patch()"
          :disabled="$store.state.champion.listInfo.inspiration > 10"
        >
          +
        </button>
        <button
          class="col"
          @click="$store.state.champion.listInfo.inspiration--, patch()"
          :disabled="$store.state.champion.listInfo.inspiration < 1"
        >
          -
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InspirationFrame",
  data() {
    return {
      polling: null,
    };
  },
  methods: {
    patch() {
      this.destroyInterval();
      this.createTimer();
    },
    pollData() {
      this.polling = setTimeout(() => {
        this.$store.dispatch("champion/patchInspirationFrame");
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
