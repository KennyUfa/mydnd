<template>
  <div class="card-body">
    <h6 class="card-header">{{ skillName }} - {{ value }}</h6>
    <div class="card-info">
      <button class="btn btn-outline-success skill-info" v-if="!show">
        {{ Math.floor((value - 10) / 2) }}
      </button>
      <div id="skill-info" v-if="show">
        <button
          class="btn btn-outline-primary"
          @click="incrementValue"
          :disabled="value > 29"
        >
          +
        </button>
        <button class="btn btn-outline-success">
          {{ Math.floor((value - 10) / 2) }}
        </button>
        <button
          class="btn btn-outline-primary"
          @click="decrementValue"
          :disabled="value < 2"
        >
          -
        </button>
      </div>
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
