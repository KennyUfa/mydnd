<template>
  <div class="card-text stat">
    <h4>{{ backgroundName }}</h4>
    <strong>Описание</strong>:
    <p v-if="!show">
      {{ backgroundValue }}
    </p>
    <textarea v-else :value="backgroundValue" @input="onUserChange"></textarea>
  </div>
</template>

<script>
export default {
  name: "BackgroundInfo",
  props: ["backgroundName", "backgroundValue", "show"],
  methods: {
    onUserChange(event) {
      this.$emit("update:backgroundValue", event.target.value);
    },
  },
};
</script>

<style scoped></style>
