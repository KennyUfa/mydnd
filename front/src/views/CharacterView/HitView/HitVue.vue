<template>
    <div class="border-2 border-red-600 rounded-xl relative pt-3">
        <div class="text-center text-xl italic font-bold
             tracking-wide">Здоровье
        </div>
        <div
                class="flex items-center justify-around p-2  pb-4">

            <MaxHit></MaxHit>

            <div class="flex flex-col mr-2">
                <!-- Кнопка "Heal" -->
                <button class="bg-green-500 rounded-xl  px-2 py-1"
                        @click="heal">
                    Heal
                </button>

                <!-- Поле ввода числа -->
                <input
                        class="border-2 border-red-600 rounded-xl  px-2 py-1"
                        data-testid="hp-adjust-input"
                        type="number"
                        aria-label="Hit Points Adjustment"
                        min="0"
                        max="999"
                        v-model="buffer_hit"
                />

                <!-- Кнопка "Damage" -->
                <button
                        class="bg-red-500 rounded-xl px-2 py-1"
                        @click="damage">Damage
                </button>
            </div>

            <div
                    class="flex flex-col border-2 p-1 rounded-xl border-red-600 text-center px-3">
                <div class="text-s">
                    Текущее
                </div>
                <div class="text-xl"> {{ character.current_hit }}</div>
            </div>
            <div class="flex flex-col border-2 text-center p-1 rounded-xl border-red-600 px-3">
                <div class="text-s">
                    MAX
                </div>
                <div class="text-xl"> {{ character.max_hit }}</div>
            </div>
            <div class="flex flex-col border-2 text-center p-1 rounded-xl border-red-600 px-3">
                <div class="text-s">
                    ВРЕМ
                </div>
                <div class="text-xl"> {{ character.temp_hit }}</div>
            </div>
        </div>
    </div>

</template>

<script setup>
import MaxHit from "@/views/CharacterView/HitView/MaxHit.vue";
import {computed, ref} from "vue";
import {useCharacterStore} from "@/stores/characterStore.js";

const store = useCharacterStore();


const character = computed(() => store.character);
const buffer_hit = ref(0);

function heal() {
    if (buffer_hit.value > 0) {
        store.heal(buffer_hit.value);
    }
    buffer_hit.value = 0;
}

function damage() {
    if (buffer_hit.value > 0) {
        store.damage(buffer_hit.value);
    }
    buffer_hit.value = 0;
}
</script>

<style scoped></style>
