<template>
    <div
            class="bg-gray-800 p-2 rounded-lg border border-gray-700 flex items-center justify-between">
        <div>Скорость</div>
        <div>{{ character.speed }}</div>
    </div>
</template>

<script setup>
import {computed} from "vue";
import {useCharacterStore} from "@/stores/characterStore.js";

const store = useCharacterStore();
const character = computed(() => store.character);
</script>

<style scoped>
</style>
