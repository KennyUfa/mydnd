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
  methods: {
    setLogin() {
      AuthService.login(this.log, this.password);
    }
  },
  mounted() {
  }
}
</script>
<style scoped>

</style>