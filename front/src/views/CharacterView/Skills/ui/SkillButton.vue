<template>
  <div class="card-body">
    <h6 class="card-header">{{ skillName }} - {{ skillValue }}</h6>
    <div class="card-info">
      <button class="btn btn-outline-success skill-info" v-if="!show">
        {{ Math.floor((skillValue - 10) / 2) }}
      </button>
      <div id="skill-info" v-if="show">
        <button
          class="btn btn-outline-primary"
          @click="incrementValue"
          :disabled="skillValue >= 30"
        >
          +
        </button>
        <button class="btn btn-outline-success">
          {{ Math.floor((skillValue - 10) / 2) }}
        </button>
        <button
          class="btn btn-outline-primary"
          @click="decrementValue"
          :disabled="skillValue <= 1"
        >
          -
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  skillName: String,
  skillValue: Number,
  show: Boolean,
});

const emit = defineEmits(["update:skillValue"]);


// Увеличение значения навыка
const incrementValue = () => {
  const newValue = props.skillValue + 1;
  if (newValue <= 30) {
    emit("update:skillValue", newValue); // Отправляем новое значение родителю
  }
};

// Уменьшение значения навыка
const decrementValue = () => {
  const newValue = props.skillValue - 1;
  if (newValue >= 1) {
    emit("update:skillValue", newValue); // Отправляем новое значение родителю
  }
};
</script>

<style scoped></style>