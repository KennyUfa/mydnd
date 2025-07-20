<template>
  <TransitionGroup name="list" tag="ul">
    <div v-if="isLoading">Загрузка...</div>
    <li
      v-else
      v-if="characterList.length === 0"
      class="border-4 border-black my-1 rounded-md p-2 text-center"
    >
      <div class="font-bold leading-[0.8] italic pb-4">Нет данных</div>
    </li>
    <li
      v-for="champion in characterList"
      v-bind:key="champion.id"
      class="border-4 border-black my-1 rounded-md p-2 text-center"
    >
      <button @click="championLink(champion.id)">
        <div class="font-bold leading-[0.8] italic pb-4">
          Имя персонажа -
          <div class="inline-block uppercase">{{ champion.name_champion }}</div>
        </div>
        <div class="font-bold leading-[0.8] italic pb-2">
          Класс - {{ champion.champion_class }}
        </div>
        <div class="font-bold leading-[0.8] italic pb-2">
          Расса - {{ champion.race }}
        </div>
        <div class="font-bold leading-[0.8] italic pb-2">
          Уровень - {{ champion.level }}
        </div>
      </button>
      <Button
        variant="destructive"
        class="border-2 text-white flex justify-center px-3 w-full rounded-md"
        @click="deleteChampion(champion.id)"
      >
        Delete
      </Button>
    </li>
  </TransitionGroup>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useCharacterList } from '@/stores/list_characters.module.js';  
import { useRouter } from 'vue-router';
import { Button } from '@/components/ui/button/index.js';

// Инициализация хранилища
const characterListStore = useCharacterList();

// Доступ к состоянию
const characterList = computed(() => characterListStore.characterList);
const isLoading = computed(() => characterListStore.isLoading);
const router = useRouter();

// Загрузка данных при монтировании компонента
onMounted(() => {
  characterListStore.fetchCharacterList();
});

// Функция удаления персонажа
const deleteChampion = (id) => {
  console.log('Удаление персонажа с ID:', id);
  characterListStore.deleteChampion(id); // Вызываем действие из хранилища
};
// Функция перехода к деталям персонажа
const championLink = (id) => {
  localStorage.setItem('champion_id', id);
  router.push({ path: '/character' }); // Перенаправляем на страницу персонажа
};
</script>

<style scoped>
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>
