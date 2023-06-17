<!-- <template>
  <div>
    <a
      href=""
      data-bs-toggle="modal"
      data-bs-target="#exampleModal3"
      @click="loadSpellInfo(spell.id)"
    >
      {{ spell.name }}
      {{ spell.lvl }}
      {{ spell.class_actor }}</a
    >
    <div class="">
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
    </div>
    <div
      class="modal fade"
      id="exampleModal3"
      tabindex="-1"
      aria-labelledby="exampleModalLabel3"
      aria-hidden="true"
      v-if="
        this.$store.state.spellbook.spell_detail &&
        this.$store.state.spellbook.spell_detail.id === spell.id
      "
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel3">
              {{ $store.state.spellbook.spell_detail.name }}
            </h5>
          </div>
          <div class="modal-body">
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
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SpellDetail",
  methods: {
    loadSpellInfo(id) {
      this.$store.dispatch("spellbook/getDetailSpell", id);
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

<style lang="scss" scoped></style> -->
