<template>
    <div
            class="border-2 border-red-600 flex items-center justify-between rounded-xl px-2">
        <div>Бонус Владения</div>
        <div>{{ character.possession_bonus }}</div>
    </div>
</template>
<script setup>
import {computed,} from "vue";
import {useCharacterStore} from "@/stores/characterStore.js";

const store = useCharacterStore();
const character = computed(() => store.character);


</script>

<style scoped></style>
