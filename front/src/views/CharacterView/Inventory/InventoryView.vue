<template>
    <momey-view></momey-view>
    <div v-for="item in my_items"
         class="border-2 mb-2 p-1 flex justify-between">
        <div>
            <div class="text-[14px]">надето</div>
            <Checkbox class="h-6 w-12" v-model="item.put_on"
                      @click="item.put_on = !item.put_on,patchItem()"></Checkbox>
        </div>

        <Dialog>
            <DialogTrigger class=""
                           as-child
                           @click="getDescriptionItem(item.item)">
                <Button variant="outline "
                        class="text-balance"
                >
                    {{ item.item.name }}
                </Button>
            </DialogTrigger>
            <DialogContent class="">
                <DialogHeader>
                    <DialogTitle v-if="item_details">
                        {{ item_details.name }}
                    </DialogTitle>
                    <DialogTitle v-else>Загрузка..
                        .
                    </DialogTitle>
                    <DialogDescription v-if="item_details"
                                       class="overflow-y-auto">
                        <item-detail></item-detail>
                    </DialogDescription>
                    <DialogDescription v-else>Загрузка..
                    </DialogDescription>
                </DialogHeader>
            </DialogContent>
        </Dialog>

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
import MomeyView from "@/views/CharacterView/Inventory/MoneyView.vue";
import {Badge} from "@/components/ui/badge/index.js";
import {computed, ref} from "vue";
import {useInventoryStore} from "@/stores/inventoryStore.js";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger
} from "@/components/ui/dialog/index.js";
import {Button} from "@/components/ui/button/index.js";
import ItemDetail from "@/views/CharacterView/Inventory/ItemDetail.vue";
import {Checkbox} from "@/components/ui/checkbox/index.js";

const character = useCharacterStore()
const inventory = useInventoryStore()

const my_items = computed(() => character.character.my_items)
const polling = ref(null);
const item_details = computed(() => inventory.item_details)

function getDescriptionItem(item) {
    inventory.getDescriptionItem(item)
}

const patchPutOn = (item) => {
    item.put_on = !item.put_on;
    patchItem()
}


const patchItem = () => {
    destroyInterval();
    polling.value = setTimeout(() => {
        inventory.patchInventoryItem()
    }, 2000);
};

const destroyInterval = () => {
    if (polling.value) {
        clearInterval(polling.value);
    }
};

</script>
