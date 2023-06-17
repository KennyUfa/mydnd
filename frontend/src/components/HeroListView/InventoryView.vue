<template>
  <div class="card">
    <div class="card-header">
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
        @click="loadInventory"
      >
        Поиск по инвентарю
      </button>
      <div
        class="modal fade"
        id="exampleModal"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Предметы</h5>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <a
              v-if="!this.$store.state.item.itemList"
              class="dropdown-item"
              href="#"
              >Загрузка</a
            >
            <div class="modal-body" v-else><ItemSearch></ItemSearch></div>
          </div>
        </div>
      </div>
    </div>
    <div class="card-body">
      <div
        class="spellbook border border-primary"
        v-for="item in this.$store.state.champion.listInfo.items"
        v-bind:key="item"
      >
        <a
          href=""
          data-bs-toggle="modal"
          data-bs-target="#ModalItemView"
          @click="loadItemInfo(item.id)"
        >
          {{ item.name }}
        </a>
        <div
          class="modal fade"
          id="ModalItemView"
          tabindex="-1"
          aria-labelledby="ModalLabelItemView"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="ModalLabelItemView">
                  {{ item.name }}
                </h5>
              </div>
              <div
                class="modal-body"
                v-if="
                  this.$store.state.item.item_detail &&
                  this.$store.state.item.item_detail.id === this.id
                "
              >
                <div>{{ $store.state.item.item_detail }}</div>
              </div>
              <div class="modal-content" v-else>load</div>
            </div>
          </div>
        </div>
        <button
          type="button"
          class="btn btn-danger"
          @click="deleteItem(item.id)"
        >
          -
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import ItemSearch from "../Inventory/ItemSearch.vue";
export default {
  name: "InventoryView",
  components: {
    ItemSearch,
  },
  data() {
    return {
      id: "",
    };
  },
  methods: {
    deleteItem(id) {
      this.$store.dispatch("champion/deleteItem", id);
    },
    loadInventory() {
      this.$store.dispatch("item/getData");
    },
    loadItemInfo(id) {
      this.$store.dispatch("item/getDetailItem", id);
      this.id = id;
    },
  },
};
</script>
<style scoped></style>
