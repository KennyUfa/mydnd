<template>
  <MainInfoView></MainInfoView>
  <saving-throw-view></saving-throw-view>
  <skills-view></skills-view>
  <div class="wrapper">
    <passive-perception></passive-perception>
    <inspiration-frame></inspiration-frame>
    <possession-bonus></possession-bonus>
    <protection-class-view></protection-class-view>
    <initiative-view></initiative-view>
    <speed-view></speed-view>
  </div>
  <hit-vue></hit-vue>
  <ability-view></ability-view>
  <div class="col">
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

<style scoped>
.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 5px;
  padding-top: 10px;
}
</style>
