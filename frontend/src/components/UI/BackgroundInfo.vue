<template>
  <div class="card-text">
    <h4>{{ backgroundName }}</h4>
    Описание: {{ backgroundValue }}

  </div>
</template>

<script>
import backgroundInfo from "./BackgroundInfo.vue";

export default {
  name: "BackgroundInfo",
  props: ['backgroundName', 'backgroundValue', 'show'],
  methods: {
    backgroundInfo() {
      return backgroundInfo
    }
  }
}
</script>

<style scoped>

</style>