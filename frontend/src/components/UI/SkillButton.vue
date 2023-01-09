<template>
  <div class="card-body stat">
    <h5 class="card-title">{{ skillName }}</h5>
    <p class="card-text ">
      всего {{ skillValue }}
    </p>
    <p class="card-text ">
      бонус {{Math.floor((skillValue - 10)/2) }}
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
  data(){
    return{
      saveSkill:true,
    }
  },
  methods: {
    onUserChange: function () {
      this.$emit('update:skillValue', this.skillValue);
      this.saveSkill=false;
    }
  }
}
</script>

<style scoped>

</style>