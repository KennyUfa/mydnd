<template>
  <div class="container">
    <MainInfoView></MainInfoView>

      <div class="row">
        <div class="col player-info">
          <div class="row">
            <div class="col player-info">
              <skills-view></skills-view>
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
                <saving-throw-view></saving-throw-view>
              </div>
              <div class="row card stat">
                <ability-view></ability-view>
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
        <background-view></background-view>
          <div class="card-body stat">
            <h5 class="card-title">УМЕНИЯ И СПОСОБНОСТИ</h5>
            <p class="card-text">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit.
              Dolorem est iusto laboriosam nulla quidem. Alias corporis cum
              quo tempore? Adipisci enim laboriosam nihil nobis omnis?
              Deleniti earum numquam quae repellat.
            </p>
          </div>

          <div class="col"></div>
          <div class="col"></div>
          <div class="col"></div>
          <div class="col"></div>
        </div>
      </div>
  </div>
</template>

<script>
import SkillsView from "./HeroListView/SkillsView.vue";
import MainInfoView from "./HeroListView/MainInfoView.vue";
import SavingThrowView from "./HeroListView/SavingThrowView.vue";
import AbilityView from "./HeroListView/АbilityView.vue";
import BackgroundView from "./HeroListView/BackgroundView.vue";


export default {
  components: {
    SkillsView, MainInfoView, SavingThrowView, AbilityView,BackgroundView
  },
  name: "CharList",
};
</script>

<style scoped>
</style>