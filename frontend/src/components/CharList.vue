<template>
  <random-window ref="RandomWindow"></random-window>
  <div class="col">
    <!-- Nav tabs -->
    <ul class="nav nav-tabs" role="tablist">
      <li class="nav-item" role="presentation">
        <a
          class="nav-link"
          data-bs-toggle="tab"
          href="#stats"
          role="tab"
          aria-selected="false"
        >Характеристики</a
        >
      </li>
      <li class="nav-item" role="presentation">
        <a
          class="nav-link"
          data-bs-toggle="tab"
          href="#inventory"
          role="tab"
          aria-selected="false"
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
          class="nav-link active"
          data-bs-toggle="tab"
          href="#class-information"
          role="tab"
          aria-selected="True"
        >Классовая информация</a
        >
      </li>
    </ul>
    <!-- Tab panes -->
    <div class="tab-content">
      <div class="tab-pane fade" id="inventory" role="tabpanel">
        <inventory-view></inventory-view>
      </div>
      <div class="tab-pane fade" id="spells" role="tabpanel">
        <spell-view></spell-view>
      </div>
      <div class="tab-pane fade" id="stats" role="tabpanel">
        <MainInfoView></MainInfoView>
        <ability-view @callRandomWindow="callRandomWindowMethod"></ability-view>
        <saving-throw-view
          @callRandomWindow="callRandomWindowMethod"
        ></saving-throw-view>
        <skills-view></skills-view>
        <div class="wrapper">
          <div class="container">
            <possession-bonus></possession-bonus>
            <passive-perception></passive-perception>
            <inspiration-frame></inspiration-frame>
            <protection-class-view></protection-class-view>
            <initiative-view></initiative-view>
            <speed-view></speed-view>
          </div>
        </div>
        <hit-vue></hit-vue>
      </div>
      <!--            <div class="tab-pane fade" id="prehistory" role="tabpanel">-->
      <!--              <background-view></background-view>-->
      <!--            </div>-->
      <div class="tab-pane fade show active" id="class-information"
           role="tabpanel">
        <class-information-view></class-information-view>
      </div>
      <!--            <div class="tab-pane fade" id="outher" role="tabpanel">-->
      <!--              <proficiencie-and-languages></proficiencie-and-languages>-->
      <!--            </div>-->
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
import InventoryView from "./HeroListView/InventoryView.vue";
import RandomWindow from "@/components/UI/RandomWindow.vue";
import ClassInformationView from "@/components/HeroListView/ClassInformationsView.vue";

export default {
  components: {
    ClassInformationView,
    RandomWindow,
    InventoryView,
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
  methods: {
    callRandomWindowMethod(arg) {
      console.log(arg);
      this.$refs.RandomWindow.openPopup(arg);
    },
  },
};
</script>
