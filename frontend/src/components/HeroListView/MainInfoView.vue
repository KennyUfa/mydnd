<template>
  <div class="container">
    <div class="row main-info">
      <div class="col-2 stat" v-if="!show">
        <button class="btn btn-success" v-on:click="show = !show">
          <i class="bi bi-vector-pen"></i>
        </button>
        <div class="info">Имя персонажа</div>
        <div class="info" v-if="!show">
          {{ listInfo.name_champion }}
        </div>
      </div>
      <div class="col-2 pb-4 stat" v-else>
        <button class="btn btn-danger" v-on:click="patchMainInfo">
          <i class="bi bi-vector-pen"></i>
        </button>
        <div class="info">Имя персонажа</div>
        <input
          type="name"
          class="form-control"
          aria-describedby="InputName"
          v-model="name"
        />
      </div>
      <div class="col">
        <div class="row h-50">
          <div class="col stat">Класс - {{ listInfo.champion_class }}</div>
          <div class="col stat" v-if="!show">
            <div>Предистория - {{ listInfo.pre_history }}</div>
          </div>
          <div class="col stat" v-else>
            <div>
              Предистория - {{ listInfo.pre_history }}
              <button
                type="button"
                @click="loadPreHistory"
                class="btn btn-danger dropdown-toggle dropdown-toggle-split"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              ></button>
              <ul class="dropdown-menu">
                <a
                  v-if="!this.$store.state.champion.prehistorylist"
                  class="dropdown-item"
                  href="#"
                  >Загрузка</a
                >
                <div
                  v-else
                  v-for="prehistory in this.$store.state.champion
                    .prehistorylist"
                  :key="prehistory"
                >
                  <a
                    class="dropdown-item"
                    href="#"
                    @click="changePreHistory(prehistory.pre_history_choices)"
                    >{{ prehistory.pre_history_choices }}</a
                  >
                </div>
              </ul>
            </div>
          </div>
          <div class="col stat">
            <div>Имя игрока - {{ $store.state.auth.user.name }}</div>
          </div>
        </div>
        <div class="row h-50">
          <div class="col-2 stat">
            <div>Расса - {{ listInfo.race }}</div>
          </div>
          <div class="col stat" v-if="!show">
            <div>Мировозрение - {{ listInfo.world_outlook }}</div>
          </div>
          <div class="col stat" v-else>
            <div>
              Мировозрение - {{ listInfo.world_outlook }}
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
                    @click="changeWorldOutlook(wlook.world_outlook)"
                    >{{ wlook.world_outlook }}</a
                  >
                </div>
              </ul>
            </div>
          </div>
          <div class="col-2 stat">
            <div>Опыт - {{ listInfo.experience }}</div>
          </div>
          <div class="col stat">
            <div>
              <div id="buttonCountNumber">
                Уровень - {{ listInfo.lvl }}
                <div v-if="show" class="lvl_up">
                  <button
                    class="col"
                    @click="listInfo.lvl++"
                    :disabled="listInfo.lvl > 19"
                  >
                    +
                  </button>
                  <button
                    class="col"
                    @click="listInfo.lvl--"
                    :disabled="listInfo.lvl < 2"
                  >
                    -
                  </button>
                </div>
              </div>
            </div>
          </div>
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
    loadPreHistory() {
      this.$store.dispatch("champion/loadPreHistory");
    },
    changePreHistory(selected) {
      this.$store.dispatch("champion/changePreHistory", selected);
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
        console.log(value);
        this.$store.commit("champion/updateName", value);
      },
    },
    ...mapState({
      listInfo: (state) => state.champion.listInfo,
    }),
  },
};
</script>

<style scoped></style>
