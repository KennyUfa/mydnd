<template>
  <div class="card-body">
    <div class="card-header">
      Бонус Владения {{ $store.state.champion.listInfo.possession_bonus }}
    </div>
    <div class="card-info">
      <div id="skill-info">
        <button
          class="btn btn-outline-primary"
          @click="$store.state.champion.listInfo.possession_bonus++, patchP()"
          :disabled="$store.state.champion.listInfo.possession_bonus > 10"
        >
          +
        </button>
        <button
          class="btn btn-outline-primary"
          @click="$store.state.champion.listInfo.possession_bonus--, patchP()"
          :disabled="$store.state.champion.listInfo.possession_bonus < 2"
        >
          -
        </button>
      </div>
    </div>
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
