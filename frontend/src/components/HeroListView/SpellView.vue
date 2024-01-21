<template>
  <div
    class="modal fade"
    id="SpellModalToggleOne"
    aria-hidden="true"
    aria-labelledby="SpellModalToggleLabelOne"
    tabindex="-1"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="SpellModalToggleLabelOne">
            Список заклинаний
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Закрыть"
          ></button>
        </div>
        <a
          v-if="!this.$store.state.spellbook.spellList"
          class="dropdown-item"
          href="#"
          >Загрузка</a
        >
        <div class="modal-body" v-else>
          <form id="search">
            Search <input name="query" v-model="search" />
          </form>
          <div
            class="spellbook border border-primary"
            v-for="spell in this.$store.state.spellbook.spellList"
            v-bind:key="spell"
          >
            <a
              class="btn btn-primary"
              data-bs-target="#SpellModalToggle2"
              data-bs-toggle="modal"
              @click="loadSpellInfo(spell.id)"
            >
              {{ spell.name }}
              {{ spell.lvl }}
              {{ spell.class_actor }}
            </a>
            <button
              type="button"
              class="btn btn-success"
              @click="addSpell(spell.id)"
            >
              +
            </button>
            <button
              v-if="
                this.$store.state.champion.listInfo.spells_id.includes(spell.id)
              "
              type="button"
              class="btn btn-danger"
              @click="deleteSpell(spell.id)"
            >
              -
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="SpellModalToggle2"
    aria-hidden="true"
    aria-labelledby="SpellModalToggleLabel2"
    tabindex="-1"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div
        class="modal-content"
        v-if="
          this.$store.state.spellbook.spell_detail &&
          this.$store.state.spellbook.spell_detail.id === this.id_spell
        "
      >
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="SpellModalToggleLabel2">
            {{ $store.state.spellbook.spell_detail.name }}
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Закрыть"
          ></button>
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
        <div class="modal-footer">
          <button
            class="btn btn-primary"
            data-bs-target="#SpellModalToggleOne"
            data-bs-toggle="modal"
          >
            Вернуться к списку
          </button>
        </div>
      </div>
      <div class="modal-content" v-else>load</div>
    </div>
  </div>
  <a
    class="btn btn-primary"
    data-bs-toggle="modal"
    href="#SpellModalToggleOne"
    role="button"
    @click="loadSpells"
    >Книга заклинаний</a
  >
  <div class="card-body">
    <!-- Оставьте эту часть без изменений, она отвечает за отображение заклинаний -->
    <div
      class="spellbook border border-primary"
      v-for="spell in this.$store.state.champion.listInfo.spells"
      v-bind:key="spell"
    >
      <a
        href=""
        data-bs-toggle="modal"
        data-bs-target="#SpellModalToggle2"
        @click="loadSpellInfo(spell.id)"
      >
        {{ spell.name }}
        {{ spell.lvl }}
        {{ spell.class_actor }}
      </a>
      <button
        type="button"
        class="btn btn-danger"
        @click="deleteSpell(spell.id)"
      >
        -
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SpellView",
  data() {
    return {
      id: "",
      search: "",
      polling: null,
      id_spell: "",
    };
  },
  watch: {
    search() {
      this.patchSearch();
    },
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
  },
};
</script>

<style scoped></style>
