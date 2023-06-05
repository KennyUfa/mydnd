<template>
  <header class="p-3 text-bg-dark">
    <div class="container">
      <div
        class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start"
      >
        <a
          href="/"
          class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none"
        >
          <img
            src="https://cdn.shopify.com/s/files/1/0170/5859/4880/products/SP-Kenny-Stand-28_1024x1024.jpg?v=1618604105"
            height="30"
            alt="MDB Logo"
            loading="lazy"
          />
        </a>
        <ul
          class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0"
        >
          <li><a href="/" class="nav-link px-2 text-secondary">Home</a></li>
          <li>
            <a href="/characters" class="nav-link px-2 text-white"
              >Лист персонажей</a
            >
          </li>
          <li>
            <a href="/charlist" class="nav-link px-2 text-white"
              >Мой персонаж</a
            >
          </li>
        </ul>
        <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
          <input
            type="search"
            class="form-control form-control-dark text-bg-dark"
            placeholder="Search..."
            aria-label="Search"
          />
        </form>
        <div class="text-end" v-if="$store.state.auth.name">
          <button type="button" class="btn btn-outline-light me-2">
            Имя аккаунта {{ $store.state.auth.name }}
          </button>
          <button type="button" class="btn btn-warning" @click="logout">
            Logout
          </button>
        </div>
      </div>
    </div>
  </header>
</template>
<script>
export default {
  data() {
    return {
      isActive: 1,
    };
  },

  name: "LoginView",
  methods: {
    logout() {
      this.$store.dispatch("auth/logout");
      this.$router.push({ path: "/" });
    },
  },
};
</script>
