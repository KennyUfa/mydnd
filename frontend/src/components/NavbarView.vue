<template>
  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand me-2" href="/">
        <img
            src="https://cdn.shopify.com/s/files/1/0170/5859/4880/products/SP-Kenny-Stand-28_1024x1024.jpg?v=1618604105"
            height="30"
            alt="MDB Logo"
            loading="lazy"
            style="margin-top: -1px"
        />
      </a>
      <div class="navbar-collapse">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link" href="/charlist">CharList</a>
          </li>
        </ul>
        <div class="align-items-center">
          <button type="button" v-if="$store.state.auth.name" class="btn me-3">
            Имя аккаунта {{ $store.state.auth.name }}
          </button>
          <button type="button" class="btn btn-primary me-3"
                  @click="this.$router.push('/characters')">
            Лист персонажей
          </button>
          <button type="button" class="btn btn-primary me-3" @click="logout">
          Logout
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
  name: "LoginView",
  methods: {
    logout() {
      this.$store.dispatch("auth/logout");
      this.$router.push({path: "/"});
    },
  },
};
</script>