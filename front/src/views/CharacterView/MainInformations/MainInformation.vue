<template>
  <div class="wrapper">
    <div class="center name-champion" v-if="!show">
      <Button class="btn btn-success" v-on:click="show = !show">
        <i class="bi bi-vector-pen"></i>
      </Button>
      <div class="">Имя персонажа</div>
      <div class="info" v-if="!show">
        {{ character.name_champion || "-" }}
      </div>
    </div>
    <div class="center name-champion" v-else>
      <Button class="btn btn-danger" v-on:click="patchMainInfo">
        <i class="bi bi-vector-pen"></i>
      </Button>
      <div class="">Имя персонажа</div>
      <input
        type="name"
        class="form-control"
        aria-describedby="InputName"
        v-model="character.name_champion "
      />
    </div>
    <div class="center">
      Класс - {{ character.champion_class?.name }}
    </div>
    <div class="center" v-if="!show">
      <div v-if="character.origin">
        Предистория - {{ character.origin }}
      </div>
      <div v-else>Предистория - не выбрана</div>
    </div>
    <div class="center" v-else>
      <div>
        <div v-if="character.origin">
          Предистория - {{ character.origin.name || "- pre" }}
        </div>
        <div v-else>Предистория - не выбрана</div>
        <Button
          type="button"
          @click="loadOrigin"
          class="btn btn-danger dropdown-toggle dropdown-toggle-split"
          data-bs-toggle="dropdown"
          aria-expanded="false"
        >Быврать</Button>
        <ul class="dropdown-menu">
          <a v-if="!origin_list" class="dropdown-item"
             href="#">
            Загрузка...
          </a>
          <div v-else v-for="origin in origin_list" :key="origin.id">
            <a
              class="dropdown-item"
              href="#"
              @click="changeOrigin(origin)"
            >
              {{ origin.name }}
            </a>
          </div>
        </ul>
      </div>
    </div>
    <div class="center">Расса - {{ character.race?.name || "race" }}</div>
    <div class="center">
      <div class="" v-if="!show">
        <div>Мировоззрение</div>
        <div class="">{{ character.world_outlook?.name || "-" }}</div>
      </div>
      <div class="" v-else>
        <div>
          <div>
            Мировозрение
            <Button
              type="button"
              @click="loadWorldOutlook"
              class="btn btn-danger dropdown-toggle dropdown-toggle-split"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >Быврать</Button>
            <ul class="dropdown-menu">
              <a
                v-if="!world_outlook_list"
                class="dropdown-item"
                href="#"
              >Загрузка</a
              >
              <div
                v-else
                v-for="wlook in world_outlook_list"
                :key="wlook"
              >
                <a
                  class="dropdown-item"
                  href="#"
                  @click="changeWorldOutlook(wlook)"
                >{{ wlook.name }}</a
                >
              </div>
            </ul>
          </div>
          <div class="">{{ character.world_outlook?.name || "-" }}</div>
        </div>
      </div>
    </div>
    <div class="center">Опыт - {{ character.experience }}</div>
    <div class="center">
      <div id="buttonCountNumber">
        Уровень - {{ character.level }}
        <div v-if="show" class="lvl_up">
          <Button
            class="btn btn-danger"
            @click="character.level++"
            :disabled="character.level > 19"
          >
            +
          </Button>
          <Button
            class="btn btn-danger"
            @click="character.level--"
            :disabled="character.level < 2"
          >
            -
          </Button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {computed, ref} from "vue";
import {useCharacterStore} from "@/stores/characterStore";
import { Button } from '@/components/ui/button';

const store = useCharacterStore();
const character = computed(() => store.character,);
const origin_list = computed(() => store.origin_list,);
const world_outlook_list = computed(() => store.world_outlook_list,);

const show = ref(false);

const patchMainInfo = () => {
  store.patchMainInfo();
  show.value = !show.value;
}

const loadOrigin = () => {
  store.fetchOriginList();
}

const loadWorldOutlook = () => {
  store.fetchWorldOutlookList();
}

const changeWorldOutlook = (selected) => {
  store.changeWorldOutlook(selected);
}
const changeOrigin = (selected) => {
  store.changeOrigin(selected);
}
</script>

<style scoped>
.center {
  display: flex;
  text-align: center;
  justify-content: center;
  align-items: center;
  border: solid 1px black;
  border-radius: 10px;
  background-color: #faf0b6;
}

.wrapper {
  display: grid;
  grid-gap: 5px;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: minmax(50px, auto);
}

.name-champion {
  display: flex;
  justify-content: space-between; /* Раздвинуть элементы по горизонтали */
  align-items: center; /* Выравнивание по вертикали */
}

.center:nth-child(1) {
  grid-column: 1 / span 3; /* Одно окошко на всю ширину */
  padding: 5px;
}

.center:nth-child(n + 2) {
  grid-column: span 1; /* По 3 окошка в ряд на второй и третий ряд */
}

.name-champion {
  display: flex;
  justify-content: space-around;
}

@media (max-width: 1024px) {
  .center {
    font-size: 13px;
  }
}

/* Медиа-запрос для мобильных устройств с шириной экрана меньше 768px */
</style>
