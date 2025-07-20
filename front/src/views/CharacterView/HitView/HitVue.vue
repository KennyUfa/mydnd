<template>
  <div
    class="bg-gradient-to-br from-gray-900 to-gray-800 p-6 rounded-xl shadow-2xl relative">
     <MaxHit/>
    <div class="text-center mb-6">
      <h2 class="text-2xl font-bold text-yellow-400 tracking-wide">
        Здоровье
      </h2>
      <p class="text-gray-400 text-sm">Управление хит-поинтами персонажа</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <!-- Хит-поинты -->
      <div class="bg-gray-800 p-4 rounded-lg border border-gray-700">
        <div class="flex items-center justify-between mb-3">
          <div class="flex items-center">
            <div class="w-3 h-3 bg-green-500 rounded-full mr-2"></div>
            <span class="text-sm text-gray-400">Текущее</span>
          </div>
          <div class="font-mono text-lg">{{ character.current_hit }}</div>
        </div>

        <div class="flex items-center justify-between mb-3">
          <div class="flex items-center">
            <div class="w-3 h-3 bg-yellow-500 rounded-full mr-2"></div>
            <span class="text-sm text-gray-400">Максимальное</span>
          </div>
          <div class="font-mono text-lg">{{ character.max_hit }}</div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <div class="w-3 h-3 bg-red-500 rounded-full mr-2"></div>
            <span class="text-sm text-gray-400">Временное</span>
          </div>
          <div class="font-mono text-lg">{{ character.temp_hit }}</div>
        </div>
      </div>

      <!-- Контролы -->
      <div class="bg-gray-800 p-4 rounded-lg border border-gray-700 flex flex-col items-center">
        <div class="mb-4 w-full max-w-xs">
          <input
            type="number"
            v-model.number="buffer_hit"
            min="0"
            max="999"
            class="w-full p-3 bg-gray-700 border-2 border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 transition-all"
            placeholder="0"
          />
        </div>

        <div class="flex space-x-3">
          <button
            @click="heal"
            class="px-5 py-2 bg-green-500 hover:bg-green-600 text-white rounded-lg transition-all transform hover:scale-105 shadow-md flex items-center space-x-2"
          >
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 13l4 4L19 7" />
            </svg>
            <span>Heal</span>
          </button>

          <button
            @click="damage"
            class="px-5 py-2 bg-red-500 hover:bg-red-600 text-white rounded-lg transition-all transform hover:scale-105 shadow-md flex items-center space-x-2"
          >
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M19 13l-7 7-7-7" />
            </svg>
            <span>Damage</span>
          </button>
        </div>
      </div>

      <!-- Максимальные ХП -->

    </div>
  </div>
</template>

<script setup>
import MaxHit from "@/views/CharacterView/HitView/MaxHit.vue";
import {computed, ref} from "vue";
import {useCharacterStore} from "@/stores/characterStore.js";

const store = useCharacterStore();
const character = computed(() => store.character);
const buffer_hit = ref(0);

function heal() {
  if (buffer_hit.value > 0) {
    store.heal(buffer_hit.value);
    buffer_hit.value = 0;
  }
}

function damage() {
  if (buffer_hit.value > 0) {
    store.damage(buffer_hit.value);
    buffer_hit.value = 0;
  }
}
</script>

<style scoped>
/* Добавляем анимацию для очищения поля ввода */
input::placeholder {
  color: #4b5563;
  transition: color 0.3s ease;
}

input:focus::placeholder {
  color: transparent;
}
</style>