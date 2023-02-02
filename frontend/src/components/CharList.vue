<template>
  <div class="container">
    <MainInfoView></MainInfoView>
    <div class="row">
      <div class="col-4 player-info">
        <div class="row">
          <div class="col player-info">
            <skills-view></skills-view>
          </div>
          <div class="col player-info">
            <div class="row">
              <inspiration-frame></inspiration-frame>
              <possession-bonus></possession-bonus>
            </div>
            <div class="row card stat">
              <saving-throw-view></saving-throw-view>
            </div>
            <div class="row card stat">
              <ability-view></ability-view>
            </div>
          </div>
          <div class="card">
            <passive-perception></passive-perception>
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
          <protection-class-view></protection-class-view>
          <initiative-view></initiative-view>
          <speed-view></speed-view>
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
        <spell-view></spell-view>
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
import PossessionBonus from "./UI/PossessionBonus.vue";
import InspirationFrame from "./UI/InspirationFrame.vue";
import PassivePerception from "./HeroListView/PassivePerception.vue";
import ProtectionClassView from "./HeroListView/ProtectionClassView.vue";
import InitiativeView from "./HeroListView/InitiativeView.vue";
import SpeedView from "./HeroListView/SpeedView.vue";
import SpellView from "./HeroListView/SpellView.vue";


export default {
  components: {
    InitiativeView,
    ProtectionClassView,
    PassivePerception,
    InspirationFrame,
    SkillsView,
    MainInfoView,
    SavingThrowView,
    AbilityView,
    BackgroundView,
    PossessionBonus,
    SpeedView,
    SpellView,
  },
  name: "CharList",
};
</script>

<style scoped>
</style>