<template>
  <div
    class="p-2 my-2 relative">
    <change-ability></change-ability>
    <div class="text-center text-2xl text-yellow-400 font-bold tracking-wide">
      Навыки
    </div>
    <div class="grid gap-2 grid-cols-2  md:grid-cols-3 my-4">
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Атлетика"
        stat="strength"
        skill-value="athletics"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Акробатика"
        stat="dexterity"
        skill-value="acrobatics"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Ловкость рук"
        stat="dexterity"
        skill-value="sleight_of_hand"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Скрытность"
        stat="dexterity"
        skill-value="stealth"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Магия"
        stat="intelligence"
        skill-value="arcana"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="История"
        stat="intelligence"
        skill-value="history"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Анализ"
        stat="intelligence"
        skill-value="investigation"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Природа"
        stat="intelligence"
        skill-value="nature"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Религия"
        stat="intelligence"
        skill-value="religion"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Уход за животными"
        stat="wisdom"
        skill-value="animal_handling"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Проницательность"
        stat="wisdom"
        skill-value="insight"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Медицина"
        stat="wisdom"
        skill-value="medicine"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Внимательность"
        stat="wisdom"
        skill-value="perception"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Выживание"
        stat="wisdom"
        skill-value="survival"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Обман"
        stat="charisma"
        skill-value="deception"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Запугивание"
        stat="charisma"
        skill-value="intimidation"

      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Выступление"
        stat="charisma"
        skill-value="performance"
      ></ability-frame>
      <ability-frame
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Убеждение"
        stat="charisma"
        skill-value="persuasion"
      ></ability-frame>
    </div>
  </div>
</template>

<script setup>
import AbilityFrame from "@/views/CharacterView/Skills/ui/AbilityFrame.vue";
import {useCharacterStore} from "@/stores/characterStore.js";

import ChangeAbility
  from "@/views/CharacterView/Skills/ChangeSkill/ChangeAbility.vue";

const emit = defineEmits(["callRandomWindow"]);
const champion = useCharacterStore();

const handleCallRandomWindow = (data) => {
  emit("callRandomWindow", data);
};

</script>
