<template>
    <div
            class="border-2 border-red-600 flex items-center justify-between rounded-xl px-2">
        <div class="">Пассивная мудрость</div>
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
