<template>
  <form id="search">Search <input name="query" v-model="search" /></form>
  <div
    class="border border-primary"
    v-for="item in this.$store.state.item.itemList"
    v-bind:key="item"
  >
    <a
      href=""
      data-bs-toggle="modal"
      data-bs-target="#ModalItemSearch"
      @click="loadItemInfo(item.id)"
    >
      {{ item.name }}</a
    >
    <button type="button" class="btn btn-success" @click="addItem(item.id)">
      +
    </button>
    <button
      v-if="this.$store.state.champion.listInfo.my_items.includes(item.id)"
      type="button"
      class="btn btn-danger"
      @click="deleteItem(item.id)"
    >
      -
    </button>
    <div
      class="modal fade"
      id="ModalItemSearch"
      tabindex="-1"
      aria-labelledby="ModalLabelItemSearch"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div
          class="modal-content"
          v-if="
            this.$store.state.item.item_detail &&
            this.$store.state.item.item_detail.id === this.id_item
          "
        >
          <div class="modal-header">
            <h5 class="modal-title" id="ModalLabelItemSearch">
              {{ $store.state.item.item_detail.name }}
            </h5>
          </div>
          <div class="modal-body">
            <div
              v-for="info in this.$store.state.item.item_detail"
              v-bind:key="info"
            >
              {{ info }}
            </div>
          </div>
        </div>
        <div class="modal-content" v-else>
          <div class="modal-header">
            <h5 class="modal-title" id="ModalLabelItemSearch">Load</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ItemSearch",
  data() {
    return {
      search: "",
      polling: null,
      id_item: "",
    };
  },
  props: {
    id: {
      type: String,
      default: null,
    },
  },
  watch: {
    search() {
      this.patchSearch();
    },
  },
  methods: {
    loadItemInfo(id) {
      this.$store.dispatch("item/getDetailItem", id);
      this.id_item = id;
    },
    patchSearch() {
      this.destroyInterval();
      this.createTimer();
    },
    pollData() {
      this.polling = setTimeout(() => {
        this.$store.dispatch("item/getData", this.search);
      }, 1000);
    },
    destroyInterval() {
      if (this.polling) {
        clearInterval(this.polling);
      }
    },
    createTimer() {
      this.pollData();
    },
    addItem(id) {
      this.$store.dispatch("champion/addItem", id);
    },
    deleteItem(id) {
      this.$store.dispatch("champion/deleteItem", id);
    },
  },
};
</script>

<style scoped></style>
