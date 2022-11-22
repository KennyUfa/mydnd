<template>
чарлист
</template>

<script>
import store from "@/store";
import {auth} from "@/store/auth.module";

export default {
  name: "CharList",
  computed: {
    currentUser() {
      return store.state.auth.status.loggedIn;
    }
  },
  mounted() {
    console.log(this.currentUser)
    if (!this.currentUser) {
      this.$router.push({ path: '/login' });
    }
  }
}
</script>

<style scoped>

</style>