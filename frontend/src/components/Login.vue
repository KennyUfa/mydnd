<template>
    <div class="wrapper fadeInDown">
  <div id="formContent">
    <!-- Login Form -->
    <form>
      <input type="text" v-model="login" class="fadeIn second" placeholder="login">
      <input type="text" v-model="password" class="fadeIn third" placeholder="password">
      <button class="fadeIn fourth" @click="this.submit">Войти</button>
    </form>

    <!-- Remind Passowrd -->
    <div id="formFooter">
      <a class="underlineHover" href="#">Forgot Password?</a>
    </div>

  </div>
  </div>
</template>
<script>
import AuthService from "../serveces/auth.service";
export default {
  data() {
    return {
      login: '',
      password: ''
    }
  },
  computed: {
    isValid() {
      return this.login !== '' && this.password !== ''
    }
  },
  methods: {
    submit() {
      if (this.isValid) {
        AuthService.login(this.login,this.password);
      }
    }
  }
}
</script>