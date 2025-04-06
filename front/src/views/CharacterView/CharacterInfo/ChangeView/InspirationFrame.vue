<template>
    <div class="border-2 border-red-600 flex items-center justify-between p-2 rounded-xl">

        <button
                class="border-2 w-6 h-6 rounded-xl"
                @click="character.inspiration++, patch()"
                :disabled="character.inspiration > 10"
        >
            +
        </button>
        <div class="mx-2">
            Вдохновение {{ character.inspiration }}
        </div>
        <button
                class="border-2 w-6 h-6 rounded-xl"
                @click="character.inspiration--, patch()"
                :disabled="character.inspiration < 1"
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
const polling = ref(null);


function patch() {
    this.destroyInterval();
    this.createTimer();
}

function pollData() {
    this.polling = setTimeout(() => {
        store.patchInspirationFrame();
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
