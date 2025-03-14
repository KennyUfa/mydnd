<template>
  <div>
    <h2>Инвентарь</h2>
    <form id="search">Search <input name="query" v-model="search"/></form>
    <div
      class="spellbook border border-primary"
      v-for="(items,letter) in groupedItems"
    >
      {{ letter }}
      <div v-for="item in items" v-bind:key="item.id">
        {{ item.name }}
        {{ item.damage }}
        {{ item.type?.description }}
      </div>

    </div>
  </div>
</template>

<script setup>
import {computed, onMounted, ref, watch} from "vue";
import {useInventoryStore} from "@/stores/inventoryStore.js";

const search = ref('');
const store = useInventoryStore()
const item_list = computed(() => store.item_list)
watch(search, () => {
    patchSearch();
  }
)
const patchSearch = () => {
  console.log(search)
  // this.destroyInterval();
  // this.createTimer();
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
// groupedItems() {
//       // Сначала сортируем предметы по алфавиту
//       const sortedItems = this.items.sort((a, b) =>
//         a.name.localeCompare(b.name)
//       );
//
//       // Группируем предметы по первой букве
//       return sortedItems.reduce((groups, item) => {
//         const letter = item.name[0].toUpperCase(); // Первая буква
//         if (!groups[letter]) {
//           groups[letter] = [];
//         }
//         groups[letter].push(item);
//         return groups;
//       }, {});
//     },
// export default {
//   name: "InventoryView",
//   data() {
//     return {
//       search: "",
//       polling: null,
//     };
//   },
//   props: {
//     id: {
//       type: String,
//       default: null,
//     },
//   },
//   watch: {
//     search() {
//       this.patchSearch();
//     },
//   },
//   methods: {
//     patchSearch() {
//       this.destroyInterval();
//       this.createTimer();
//     },
//     pollData() {
//       this.polling = setTimeout(() => {
//         this.$store.dispatch("spellbook/getData", this.search);
//       }, 2000);
//     },
//     destroyInterval() {
//       if (this.polling) {
//         clearInterval(this.polling);
//       }
//     },
//     createTimer() {
//       this.pollData();
//     },
//     addSpell(id) {
//       this.$store.dispatch("champion/addSpell", id);
//     },
//     deleteSpell(id) {
//       this.$store.dispatch("champion/deleteSpell", id);
//     },
//   },
// };
</script>

<style scoped></style>
