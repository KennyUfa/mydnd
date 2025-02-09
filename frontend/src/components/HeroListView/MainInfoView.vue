<template>
  <div class="wrapper">
    <div class="center name-champion" v-if="!show">
      <button class="btn btn-success" v-on:click="show = !show">
        <i class="bi bi-vector-pen"></i>
      </button>
      <div class="">Имя персонажа</div>
      <div class="info" v-if="!show">
        {{ listInfo.name_champion }}
      </div>
    </div>
    <div class="center name-champion" v-else>
      <button class="btn btn-danger" v-on:click="patchMainInfo">
        <i class="bi bi-vector-pen"></i>
      </button>
      <div class="">Имя персонажа</div>
      <input
        type="name"
        class="form-control"
        aria-describedby="InputName"
        v-model="name"
      />
    </div>
    <div class="center">
      Класс - {{ listInfo.champion_class.name }}
    </div>
    <div class="center" v-if="!show">
      <p v-if="listInfo.origin">
        Предистория - {{ listInfo.origin.name }}
      </p>
      <p v-else>Предистория - не выбрана</p>
    </div>
    <div class="center" v-else>
      <div>
        <p v-if="listInfo.origin">
          Предистория - {{ listInfo.origin.name }}
        </p>
        <p v-else>Предистория - не выбрана</p>

        <button
          type="button"
          @click="loadOrigin"
          class="btn btn-danger dropdown-toggle dropdown-toggle-split"
          data-bs-toggle="dropdown"
          aria-expanded="false"
        ></button>
        <ul class="dropdown-menu">
          <a
            v-if="!this.$store.state.origin.originlist"
            class="dropdown-item"
            href="#"
            >Загрузка</a
          >
          <div
            v-else
            v-for="origin in this.$store.state.origin.originlist"
            :key="origin"
          >
            <a
              class="dropdown-item"
              href="#"
              @click="changeOrigin(origin)"
              >{{ origin.name }}</a
            >
          </div>
        </ul>
      </div>
    </div>
    <div class="center">Расса - {{ listInfo.race.name }}</div>
    <div class="center">
      <div class="" v-if="!show">
        <div>Мировозрение</div>
        <div class="">{{ listInfo.world_outlook }}</div>
      </div>
      <div class="" v-else>
        <div>
          <div>
            Мировозрение
            <button
              type="button"
              @click="loadWorldOutlook"
              class="btn btn-danger dropdown-toggle dropdown-toggle-split"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            ></button>
            <ul class="dropdown-menu">
              <a
                v-if="!this.$store.state.champion.worldoutlooklist"
                class="dropdown-item"
                href="#"
                >Загрузка</a
              >
              <div
                v-else
                v-for="wlook in this.$store.state.champion.worldoutlooklist"
                :key="wlook"
              >
                <a
                  class="dropdown-item"
                  href="#"
                  @click="changeWorldOutlook(wlook.name)"
                  >{{ wlook.name }}</a
                >
              </div>
            </ul>
          </div>
          <div class="">{{ listInfo.world_outlook }}</div>
        </div>
      </div>
    </div>
    <div class="center">Опыт - {{ listInfo.experience }}</div>
    <div class="center">
      <div id="buttonCountNumber">
        Уровень - {{ listInfo.lvl }}
        <div v-if="show" class="lvl_up">
          <button
            class="btn btn-danger"
            @click="listInfo.lvl++"
            :disabled="listInfo.lvl > 19"
          >
            +
          </button>
          <button
            class="btn btn-danger"
            @click="listInfo.lvl--"
            :disabled="listInfo.lvl < 2"
          >
            -
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "MainInfostat",
  data() {
    return {
      show: false,
    };
  },
  methods: {
    patchMainInfo() {
      this.$store.dispatch("champion/patchMainInfo");
      this.show = !this.show;
    },
    loadOrigin() {
      this.$store.dispatch("origin/loadOrigin");
    },
    changeOrigin(selected) {
      this.$store.dispatch("origin/changeOrigin", selected);
    },
    loadWorldOutlook() {
      this.$store.dispatch("champion/loadWorldOutlook");
    },
    changeWorldOutlook(selected) {
      this.$store.dispatch("champion/changeWorldOutlook", selected);
    },
  },
  computed: {
    name: {
      get() {
        return this.$store.state.champion.listInfo.name_champion;
      },
      set(value) {
        this.$store.commit("champion/updateName", value);
      },
    },
    ...mapState({
      listInfo: (state) => state.champion.listInfo,
      origin: (state) => state.origin.originlist
    }),
  },
};
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
