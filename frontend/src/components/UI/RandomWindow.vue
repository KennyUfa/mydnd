<template>
  <div v-if="showPopup" class="popup">
    <div class="popup-content">
      <p>Total: {{ responseData.total }}</p>
      <p>Skill Value: {{ responseData.skillValue }}</p>
      <p>Random Result: {{ responseData.random_result }}</p>
      <p>Possession Bonus: {{ responseData.possession_bonus }}</p>
      <button @click="closePopup">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showPopup: false,
      responseData: null,
    };
  },
  methods: {
    openPopup(responseData) {
      this.responseData = responseData;
      this.showPopup = true;
    },
    closePopup() {
      this.showPopup = false;
    },
  },
};
</script>

<style>
.popup {
  position: fixed;
  bottom: 10px;
  right: 10px;
  background-color: white;
  border: 1px solid #ccc;
  padding: 10px;
  z-index: 9999;
}

.popup-content {
  text-align: left;
}
</style>
