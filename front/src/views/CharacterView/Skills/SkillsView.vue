<template>
  <button v-if="!show" v-on:click="show = !show">
    {{ show }} не видно
  </button>
  <button v-if="show" v-on:click="postSkills">{{ show }} видно</button>
  <div class="wrapper">
    <SkillButton
      skill-name="Сила"
      v-model:skill-value="skills.strength"
      v-bind:show="show"
    ></SkillButton>
    <SkillButton
      skill-name="Ловкость"
      v-model:skill-value="skills.dexterity"
      v-bind:show="show"
    ></SkillButton>
    <SkillButton
      skill-name="Телосложение"
      v-model:skill-value="skills.constitution"
      v-bind:show="show"
    ></SkillButton>
    <SkillButton
      skill-name="Интиллект"
      v-model:skill-value="skills.intelligence"
      v-bind:show="show"
    ></SkillButton>
    <SkillButton
      skill-name="Мудрость"
      v-model:skill-value="skills.wisdom"
      v-bind:show="show"
    ></SkillButton>
    <SkillButton
      skill-name="Харизма"
      v-model:skill-value="skills.charisma"
      v-bind:show="show"
    ></SkillButton>
  </div>
</template>

<script setup>
import {ref} from "vue";
import {useCharacterStore} from "@/stores/characterStore";
import SkillButton from "@/views/CharacterView/Skills/ui/SkillButton.vue";

const champion = useCharacterStore();
const skills = champion.character.skills
const show = ref(false);

const postSkills = async () => {
  await champion.postSkills();
  show.value = !show.value;
}


</script>

<style scoped>
.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 5px;
}
</style>
