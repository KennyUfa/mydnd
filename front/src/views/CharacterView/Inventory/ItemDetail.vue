<template>
    <div class="m-2 ">
        <div class="inline-block">Редкость - {{
                item_details.rarity.description
            }}
        </div>
        <div class="inline-block ml-3">Тип -{{
                item_details.type.description
            }}
        </div>

        <div v-if="item_details?.equipment" class="mt-2">
            <div>{{ item_details.equipment.price }}</div>
            <div>
                {{ item_details.equipment.description }}
            </div>
            <div class="flex flex-row justify-between mt-3">
                <div>Источник: {{ item_details.equipment.source }}</div>
                <div>Вес: {{ item_details.equipment.weight }} фнт.</div>
            </div>
        </div>
        <div v-else-if="item_details?.magic_item" class="mt-2">
            <div>{{ item_details.magic_item.price }}</div>
            <div class="text-wrap">
                {{ item_details.magic_item.description }}
            </div>
            <div class="flex flex-row justify-between mt-3">
                <div>Источник: {{ item_details.magic_item.source }}</div>
            </div>
        </div>
        <div v-else-if="item_details?.armor" class="mt-2">
            <div>{{ item_details.armor.price }}</div>
            <div>Защита: {{ item_details.armor.armore }}</div>
            <div>Снять/Надеть: {{ item_details.armor.duration }}</div>
            <div class="text-wrap">
                {{ item_details.armor.description }}
            </div>
            <div class="flex flex-row justify-between mt-3">
                <div>Источник: {{ item_details.armor.source }}</div>
                <div>Вес: {{ item_details.armor.weight }}</div>
            </div>
        </div>
        <div v-else-if="item_details?.weapon" class="mt-2">
            <div class="flex flex-row justify-around gap-1">
                <div v-for="prop in item_details.weapon.properties" :key="prop.name">
                    <span>{{ prop.name }}</span>
                </div>
            </div>
            <div class="flex flex-row justify-around gap-1">
            <div>{{ item_details.weapon.price }}</div>
            <div>Урон : {{ item_details.weapon.damage }}</div>
            <div>{{ item_details.weapon.damage_type }}</div>
            </div>
            <div class="text-wrap mt-2">
                {{ item_details.weapon.description }}
            </div>
            <div class="flex flex-row justify-between mt-3">
                <div>Источник: {{ item_details.weapon.source }}</div>
            </div>
        </div>
    </div>
</template>
<script setup>
import {useInventoryStore} from "@/stores/inventoryStore.js";
import {computed} from "vue";


const store = useInventoryStore()
const item_details = computed(() => store.item_details)
</script>
