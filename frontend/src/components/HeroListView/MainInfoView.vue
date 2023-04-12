<template>
  <div class="row align-items-center">
    <div class="player-name col-md-3" v-if="!show">
      <button
          class="btn btn-success" v-on:click="show = !show">
        <i
            class="bi bi-vector-pen">
        </i>
      </button>
      <p class="info">Имя персонажа</p>
      <p class="info" v-if="!show">
        {{ $store.state.champion.listInfo.name_champion }}
      </p>
    </div>
    <div class="player-name col-md-3" v-else>
      <button
          class="btn btn-danger" v-on:click="patchMainInfo">
        <i
            class="bi bi-vector-pen">
        </i>
      </button>
      <p class="info">Имя персонажа</p>
      <input v-model="name">
    </div>
    <div class="col-md-9">
      <div class="row">
        <div class="div col player-info">
          <p>Класс - {{ $store.state.champion.listInfo.champion_class }}</p>
        </div>

        <div class="div col player-info" v-if="!show">
          <p>
            предистория - {{ $store.state.champion.listInfo.pre_history }}
          </p>
        </div>

        <div class="div col player-info" v-else>
          <p>
            предистория - {{ $store.state.champion.listInfo.pre_history }}
          </p>
          <button type="button" @click="loadPreHistory"
                  class="btn btn-danger dropdown-toggle dropdown-toggle-split"
                  data-bs-toggle="dropdown" aria-expanded="false">
          </button>
          <ul class="dropdown-menu">
            <a v-if="!this.$store.state.champion.prehistorylist"
               class="dropdown-item"
               href="#">
              Загрузка</a>
            <div v-else
                 v-for="prehistory in this.$store.state.champion.prehistorylist">
              <a class="dropdown-item" href="#"
                 @click="changePreHistory(prehistory.pre_history_choices)">{{
                  prehistory.pre_history_choices
                }}</a>
            </div>
          </ul>
        </div>


        <div class="div col player-info">
          <p>Имя игрока - {{ $store.state.auth.user.name }}</p>
        </div>
      </div>
      <div class="row">
        <div class="col player-info">
          <p>Расса - {{ $store.state.champion.listInfo.race }}</p>
        </div>

        <div class="col player-info" v-if="!show">
          <p>
            Мировозрение - {{ $store.state.champion.listInfo.world_outlook }}
          </p>
        </div>

        <div class="div col player-info" v-else>
          <p>
            Мировозрение - {{ $store.state.champion.listInfo.world_outlook }}
          </p>
          <button type="button" @click="loadWorldOutlook"
                  class="btn btn-danger dropdown-toggle dropdown-toggle-split"
                  data-bs-toggle="dropdown" aria-expanded="false">
          </button>
          <ul class="dropdown-menu">
            <a v-if="!this.$store.state.champion.worldoutlooklist"
               class="dropdown-item"
               href="#">
              Загрузка</a>
            <div v-else
                 v-for="wlook in this.$store.state.champion.worldoutlooklist">
              <a class="dropdown-item" href="#"
                 @click="changeWorldOutlook(wlook.world_outlook)">{{
                  wlook.world_outlook
                }}</a>
            </div>
          </ul>
        </div>

        <div class="col player-info">
          <p>Опыт - {{ $store.state.champion.listInfo.experience }}</p>
        </div>
        <div class="col player-info">
          <div id="row counter">
            <div id="buttonCountNumber" class="col">
              уровень - {{ $store.state.champion.listInfo.lvl }}
            </div>
            <div v-if="show">
              <button
                  class="col"
                  @click="$store.state.champion.listInfo.lvl++"
                  :disabled="$store.state.champion.listInfo.lvl > 19"
              >
                +
              </button>
              <button
                  class="col"
                  @click="$store.state.champion.listInfo.lvl--"
                  :disabled="$store.state.champion.listInfo.lvl < 2"
              >
                -
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainInfoView",
  data() {
    return {
      show: false,
    }
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
        return this.$store.state.champion.listInfo.name_champion
      },
      set(value) {
        console.log(value)
        this.$store.commit('champion/updateName', value)
      }
    }
  }

}
</script>

<style scoped>

</style>