<template>
    <div class="col card stat">
      <h5 class="card-title">
        Бонус Владения {{ $store.state.champion.listInfo.possession_bonus }}
      </h5>
      <button
        class="col"
        @click="$store.state.champion.listInfo.possession_bonus++, patchP()"
        :disabled="$store.state.champion.listInfo.possession_bonus > 10"
      >
        +
      </button>
      <button
        class="col"
        @click="$store.state.champion.listInfo.possession_bonus--, patchP()"
        :disabled="$store.state.champion.listInfo.possession_bonus < 2"
      >
        -
      </button>
    </div>
</template>
<script>
export default {
  name: "PossessionBonus",
  data() {
    return {
      polling: null,
    };
  },
  methods: {
    patchP() {
      this.destroyInterval();
      this.createTimer();
    },
    pollData() {
      this.polling = setTimeout(() => {
        this.$store.dispatch("champion/patchPossessionBonus");
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
