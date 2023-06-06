<template>
  <div>
    <div class="user_login">
      <input v-model="log" type="text" placeholder="Логин" />
      <input v-model="password" type="password" placeholder="Пароль" />
      <button type="button" class="btn btn-primary" @click="login">
        Войти
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      log: "",
      password: "",
    };
  },
  methods: {
    logged() {
      return this.$store.state.auth.user;
    },

    async login() {
      await this.$store.dispatch("auth/login", {
        username: this.log,
        password: this.password,
      });
      if (this.logged) {
        this.$router.push({ path: "/characters" });
      }
    },
  },
};
</script>
<style scoped></style>
