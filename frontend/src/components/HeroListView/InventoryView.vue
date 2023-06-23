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
        v-for="item in my_items"
        v-bind:key="item"
      >
        <a
          href=""
          data-bs-toggle="modal"
          data-bs-target="#ModalItemView"
          @click="loadItemInfo(item.item.id)"
        >
          {{ item.item.name }}
        </a>
        <div
          class="modal fade"
          id="ModalItemView"
          tabindex="-1"
          aria-labelledby="ModalLabelItemView"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div
              class="modal-content"
              v-if="item_detail && item_detail.id === this.id"
            >
              <div class="modal-header">
                <h5 class="modal-title" id="ModalLabelItemView">
                  {{ item_detail.name }}
                </h5>
              </div>
              <div class="modal-body">
                <div>{{ item_detail }}</div>
              </div>
            </div>
            <div class="modal-content" v-else>load</div>
          </div>
        </div>
        <button
          type="button"
          class="btn btn-danger"
          @click="item.quantity++, patch()"
        >
          +
        </button>
        {{ item.quantity }}
        <button
          type="button"
          class="btn btn-danger"
          @click="item.quantity--, patch()"
          :disabled="item.quantity < 1"
        >
          -
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import ItemSearch from "../Inventory/ItemSearch.vue";
import { mapState } from "vuex";
export default {
  name: "InventoryView",
  components: {
    ItemSearch,
  },
  data() {
    return {
      id: "",
      polling: null,
    };
  },
  computed: {
    ...mapState({
      my_items: (state) => state.champion.listInfo.my_items,
      item_detail: (state) => state.item.item_detail,
    }),
  },
  methods: {
    loadInventory() {
      this.$store.dispatch("item/getData");
    },

    loadItemInfo(id) {
      console.log(id);
      this.$store.dispatch("item/getDetailItem", id);
      this.id = id;
    },

    patch() {
      this.destroyInterval();
      this.createTimer();
    },
    pollData() {
      this.polling = setTimeout(() => {
        this.$store.dispatch("champion/patchItem");
      }, 2000);
    },
    destroyInterval() {
      if (this.polling) {
        clearInterval(this.polling);
      }
    },
    createTimer() {
      this.pollData();
    },
  },
};
</script>
<style scoped></style>
