<template>
  <div
    class="p-2 my-2 relative">
    <change-info></change-info>
    <div
      class="text-center text-2xl font-bold text-yellow-400 tracking-wide">
      Показатели героя
    </div>
    <div class="grid grid-cols-2 gap-1 mt-4">
      <passive-perception></passive-perception>
      <initiative-view></initiative-view>
      <possession-bonus></possession-bonus>
      <inspiration-frame></inspiration-frame>
      <protection-class-view></protection-class-view>
      <speed-view></speed-view>
    </div>
  </div>

</template>
<script setup>
import PossessionBonus
  from "@/views/CharacterView/CharacterInfo/PossessionBonus.vue";
import PassivePerception
  from "@/views/CharacterView/CharacterInfo/PassivePerception.vue";
import InspirationFrame
  from "@/views/CharacterView/CharacterInfo/InspirationFrame.vue";
import ProtectionClassView
  from "@/views/CharacterView/CharacterInfo/ProtectionClassView.vue";
import InitiativeView
  from "@/views/CharacterView/CharacterInfo/InitiativeView.vue";
import SpeedView from "@/views/CharacterView/CharacterInfo/SpeedView.vue";
import ChangeInfo from "@/views/CharacterView/CharacterInfo/ChangeInfo.vue";
</script>
