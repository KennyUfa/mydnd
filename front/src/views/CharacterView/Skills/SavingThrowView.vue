<template>
  <button v-if="!show" v-on:click="show = !show">изменить</button>
  <button v-if="show" v-on:click="patchProtectSkills">применить</button>
    <div class="card-header">Спасброски</div>
    <div class="grid grid-cols-6">
      <protect-state
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Сила"
        stat="strength"
        skill-value="protect_state_strength"
        v-bind:show="show"
      ></protect-state>
      <protect-state
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Ловкость"
        stat="dexterity"
        skill-value="protect_state_dexterity"
        v-bind:show="show"
      ></protect-state>
      <protect-state
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Телосложение"
        stat="constitution"
        skill-value="protect_state_constitution"
        v-bind:show="show"
      ></protect-state>
      <protect-state
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Интеллект"
        stat="intelligence"
        skill-value="protect_state_intelligence"
        v-bind:show="show"
      ></protect-state>
      <protect-state
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Мудрость"
        stat="wisdom"
        skill-value="protect_state_wisdom"
        v-bind:show="show"
      ></protect-state>
      <protect-state
        @callRandomWindow="handleCallRandomWindow"
        skill-name="Харизма"
        stat="charisma"
        skill-value="protect_state_charisma"
        v-bind:show="show"
      ></protect-state>
    </div>
</template>

<script setup>
import ProtectState from "@/views/CharacterView/Skills/ui/ProtectState.vue";
import {ref} from "vue";
import {useCharacterStore} from "@/stores/characterStore";


const emit = defineEmits(["callRandomWindow"]);
const show = ref(false);
const champion = useCharacterStore();


const patchProtectSkills = async () => {
  await champion.patchProtectSkills();
  show.value = !show.value
}

const handleCallRandomWindow = (data) => {
  emit("callRandomWindow", data);
};
</script>

<style scoped>

</style>
