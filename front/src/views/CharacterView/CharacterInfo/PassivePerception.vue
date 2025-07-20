<template>
    <div
            class="bg-gray-800 p-2 rounded-lg border border-gray-700 flex items-center justify-between">
        <div class="">Пассив. мудрость</div>
        <div>{{ 10 + Math.floor((character.skills.wisdom - 10) / 2) }}</div>
    </div>
</template>

<script setup>
import {useCharacterStore} from "@/stores/characterStore.js";
import {computed} from "vue";

const store = useCharacterStore();
const character = computed(() => store.character);
</script>

<style scoped></style>
