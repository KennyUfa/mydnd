<template>
    <div
            class="border-2 border-red-600 flex items-center justify-between p-2 rounded-xl">
        <div class="text-xs flex border-2 ">
            <div class="flex flex-row">
                Максимум хитов
            </div>
            <div class="flex pl-2"> {{ character.max_hit }}</div>
            <MaxHit></MaxHit>
        </div>

        <!--      <div class="">-->
        <!--        Текущие Хиты {{ character.current_hit }}-->
        <!--      </div>-->
        <!--      <div class="">-->
        <!--        <button class="" @click="heal">Heal</button>-->
        <!--        <button class="" @click="damage">Damage</button>-->
        <!--      </div>-->
        <!--      <div v-if="!show" class="">-->
        <!--        Временные Хиты {{ character.temp_hit }}-->
        <!--      </div>-->
        <!--      <div class="" v-if="show">-->
        <!--        Временные Хиты {{ character.temp_hit }}-->
        <!--      </div>-->
        <!--      <div class="">-->
        <!--        <div class="">Кость Хитов</div>-->
        <!--      </div>-->
        <!--      <div class="">-->
        <!--        <div class="">Спасброски от смерти</div>-->
        <!--      </div>-->
    </div>
</template>

<script setup>
import MaxHit from "@/views/CharacterView/HitView/MaxHit.vue";
import {computed, ref} from "vue";
import {useCharacterStore} from "@/stores/characterStore.js";

const store = useCharacterStore();


const character = computed(() => store.character);
const show = ref(false);


</script>

<style scoped></style>
