<template>
  <div class="user_login">
    <input v-model="log" type="text" placeholder="Логин"/>
    <input v-model="password" type="password" placeholder="Пароль"/>
    <button @click="login">Войти</button>
  </div>
</template>

<script>
import { useAttrs } from '@vue/runtime-core';

export default {
  name: "LoginView",
  data() {
    return {
      log: '',
      password: '',
    }
  },
  computed: {

  },
  methods: {
    logged() {
      return this.$store.state.auth.status.loggedIn;
    },
    login() {
      console.log(this.logged)
        return this.$store.dispatch('auth/login',{username:this.log,
          password:this.password}).then(()=>
          {if (this.logged) {
          this.$router.push({path: '/charlist'})}
        // if (this.logged()) {
        //   this.$router.push({path: '/charlist'});
        // }
    });
  },},}
</script>
<style scoped>

</style>