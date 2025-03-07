<template>
  <!--  <random-window ref="RandomWindow"></random-window>-->
  <div class="col">
    <!-- Nav tabs -->
    <ul class="nav nav-tabs" role="tablist">
      <li class="nav-item" role="presentation">
        <a
          class="nav-link active"
          data-bs-toggle="tab"
          href="#main"
          role="tab"
          aria-selected="false"
        >Характеристики</a
        >
      </li>
      <!--      <li class="nav-item" role="presentation">-->
      <!--        <a-->
      <!--          class="nav-link"-->
      <!--          data-bs-toggle="tab"-->
      <!--          href="#inventory"-->
      <!--          role="tab"-->
      <!--          aria-selected="false"-->
      <!--        >Инвентарь</a-->
      <!--        >-->
      <!--      </li>-->
      <!--      <li class="nav-item" role="presentation">-->
      <!--        <a-->
      <!--          class="nav-link"-->
      <!--          data-bs-toggle="tab"-->
      <!--          href="#spells"-->
      <!--          role="tab"-->
      <!--          aria-selected="false"-->
      <!--        >Заклинания</a-->
      <!--        >-->
      <!--      </li>-->
      <!--      <li class="nav-item" role="presentation">-->
      <!--        <a-->
      <!--          class="nav-link"-->
      <!--          data-bs-toggle="tab"-->
      <!--          href="#class-information"-->
      <!--          role="tab"-->
      <!--          aria-selected="True"-->
      <!--        >Классовая информация</a-->
      <!--        >-->
      <!--      </li>-->
    </ul>
    <!-- Tab panes -->
    <div class="tab-content">
      <!--      <div class="tab-pane fade" id="inventory" role="tabpanel">-->
      <!--        <inventory-view></inventory-view>-->
      <!--      </div>-->
      <!--      <div class="tab-pane fade" id="spells" role="tabpanel">-->
      <!--        <spell-view></spell-view>-->
      <!--      </div>-->
      <div class="tab-pane fade show active" id="main" role="tabpanel">
        <MainInformation></MainInformation>
        <!--        <ability-view @callRandomWindow="callRandomWindowMethod"></ability-view>-->
        <!--        <saving-throw-view-->
        <!--          @callRandomWindow="callRandomWindowMethod"-->
        <!--        ></saving-throw-view>-->
        <!--        <skills-view></skills-view>-->
        <!--        <div class="wrapper">-->
        <!--          <div class="container">-->
        <!--            <possession-bonus></possession-bonus>-->
        <!--            <passive-perception></passive-perception>-->
        <!--            <inspiration-frame></inspiration-frame>-->
        <!--            <protection-class-view></protection-class-view>-->
        <!--            <initiative-view></initiative-view>-->
        <!--            <speed-view></speed-view>-->
        <!--          </div>-->
        <!--        </div>-->
        <!--        <hit-vue></hit-vue>-->
      </div>
    </div>
  </div>
  <!--                  <div class="tab-pane fade" id="prehistory" role="tabpanel">-->
  <!--                    <background-view></background-view>-->
  <!--                  </div>-->
  <!--  <div class="tab-pane fade" id="class-information"-->
  <!--       role="tabpanel">-->
  <!--    <class-information-view></class-information-view>-->
  <!--  </div>-->
  <!--                  <div class="tab-pane fade" id="outher" role="tabpanel">-->
  <!--                    <proficiencie-and-languages></proficiencie-and-languages>-->
  <!--                  </div>-->
  <!--    </div>-->
  <!--  </div>-->
</template>

<script setup>
import {onMounted} from "vue";
import {useCharacterStore} from "@/stores/characterStore.js";
import MainInformation
  from "@/views/CharacterView/MainInformations/MainInformation.vue";
import {useRouter} from "vue-router";

const characterStore = useCharacterStore();
const router = useRouter();


</script>
