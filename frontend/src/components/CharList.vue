<template>
  <div class="container">
    <div class="row">
      <div class="player-name col-md-3">
        <p class="info">Имя персонажа</p>
        <input
          class="info"
          v-if="show"
          :value="name_champion"
          @input="updateName"
        />
        <p class="info" v-if="!show">
          {{ $store.state.champion.listInfo.name_champion }}
        </p>
        <div class="btn m-1 btn-outline-secondary" v-on:click="show = !show">
          <i class="bi bi-pen"></i>
        </div>
      </div>
      <div class="col-md-9">
        <div class="row">
          <div class="div col player-info p-1">
            <p>Класс - {{ $store.state.champion.listInfo.champion_class }}</p>
          </div>
          <div class="div col player-info p-1">
            <p>
              предистория - {{ $store.state.champion.listInfo.pre_history }}
            </p>
          </div>
          <div class="div col player-info p-1">
            <p>Имя игрока - {{ $store.state.auth.user.name }}</p>
          </div>
        </div>
        <div class="row">
          <div class="col player-info p-1">
            <p>Расса - {{ $store.state.champion.listInfo.race }}</p>
          </div>
          <div class="col player-info p-1">
            <p>
              Мировозрение - {{ $store.state.champion.listInfo.world_outlook }}
            </p>
          </div>
          <div class="col player-info p-1">
            <p>Опыт - {{ $store.state.champion.listInfo.experience }}</p>
          </div>
          <div class="col player-info p-1">
            <div id="row counter">
              <div id="buttonCountNumber" class="col">
                {{ $store.state.champion.listInfo.lvl }}
              </div>
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
    <div id="send-button">
      <button v-on:click="show = !show">Переключить</button>
      <transition name="fade">
        <p v-if="show">привет</p>
      </transition>
    </div>
    <div id="One" class="tabcontent">
      <div class="row">
        <div class="col player-info">
          <div class="row">
            <div class="col player-info">
              <div class="card">
                <div class="card-body stat">
                  <h5 class="card-title">Сила</h5>
                  <p class="card-text">
                    Some quick example text to build on the card title and make
                    up the bulk of the card's content.
                  </p>
                </div>
                <div class="card-body stat">
                  <h5 class="card-title">Ловкость</h5>
                  <p class="card-text">
                    Some quick example text to build on the card title and make
                    up the bulk of the card's content.
                  </p>
                </div>
                <div class="card-body stat">
                  <h5 class="card-title">Телосложение</h5>
                  <p class="card-text">
                    Some quick example text to build on the card title and make
                    up the bulk of the card's content.
                  </p>
                </div>
                <div class="card-body stat">
                  <h5 class="card-title">Интелект</h5>
                  <p class="card-text">
                    Some quick example text to build on the card title and make
                    up the bulk of the card's content.
                  </p>
                </div>
                <div class="card-body stat">
                  <h5 class="card-title">Мудрость</h5>
                  <p class="card-text">
                    Some quick example text to build on the card title and make
                    up the bulk of the card's content.
                  </p>
                </div>
                <div class="card-body stat">
                  <h5 class="card-title">Харизма</h5>
                  <p class="card-text">
                    Some quick example text to build on the card title and make
                    up the bulk of the card's content.
                  </p>
                </div>
              </div>
            </div>
            <div class="col player-info">
              <div class="row">
                <div class="card stat">
                  <h5 class="card-title">Вдохновение</h5>
                </div>
                <div class="card stat">
                  <h5 class="card-title">Бонус Владения</h5>
                </div>
              </div>
              <div class="row card stat">
                <div class="">
                  <h5 class="card-title">Сила</h5>
                </div>
                <div class="">
                  <h5 class="card-title">Ловкость</h5>
                </div>
                <div class="">
                  <h5 class="card-title">Телосложение</h5>
                </div>
                <div class="">
                  <h5 class="card-title">Интеллект</h5>
                </div>
                <div class="">
                  <h5 class="card-title">Мудрость</h5>
                </div>
                <div class="">
                  <h5 class="card-title">Харизма</h5>
                </div>
                <div class="">
                  <h6 class="card-title" style="text-align: center">
                    Спасброски
                  </h6>
                </div>
              </div>
              <div class="row card stat">
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h5 class="card-title">рыбааааааа</h5>
                </div>
                <div class="">
                  <h6 class="card-title" style="text-align: center">Навыки</h6>
                </div>
              </div>
            </div>
            <div class="card">
              <div class="card-body stat">
                <p class="card-text">пассивная мудрость</p>
              </div>
            </div>
            <div class="card">
              <div class="card-body stat">
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                  Architecto culpa dignissimos dolor dolore earum, eos excepturi
                  hic incidunt inventore ipsum iusto, natus quia recusandae
                  reprehenderit saepe similique velit vero voluptatibus!
                </p>
                <p class="card-text">ПРОЧИЕ ВЛАДЕНИЯ И ЯЗЫКИ</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col player-info">
          <div class="row gx-1">
            <div class="col">
              <div class="p-1 border bg-light">КЗ</div>
            </div>
            <div class="col">
              <div class="p-1 border bg-light">Инициатива</div>
            </div>
            <div class="col">
              <div class="p-1 border bg-light">Скорость</div>
            </div>
          </div>
          <div class="col player-info">
            <div class="card">
              <div class="card-body stat">
                <h5 class="card-title">Максимум хитов</h5>
                <h5 class="card-title">Текущие Хиты</h5>
                <h5 class="card-title">Временные Хиты</h5>
              </div>
            </div>
          </div>
          <div class="row dx-1">
            <div class="col">
              <div class="p-1 border bg-light">Кость Хитов</div>
            </div>
            <div class="col">
              <div class="p-1 border bg-light">Спасброски от смерти</div>
            </div>
          </div>
          <div class="card">
            <div class="card-header">АТАКИ</div>
            <div class="card-body">
              <h5 class="card-title">Атаки и заклинания</h5>
              <p class="card-text">
                With supporting text below as a natural lead-in to additional
                content.
              </p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
          <div class="card">
            <div class="card-header">АТАКИ</div>
            <div class="card-body">
              <h5 class="card-title">СНАРЯЖЕНИЕ</h5>
              <button class="button button1">мм</button>
              <button class="button button1">см</button>
              <button class="button button1">зм</button>
              <button class="button button1">эм</button>
              <button class="button button1">пм</button>
              <p class="card-text">
                With supporting text below as a natural lead-in to additional
                content.
              </p>
            </div>
          </div>
        </div>
        <div class="col player-info">
          <div class="col">
            <div class="card-body stat">
              <h5 class="card-title">ЧЕРТЫ ХАРАКТЕРА</h5>
              <p class="card-text">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Dolorem est iusto laboriosam nulla quidem. Alias corporis cum
                quo tempore? Adipisci enim laboriosam nihil nobis omnis?
                Deleniti earum numquam quae repellat.
              </p>
            </div>
            <div class="card-body stat">
              <h5 class="card-title">ИДЕАЛЫ</h5>
              <p class="card-text">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Dolorem est iusto laboriosam nulla quidem. Alias corporis cum
                quo tempore? Adipisci enim laboriosam nihil nobis omnis?
                Deleniti earum numquam quae repellat.
              </p>
            </div>
            <div class="card-body stat">
              <h5 class="card-title">ПРИВЯЗАННОСТИ</h5>
              <p class="card-text">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Dolorem est iusto laboriosam nulla quidem. Alias corporis cum
                quo tempore? Adipisci enim laboriosam nihil nobis omnis?
                Deleniti earum numquam quae repellat.
              </p>
            </div>
            <div class="card-body stat">
              <h5 class="card-title">СЛАБОСТИ</h5>
              <p class="card-text">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Dolorem est iusto laboriosam nulla quidem. Alias corporis cum
                quo tempore? Adipisci enim laboriosam nihil nobis omnis?
                Deleniti earum numquam quae repellat.
              </p>
            </div>
            <div class="card-body stat">
              <h5 class="card-title">УМЕНИЯ И СПОСОБНОСТИ</h5>
              <p class="card-text">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Dolorem est iusto laboriosam nulla quidem. Alias corporis cum
                quo tempore? Adipisci enim laboriosam nihil nobis omnis?
                Deleniti earum numquam quae repellat.
              </p>
            </div>
          </div>
          <div class="col"></div>
          <div class="col"></div>
          <div class="col"></div>
          <div class="col"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import store from "../store";
import { mapState } from "vuex";

export default {
  data() {
    return {
      show: false,
    };
  },
  beforeCreate() {
    if (!store.getters["auth/isAuthenticated"]) {
      return this.$router.push({ path: "/" });
    }
    this.$store.dispatch("champion/getData");
  },
  name: "CharList",
  computed: {
    ...mapState({
      name_champion: (state) => state.champion.listInfo.name_champion,
    }),
    currentUser() {
      return store.state.auth.status.loggedIn;
    },
  },
  mounted() {},
  methods: {
    updateName(e) {
      this.$store.commit("champion/updateName_champion", e.target.value);
    },
  },
};
</script>

<style scoped>
</style>