<template>
  <MainInfoView></MainInfoView>
  <skills-view></skills-view>
  <div class="container">
    <div class="row justify-content-center m-0">
      <passive-perception></passive-perception>
      <inspiration-frame></inspiration-frame>
      <possession-bonus></possession-bonus>
      <protection-class-view></protection-class-view>
      <initiative-view></initiative-view>
      <speed-view></speed-view>
    </div>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-3">
        <div class="col player-info">
          <div class="card saving-card">
            <saving-throw-view></saving-throw-view>
          </div>
          <div class="card saving-card">
            <ability-view></ability-view>
          </div>
        </div>
      </div>
      <div class="col-9">
        <hit-vue></hit-vue>
        <!-- Nav tabs -->
        <ul class="nav nav-tabs" role="tablist">
          <li class="nav-item" role="presentation">
            <a
              class="nav-link active"
              data-bs-toggle="tab"
              href="#inventory"
              role="tab"
              aria-selected="true"
              >Инвентарь</a
            >
          </li>
          <li class="nav-item" role="presentation">
            <a
              class="nav-link"
              data-bs-toggle="tab"
              href="#spells"
              role="tab"
              aria-selected="false"
              >Заклинания</a
            >
          </li>
          <li class="nav-item" role="presentation">
            <a
              class="nav-link"
              data-bs-toggle="tab"
              href="#prehistory"
              role="tab"
              aria-selected="false"
              >Предыстория</a
            >
          </li>
          <li class="nav-item" role="presentation">
            <a
              class="nav-link"
              data-bs-toggle="tab"
              href="#skills-and-abilites"
              role="tab"
              aria-selected="false"
              >Умения и способнисти</a
            >
          </li>
          <li class="nav-item" role="presentation">
            <a
              class="nav-link"
              data-bs-toggle="tab"
              href="#outher"
              role="tab"
              aria-selected="false"
              >ПРОЧИЕ ВЛАДЕНИЯ И ЯЗЫКИ</a
            >
          </li>
        </ul>
        <!-- Tab panes -->
        <div class="tab-content">
          <div class="tab-pane fade show active" id="inventory" role="tabpanel">
            <inventory-view></inventory-view>
          </div>
          <div class="tab-pane fade" id="spells" role="tabpanel">
            <spell-view></spell-view>
          </div>
          <div class="tab-pane fade" id="prehistory" role="tabpanel">
            <background-view></background-view>
          </div>
          <div class="tab-pane fade" id="skills-and-abilites" role="tabpanel">
            УМЕНИЯ И СПОСОБНОСТИ
          </div>
          <div class="tab-pane fade" id="outher" role="tabpanel">
            <proficiencie-and-languages></proficiencie-and-languages>
          </div>
        </div>
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
import HitVue from "./HeroListView/HitVue.vue";
import ProficiencieAndLanguages from "./HeroListView/ProficiencieAndLanguages.vue";
import InventoryView from "./HeroListView/InventoryView.vue";

export default {
  components: {
    InventoryView,
    ProficiencieAndLanguages,
    HitVue,
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

<style scoped></style>
