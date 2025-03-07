<template>
  <transition-group name="list-champions">
    <div v-if="isLoading">Загрузка...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else
         class="champion row"
         v-for="champion in characterList"
         v-bind:key="champion.id"
    >
      <button @click="championLink(champion.id)">
        <div class="champ">Имя персонажа - {{ champion.name_champion }}</div>
        <div class="champ">
          Класс - {{ champion.champion_class }}
        </div>
        <div class="champ">Расса - {{ champion.race }}</div>
        <div class="champ">Уровень - {{ champion.level }}</div>
      </button>
      <button class="btn btn-primary" @click="deleteChampion(champion.id)">
        Delete
      </button>
    </div>
  </transition-group>
</template>


<script setup>
import {computed, onMounted} from "vue";
import {useCharacterList} from "@/stores/list_characters.module.js";
import {useCharacterStore} from "@/stores/characterStore.js";
import {useRouter} from 'vue-router';


// Инициализация хранилища
const characterListStore = useCharacterList();
const characterStore = useCharacterStore();

// Доступ к состоянию
const characterList = computed(() => characterListStore.characterList);
const isLoading = computed(() => characterListStore.isLoading);
const error = computed(() => characterListStore.error);
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
  console.log('Переход к персонажу с ID:', id);
  characterStore.fetchCharacter(id);
  router.push({path: '/character'}); // Перенаправляем на страницу персонажа
};

</script>

<style scoped>
.champion {
  border: solid 1px black;
}

.list-champions-item {
  display: inline-block;
  margin-right: 10px;
}

.list-champions-enter-active,
.list-champions-leave-active {
  transition: all 1s ease;
}

.list-champions-enter-from,
.list-champions-leave-to {
  opacity: 0;
  transform: translateY(30px);
}
</style>
