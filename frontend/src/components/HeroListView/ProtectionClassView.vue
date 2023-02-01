<template>
  <div class="col">
    <div class="p-1 border bg-light">КЗ
      {{ $store.state.champion.listInfo.protection_class }}
      <button
          class="col"
          @click="$store.state.champion.listInfo.protection_class++,patchP()"
          :disabled="$store.state.champion.listInfo.protection_class > 100"
      >
        +
      </button>
      <button
          class="col"
          @click="$store.state.champion.listInfo.protection_class--,patchP()"
          :disabled="$store.state.champion.listInfo.protection_class < 2"
      >
        -
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProtectionClassView",
  data() {
    return {
      count: 1,
      timer: 0,
      polling: null
    }
  },
  methods: {
    patchP() {
      this.destroyInterval();
      this.count += 1;
      this.createTimer();
    },
    pollData() {
      this.polling = setTimeout(() => {
        this.$store.dispatch("champion/patchProtectionClass");
      }, 2000)
    },
    destroyInterval() {
      if (this.polling) {
        clearInterval(this.polling)
      }
    },
    createTimer() {
      this.pollData()
    },
  },
}
</script>

<style scoped>

</style>