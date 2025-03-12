<template>
  <button v-if="!show" v-on:click="show = !show">изменить</button>
  <button v-if="show" v-on:click="patchAbilitySkills">применить
  </button>
  <div>Навыки</div>
  <div class="grid grid-cols-6">
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Атлетика"
      stat="strength"
      skill-value="athletics"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Акробатика"
      stat="dexterity"
      skill-value="acrobatics"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Ловкость рук"
      stat="dexterity"
      skill-value="sleight_of_hand"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Скрытность"
      stat="dexterity"
      skill-value="stealth"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Магия"
      stat="intelligence"
      skill-value="arcana"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="История"
      stat="intelligence"
      skill-value="history"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Анализ"
      stat="intelligence"
      skill-value="investigation"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Природа"
      stat="intelligence"
      skill-value="nature"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Религия"
      stat="intelligence"
      skill-value="religion"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Уход за животными"
      stat="wisdom"
      skill-value="animal_handling"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Проницательность"
      stat="wisdom"
      skill-value="insight"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Медицина"
      stat="wisdom"
      skill-value="medicine"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Внимательность"
      stat="wisdom"
      skill-value="perception"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Выживание"
      stat="wisdom"
      skill-value="survival"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Обман"
      stat="charisma"
      skill-value="deception"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Запугивание"
      stat="charisma"
      skill-value="intimidation"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Выступление"
      stat="charisma"
      skill-value="performance"
      v-bind:show="show"
    ></ability-frame>
    <ability-frame
      @callRandomWindow="handleCallRandomWindow"
      skill-name="Убеждение"
      stat="charisma"
      skill-value="persuasion"
      v-bind:show="show"
    ></ability-frame>
  </div>
</template>

<script setup>
import AbilityFrame from "@/views/CharacterView/Skills/ui/AbilityFrame.vue";
import {ref} from "vue";
import {useCharacterStore} from "@/stores/characterStore.js";

const emit = defineEmits(["callRandomWindow"]);
const show = ref(false);
const champion = useCharacterStore();

const patchAbilitySkills = () => {
  champion.patchAbilityState();
  show.value = !show.value;
}

const handleCallRandomWindow = (data) => {
  emit("callRandomWindow", data);
};

</script>
