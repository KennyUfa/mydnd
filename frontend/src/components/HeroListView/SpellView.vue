<template>
  <div class="card">
    <div class="card-header">
      <div class="card-header">
        <button
          type="button"
          class="btn btn-primary"
          data-bs-toggle="modal"
          data-bs-target="#exampleModal2"
          @click="loadSpells"
        >
          Открыть книгу заклинаний
        </button>
        <div
          class="modal fade"
          id="exampleModal2"
          tabindex="-1"
          aria-labelledby="exampleModalLabel2"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel2">
                  Список заклинаний
                </h5>
                <button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></button>
              </div>
              <a
                v-if="!this.$store.state.spellbook.spellList"
                class="dropdown-item"
                href="#"
                >Загрузка</a
              >
              <div class="modal-body" v-else><spell-search></spell-search></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="card-body">
      <div
        class="spellbook border border-primary"
        v-for="spell in this.$store.state.champion.listInfo.spells"
        v-bind:key="spell"
      >
        <a
          href=""
          data-bs-toggle="modal"
          data-bs-target="#ModalSpellView"
          @click="loadSpellInfo(spell.id)"
        >
          {{ spell.name }}
          {{ spell.lvl }}
          {{ spell.class_actor }}
        </a>
        <div
          class="modal fade"
          id="ModalSpellView"
          tabindex="-1"
          aria-labelledby="ModalLabelSpellView"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="ModalLabelSpellView">
                  {{ spell.name }}
                </h5>
              </div>
              <div
                class="modal-body"
                v-if="
                  this.$store.state.spellbook.spell_detail &&
                  this.$store.state.spellbook.spell_detail.id === this.id
                "
              >
                <div>{{ $store.state.spellbook.spell_detail.name }}</div>
                <div>{{ $store.state.spellbook.spell_detail.lvl }}</div>
                <div>{{ $store.state.spellbook.spell_detail.class_actor }}</div>
                <div>{{ $store.state.spellbook.spell_detail.components }}</div>
                <div>{{ $store.state.spellbook.spell_detail.distance }}</div>
                <div>{{ $store.state.spellbook.spell_detail.time_cast }}</div>
                <div>{{ $store.state.spellbook.spell_detail.timing }}</div>
                <div>{{ $store.state.spellbook.spell_detail.origin }}</div>
                <div>{{ $store.state.spellbook.spell_detail.instruction }}</div>
              </div>
              <div class="modal-content" v-else>load</div>
            </div>
          </div>
        </div>
        <button
          type="button"
          class="btn btn-danger"
          @click="deleteSpell(spell.id)"
        >
          -
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import SpellSearch from "../SpellBook/SpellsSearch.vue";

export default {
  name: "SpellView",
  components: {
    SpellSearch,
  },
  data() {
    return {
      id: "",
    };
  },
  methods: {
    deleteSpell(id) {
      this.$store.dispatch("champion/deleteSpell", id);
    },
    loadSpells() {
      this.$store.dispatch("spellbook/getData");
    },
    loadSpellInfo(id) {
      this.$store.dispatch("spellbook/getDetailSpell", id);
      this.id = id;
    },
  },
};
</script>

<style scoped></style>
