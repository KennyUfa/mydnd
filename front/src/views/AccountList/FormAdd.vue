<template>
  <form @submit.prevent>
    <input
      type="text"
      v-model="name_champion"
      placeholder="Имя персонажа"
    />
    <div class="btn-group">
      <button type="button" class="btn btn-danger">
        {{
          champion_class.name ||
          "Выбери класс"
        }}
      </button>
      <button
        type="button"
        class="btn btn-danger dropdown-toggle dropdown-toggle-split"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      ></button>
      <ul class="dropdown-menu">
        <a
          v-if="!class_list"
          class="dropdown-item"
          href="#"
        >
          Загрузка</a
        >
        <div
          v-else
          v-for="class_info in class_list"
          :key="class_info"
        >
          <a class="dropdown-item" href="#"
             @click="change_class(class_info)">{{
              class_info.name
            }}</a>
        </div>
      </ul>
    </div>
    <div class="btn-group">
      <button type="button" class="btn btn-danger">
        {{ race.name || 'Выбери расу' }}
      </button>
      <button
        type="button"
        class="btn btn-danger dropdown-toggle dropdown-toggle-split"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      ></button>
      <ul class="dropdown-menu">
        <a
          v-if="!race_list"
          class="dropdown-item"
          href="#"
        >
          Загрузка</a
        >
        <div
          v-else
          v-for="race in race_list"
          :key="race.name"
        >
          <a
            class="dropdown-item"
            href="#"
            @click="change_race(race)"
          >{{ race.name }}</a
          >
        </div>
      </ul>
    </div>
    <div class="btn-group">
      <button type="button" class="btn btn-danger">
        {{ level }}
      </button>
      <button
        type="button"
        class="btn btn-danger dropdown-toggle dropdown-toggle-split"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      ></button>
      <ul class="dropdown-menu">
        <div v-for="n in 20" :key="n">
          <a class="dropdown-item" @click="change_level(n)" href="#">{{ n }}</a>
        </div>
      </ul>
    </div>
  </form>
  <button class="btn btn-primary" @click="createChampion">
    Cоздать нового чемпиона
  </button>


</template>

<script setup>
import {computed, onMounted, ref} from 'vue';
import {useCreateCharacter} from '@/stores/create.character.js';

const create_character = useCreateCharacter();

const name_champion = ref('');
const champion_class = ref('');
const race = ref('');
const level = ref(1);

const class_list = computed(() => create_character.class_list);
const race_list = computed(() => create_character.race_list);


const change_class = (selected) => {
  champion_class.value = selected;
}
const change_race = (selected) => {
  race.value = selected;
}

const change_level = (selected) => {
  level.value = selected;
}

const createChampion = async () => {
  const data = {
    name_champion: name_champion.value,
    champion_class: champion_class.value,
    race: race.value,
    level: level.value,
  };
  try {
    await create_character.createCharacter(data); // Используем await
    // После успешного создания можно перенаправить пользователя или очистить форму
  } catch (error) {
    console.error('Ошибка создания:', error);
  }
};
onMounted(() => {
  create_character.fetchClassList();
  create_character.fetchRaceList();
});

</script>

<style scoped></style>
