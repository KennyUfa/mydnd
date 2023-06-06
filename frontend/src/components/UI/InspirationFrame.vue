<template>
  <div class='col-3'>
    <div class="card stat p-4">
      <h5 class="card-title">
        Вдохновение {{ $store.state.champion.listInfo.inspiration }}
      </h5>
      <div class="row">
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
