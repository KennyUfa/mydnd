<template>
  <div class="card-body">
    <h5 class="card-header">
      Вдохновение {{ $store.state.champion.listInfo.inspiration }}
    </h5>
    <div class="card-info">
      <div id="skill-info">
        <button
          class="btn btn-outline-primary"
          @click="$store.state.champion.listInfo.inspiration++, patch()"
          :disabled="$store.state.champion.listInfo.inspiration > 10"
        >
          +
        </button>
        <button
          class="btn btn-outline-primary"
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
