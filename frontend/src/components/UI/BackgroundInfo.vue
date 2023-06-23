<template>
  <div class="card-text stat col-6">
    <h4>{{ backgroundName }}</h4>
    <strong>Описание</strong>:
    <div v-if="!show">
      {{ backgroundValue }}
    </div>
    <textarea
      class="form-control autosize-textarea"
      id="exampleFormControlTextarea1"
      rows="3"
      v-else
      :value="backgroundValue"
      @input="onUserChange"
    ></textarea>
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
