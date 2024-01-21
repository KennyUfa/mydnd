<template>
  <div class="card">
    <div
      class="modal fade"
      id="exampleModalToggle"
      aria-hidden="true"
      aria-labelledby="exampleModalToggleLabel"
      tabindex="-1"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <!-- начало списка модального окна -->
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalToggleLabel">
              Предметы
              <form id="search">
                <input name="query" v-model="search" />Search
              </form>
            </h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <a
              v-if="!this.$store.state.item.itemList"
              class="dropdown-item"
              href="#"
              >Загрузка</a
            >
            <div class="modal-body" v-else>
              <div
                class="border border-primary"
                v-for="item in this.$store.state.item.itemList"
                v-bind:key="item"
              >
                <button
                  type="button"
                  class="btn btn-success"
                  @click="addItem(item.id)"
                >
                  +
                </button>
                <button
                  v-if="
                    this.$store.state.champion.listInfo.my_items.includes(
                      item.id
                    )
                  "
                  type="button"
                  class="btn btn-danger"
                  @click="deleteItem(item.id)"
                >
                  -
                </button>
                <a
                  href=""
                  @click="loadItemInfo(item.id)"
                  data-bs-target="#exampleModalToggle2"
                  data-bs-toggle="modal"
                >
                  {{ item.name }}
                  <!-- Open second modal -->
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="modal fade"
      id="exampleModalToggle2"
      aria-hidden="true"
      aria-labelledby="exampleModalToggleLabel2"
      tabindex="-1"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div
          class="modal-content"
          v-if="item_detail && item_detail.id === this.id"
        >
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalToggleLabel2">
              <!-- Modal 2 -->
              {{ item_detail.name }}
            </h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            {{ item_detail }}
            <!-- Hide this modal and show the first with the button below. -->
          </div>
          <div class="modal-footer">
            <button
              class="btn btn-primary"
              data-bs-target="#exampleModalToggle"
              data-bs-toggle="modal"
            >
              Назад в список
            </button>
          </div>
        </div>
        <div class="modal-content" v-else>load</div>
      </div>
    </div>
    <button
      class="btn btn-primary"
      data-bs-toggle="modal"
      href="#exampleModalToggle"
      role="button"
      @click="loadInventory"
    >
      Поиск по инвентарю
    </button>
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
import { mapState } from "vuex";
export default {
  name: "InventoryView",
  data() {
    return {
      search: "",
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
  watch: {
    search() {
      this.patchSearch();
    },
  },
  methods: {
    loadInventory() {
      this.$store.dispatch("item/getData");
    },

    loadItemInfo(id) {
      this.$store.dispatch("item/getDetailItem", id);
      this.id = id;
    },

    patch() {
      this.destroyInterval();
      this.createTimer();
    },
    patchSearch() {
      this.destroyInterval();
      this.createTimerSearch();
    },
    pollDataSearch() {
      this.polling = setTimeout(() => {
        this.$store.dispatch("item/getData", this.search);
      }, 1000);
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
    createTimerSearch() {
      this.pollDataSearch();
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
