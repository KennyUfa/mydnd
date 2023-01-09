<template>

  <div class="card-body stat">
    <h5 class="card-title">{{ skillName }}</h5>
    <p class="card-text ">
      {{ skillValue }}
    </p>
    <div id="row counter" v-if="show">
      <button
          class="col"
          @click="skillValue++"
          :disabled="skillValue > 29"
      >
        +
      </button>
      <button
          class="col"
          @click="skillValue--"
          :disabled="skillValue < 2"
      >
        -
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SkillButton",
  props: ['skillName', 'skillValue', 'show'],
  watch: {
    skillValue() {
      this.onUserChange()
    }
  },
  methods: {
    onUserChange: function () {
      this.$emit('update:skillValue', this.skillValue)
    }
  }
}
</script>

<style scoped>

</style>