<template>
  <div class="card">
    <button v-if="!show" v-on:click="show = !show">{{ this.show }}
    </button>
    <button v-if="show" v-on:click="show = !show, patchHit()">{{ this.show }}
    </button>
    <div class="card-body stat">
      <h5 v-if="!show" class="card-title">Максимум хитов {{
          this.$store.state.champion.listInfo.max_hit
        }}</h5>

      <h5 v-if="show" class="card-title">Максимум хитов {{
          this.$store.state.champion.listInfo.max_hit
        }}
        <button
            class="col"
            @click="$store.state.champion.listInfo.max_hit++"
        >
          +
        </button>
        <button
            class="col"
            @click="$store.state.champion.listInfo.max_hit--"
            :disabled="$store.state.champion.listInfo.max_hit < 1"
        >
          -
        </button>
      </h5>

      <h5 class="card-title">Текущие Хиты {{
          this.$store.state.champion.listInfo.current_hit
        }}</h5>
      <div class="row">
        <button class="col" @click="heal">Heal</button>
        <input class="col"
               type="number" v-model="hit">
        <button class="col" @click="damage">
          Damage
        </button>
      </div>
      <h5 v-if="!show" class="card-title">Временные Хиты {{
          this.$store.state.champion.listInfo.temp_hit
        }}</h5>
      <h5 class="card-title" v-if="show">Временные Хиты {{
          this.$store.state.champion.listInfo.temp_hit
        }}
        <button
            class="col"
            @click="$store.state.champion.listInfo.temp_hit++"
        >
          +
        </button>
        <button
            class="col"
            @click="$store.state.champion.listInfo.temp_hit--"
            :disabled="$store.state.champion.listInfo.temp_hit < 1"
        >
          -
        </button>
      </h5>
    </div>
  </div>
</template>

<script>
export default {
  name: "HitVue",
  data() {
    return {
      hit: 0,
      show: false,
    }
  },
  methods: {
    patchHit() {
      this.$store.dispatch("champion/patchHit");
    },
    heal() {
      this.$store.dispatch("champion/heal", this.hit);
      this.hit = 0
    },
    damage() {
      this.$store.dispatch("champion/damage", this.hit);
      this.hit = 0
    }
  }
}
</script>

<style scoped>

</style>