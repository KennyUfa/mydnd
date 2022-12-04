<template>
  <div class="container">
    CHAMPIONLIST
  </div>
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
    console.log(store.getters['auth/isAuthenticated']);
    // console.log(this.currentUser)
    if (!store.getters['auth/isAuthenticated']) {
      this.$router.push({ path: '/' });
    }
  }
}
</script>

<style scoped>

</style>