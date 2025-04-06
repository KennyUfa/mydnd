<template>
        <div
                class="border-2 border-red-600 flex items-center justify-between p-2 rounded-xl">
            <button
                    class="border-2 w-6 h-6 rounded-xl"
                    @click="character.possession_bonus++, patchP()"
                    :disabled="character.possession_bonus > 10"
            >
                +
            </button>
            <div class="mx-2">Бонус Владения {{ character.possession_bonus
                }}</div>
            <button
                    class="border-2 w-6 h-6 rounded-xl"
                    @click="character.possession_bonus--, patchP()"
                    :disabled="character.possession_bonus < 2"
            >
                -
            </button>
        </div>

</template>
<script setup>
import {computed, ref} from "vue";
import {useCharacterStore} from "@/stores/characterStore.js";

const store = useCharacterStore();


const character = computed(() => store.character);
const show = ref(false);


const polling = ref(null);

function patchP() {
    this.destroyInterval();
    this.createTimer();
}


function pollData() {
    this.polling = setTimeout(() => {
        store.patchPossessionBonus();
    }, 2000);
}


function destroyInterval() {
    if (this.polling) {
        clearInterval(this.polling);
    }
}


function createTimer() {
    this.pollData();
}


</script>

<style scoped></style>
