<template>
  <form id="search">Search <input name="query" v-model="search" /></form>
  <div
    class="spellbook border border-primary"
    v-for="spell in this.$store.state.spellbook.spellList"
    v-bind:key="spell"
  >
    <a
      href=""
      data-bs-toggle="modal"
      data-bs-target="#ModalSpellSearch"
      @click="loadSpellInfo(spell.id)"
    >
      {{ spell.name }}
      {{ spell.lvl }}
      {{ spell.class_actor }}</a
    >
    <button type="button" class="btn btn-success" @click="addSpell(spell.id)">
      +
    </button>
    <button
      v-if="this.$store.state.champion.listInfo.spells_id.includes(spell.id)"
      type="button"
      class="btn btn-danger"
      @click="deleteSpell(spell.id)"
    >
      -
    </button>
    <div
      class="modal fade"
      id="ModalSpellSearch"
      tabindex="-1"
      aria-labelledby="ModalLabelSpellSearch"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div
          class="modal-content"
          v-if="
            this.$store.state.spellbook.spell_detail &&
            this.$store.state.spellbook.spell_detail.id === this.id_spell
          "
        >
          <div class="modal-header">
            <h5 class="modal-title" id="ModalLabelSpellSearch">
              {{ $store.state.spellbook.spell_detail.name }}
            </h5>
          </div>
          <div class="modal-body">
            <div>{{ $store.state.spellbook.spell_detail.lvl }}</div>
            <div>{{ $store.state.spellbook.spell_detail.class_actor }}</div>
            <div>{{ $store.state.spellbook.spell_detail.components }}</div>
            <div>{{ $store.state.spellbook.spell_detail.distance }}</div>
            <div>{{ $store.state.spellbook.spell_detail.time_cast }}</div>
            <div>{{ $store.state.spellbook.spell_detail.timing }}</div>
            <div>{{ $store.state.spellbook.spell_detail.origin }}</div>
            <div>{{ $store.state.spellbook.spell_detail.instruction }}</div>
          </div>
        </div>
        <div class="modal-content" v-else>
          <div class="modal-header">
            <h5 class="modal-title" id="ModalLabelSpellSearch">Load</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SpellsSearch",
  data() {
    return {
      search: "",
      polling: null,
      id_spell: "",
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
    loadSpellInfo(id) {
      this.$store.dispatch("spellbook/getDetailSpell", id);
      this.id_spell = id;
    },
    patchSearch() {
      this.destroyInterval();
      this.createTimer();
    },
    pollData() {
      this.polling = setTimeout(() => {
        this.$store.dispatch("spellbook/getData", this.search);
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
    addSpell(id) {
      this.$store.dispatch("champion/addSpell", id);
    },
    deleteSpell(id) {
      this.$store.dispatch("champion/deleteSpell", id);
    },
  },
};
</script>

<style scoped></style>
