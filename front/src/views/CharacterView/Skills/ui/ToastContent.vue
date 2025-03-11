<script setup>
import { defineProps } from "vue";

const props = defineProps({
  data: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <div>
    <p>Total: {{ data.total }}</p>
    <p>Skill Value: {{ data.skillValue }}</p>
    <p>Random Result: {{ data.random_result }}</p>
    <p>Possession Bonus: {{ data.possession_bonus }}</p>
  </div>
</template>