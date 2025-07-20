<script setup>
const props = defineProps({
  skillName: String,
  skillValue: Number,
});
</script>

<template>
  <div class="bg-gray-700 p-3 rounded-lg">
    <div class="text-center -mx-3">
      <div class="text-sm text-gray-400 capitalize">{{ skillName }}</div>
      <div class="text-2xl font-bold">
        {{ skillValue }}
      </div>
    </div>
    <div class="flex items-center justify-center text-lg font-medium">
      Мод: {{ Math.floor((skillValue - 10) / 2) }}
    </div>
  </div>
</template>

<style scoped></style>
