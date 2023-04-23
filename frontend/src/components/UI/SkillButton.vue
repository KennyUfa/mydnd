<template>
  <div class="card-body stat">
    <h5 class="card-title">{{ skillName }}</h5>
    <p class="card-text">всего {{ value }}</p>
    <p class="card-text">бонус {{ Math.floor((value - 10) / 2) }}</p>
    <div id="row counter" v-if="show">
      <button class="col" @click="incrementValue" :disabled="value > 29">
        +
      </button>
      <button class="col" @click="decrementValue" :disabled="value < 2">
        -
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SkillButton",
  props: ["skillName", "skillValue", "show"],
  data() {
    return {
      value: this.skillValue,
    };
  },
  methods: {
    incrementValue() {
      this.value++;
      this.$emit("update:skillValue", this.value);
    },
    decrementValue() {
      this.value--;
      this.$emit("update:skillValue", this.value);
    },
  },
};
</script>

<style scoped></style>

<style scoped></style>
