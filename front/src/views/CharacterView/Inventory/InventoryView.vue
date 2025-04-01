<template>
    <div v-for="item in my_items"
         class="border-2 mb-2 p-1 flex justify-between">
        <div>{{ item.item.name }}</div>

        <div>
            <Badge
                    type="button"
                    class="mr-2"
                    @click="item.quantity++, patchItem()"
            >
                +
            </Badge>
            {{ item.quantity }}
            <Badge
                    type="button"
                    class="ml-2"
                    @click="item.quantity--, patchItem()"
            >
                -
            </Badge>
        </div>

    </div>
</template>
<script setup>
import {useCharacterStore} from "@/stores/characterStore.js";
import {Badge} from "@/components/ui/badge/index.js";
import {computed, ref} from "vue";
import {useInventoryStore} from "@/stores/inventoryStore.js";

const character = useCharacterStore()
const inventory = useInventoryStore()

const my_items = computed(() => character.character.my_items)
const polling = ref(null);

const patchItem = () => {
    destroyInterval();
    polling.value = setTimeout(() => {
        inventory.patchInventaryItem()
    }, 2000);
};

const destroyInterval = () => {
    if (polling.value) {
        clearInterval(polling.value);
    }
};


</script>
