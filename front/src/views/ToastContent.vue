<script setup>
const props = defineProps({
  data: {
    type: Object,
    required: true,
  },
});
</script>

<template>
    <strong>Итого: {{ data.total }}</strong>
    <p>Значение навыка: {{ data.skillValue }}</p>
    <p>Результат броска: {{ data.random_result }}</p>
    <p>Бонус мастерства: {{ data.possession_bonus }}</p>
</template>