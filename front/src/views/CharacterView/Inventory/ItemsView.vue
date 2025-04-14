<template>
    <div class="">
        <form id="search">Search
            <input name="query" class="border-2 w-full px-3" v-model="search"/>
        </form>
        <Badge v-for="rarity in Object.keys(store.rarity_list)"
               @click="getSearchRarity(rarity)"
               :class="getRarityColor(rarity)">
            <span>{{ rarity }}</span>
        </Badge>
        <!-- Колонки -->
        <div class="">
            <!-- Цикл для каждой буквы -->
            <div v-for="(group, letter) in groupedItems" :key="letter"
                 class="">
                <h2 class="">{{ letter }}</h2>
                <ul class="">
                    <!-- Цикл для предметов в группе -->
                    <li v-for="item in group" :key="item.id"

                        :class="['border-2 mb-1 flex justify-between',
                            item.rarity.id=== 2 ?'bg-stone-200 border-stone-300' :
                            item.rarity.id=== 3
                            ?'bg-blue-200 border-blue-300' :
                            item.rarity.id=== 4
                            ?'bg-purple-200 border-purple-300' :
                            item.rarity.id=== 5
                            ?'bg-amber-200 border-amber-300' :
                            item.rarity.id=== 6
                            ?'bg-red-200 border-red-300' :
                            'bg-grey-100 border-grey-200']">
                        <Dialog>
                            <DialogTrigger
                                    as-child
                                    @click="getDescriptionItem(item)"
                            >
                                <Button variant="outline "
                                        class="text-balance"
                                >
                                    {{ item.name }}
                                </Button>
                            </DialogTrigger>
                            <DialogContent class="overflow-y-auto max-h-[80vh]">

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

                        <div class="flex">
                            <Badge
                                    v-if="isItemInMyList(item.id)"
                                    type="button"
                                    class="mr-2 bg-green-500"
                                    @click="deleteItem(item.id)"
                            >
                                -
                            </Badge>
                            <Badge
                                    v-else
                                    type="button"
                                    class="mr-2 bg-red-500"
                                    @click="patchItem(item)"
                            >
                                +
                            </Badge>

                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script setup>
import {computed, onMounted, ref, watch} from "vue";
import {useInventoryStore} from "@/stores/inventoryStore.js";
import {useCharacterStore} from "@/stores/characterStore.js";
import {Badge} from "@/components/ui/badge/index.js";
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

const search = ref('');
const polling = ref(null);
const store = useInventoryStore()
const character = useCharacterStore()
const my_items = computed(() => character.character.my_items)
const item_list = computed(() => store.item_list)
const item_details = computed(() => store.item_details)
const searchListRarity = computed(() => store.searchListRarity)

watch(search, () => {
        patchSearch();

    }
)
const patchSearch = () => {
    destroyInterval();
    createTimer();
}

onMounted(() => {
    store.getInventory()
});

function getDescriptionItem(item) {
    store.getDescriptionItem(item)
}

const groupedItems = computed(() => {
    if (item_list.value) {
        return item_list.value.reduce((groups, item) => {
            const letter = item.name[0].toUpperCase(); // Первая буква
            if (!groups[letter]) {
                groups[letter] = [];
            }
            groups[letter].push(item);
            return groups;
        }, {});
    }
})
const isItemInMyList = (itemId) => {
    return my_items.value.some(item => item.item.id === itemId);
};
const destroyInterval = () => {
    if (polling.value) {
        clearInterval(polling.value);
    }
};
const createTimer = () => {
    pollData();
};

const pollData = () => {
    polling.value = setTimeout(() => {
        store.getInventory(search.value)
    }, 2000);
};

const patchItem = (item) => {
    store.patchItem(item);
};


const deleteItem = (item) => {
    store.deleteItem(item);
};

function getRarityColor(rarity) {
    return {
        'bg-lime-600': !searchListRarity.value.includes(store.rarity_list[rarity]),
        'bg-cyan-600': searchListRarity.value.includes(store.rarity_list[rarity])  // Цвет при выборе
    };
}

function getSearchRarity(rarity) {
    const index = searchListRarity.value.indexOf(store.rarity_list[rarity]);
    if (index !== -1) {
        searchListRarity.value.splice(index, 1); // Удаляем 1 элемент по индексу
    } else {
        searchListRarity.value.push(store.rarity_list[rarity])
    }
    patchSearch();
}

</script>

<style scoped></style>
