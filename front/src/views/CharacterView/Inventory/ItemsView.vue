<template>
  <div class="container mx-auto p-4">
    <form id="search">Search <input name="query" v-model="search"/></form>
    <!-- Колонки -->
    <div class="gap-4">
      <!-- Цикл для каждой буквы -->
      <div v-for="(group, letter) in groupedItems" :key="letter"
           class="col-span-1">
        <h2 class="text-lg font-bold mb-2">{{ letter }}</h2>
        <ul class="list-disc list-inside grid grid-cols-4">
          <!-- Цикл для предметов в группе -->
          <li v-for="item in group" :key="item.id" class="mb-1">
            <span @click="patchItem(item)">{{ item.name }}</span>
            <Badge
              type="button"
              class="btn btn-success"
              @click="patchItem(item)"
            >
              +
            </Badge>
            <Badge
              v-if="isItemInMyList(item.id)"
              type="button"
              class="btn btn-danger"
              @click="deleteItem(item.id)"
            >
              -
            </Badge>
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

const search = ref('');
const polling = ref(null);
const store = useInventoryStore()
const character = useCharacterStore()
const my_items = computed(() => character.character.my_items)
const item_list = computed(() => store.item_list)

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

</script>

<style scoped></style>
