<template>
  <div class="user_login">
    <input v-model="log" type="text" placeholder="Логин"/>
    <input v-model="password" type="password" placeholder="Пароль"/>
    <button @click="setLogin">Войти</button>
  </div>
</template>

<script>
import AuthService from "@/services/auth.service";

export default {
  name: "LoginView",
  data() {
    return {
      log: '',
      password: '',
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },},
  methods: {
    setLogin() {
      AuthService.login(this.log, this.password)
      this.$store.commit('auth/loginSuccess');
      if(this.loggedIn){
        this.$router.push({ path: '/charlist' });
      }
    }
  },
}
</script>
<style scoped>

</style>