<template>
    <div class="bg-gray-900 p-6 border-b border-gray-700">
        <div
          class="flex flex-col md:flex-row md:justify-between md:items-center"
        >
          <div>
            <h2 class="text-3xl font-bold">{{ character.name_champion || '-' }}</h2>
            <p class="text-gray-400">
               {{ character.champion_class?.name || 'class' }} {{ character.level || 'lvl' }} уровня |
              {{ character.race?.name || 'race' }}
            </p>
          </div>
          <div class="mt-4 md:mt-0">
            <button
              class="inline-block bg-yellow-900 px-4 py-2 rounded-lg font-medium"
            >
              {{ alignment }}
            </button>
          </div>
        </div>
      </div>
  <div
    class="p-4 mx-auto"
  >

    <skills-view></skills-view>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useCharacterStore } from '@/stores/characterStore';
import SkillsView from '@/views/CharacterView/Skills/SkillsView.vue';

const character = computed(() => store.character);

const store = useCharacterStore();
const alignment= 'Законный добрый';
</script>

<style scoped>

</style>
