<template>
  <div class="card-text stat">
    <h4>{{ backgroundName }}</h4>
    <strong>Описание</strong>:
    <p v-if="!show">
      {{ backgroundValue }}
    </p>
    <textarea v-else v-model="backgroundValue"></textarea>
  </div>
</template>

<script>
export default {
  name: "BackgroundInfo",
  props: ['backgroundName', 'backgroundValue', 'show'],
  watch: {
    backgroundValue() {
      this.onUserChange()
    }
  },
  data(){
    return{
      saveBackground:true,
    }
  },
  methods: {
    onUserChange: function () {
      this.$emit('update:backgroundValue', this.backgroundValue);
      this.saveBackground=false;
    }
  }
}
</script>

<style scoped>

</style>