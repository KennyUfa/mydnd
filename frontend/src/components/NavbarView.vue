<template>
  <header>
    <div class="navbar navbar-expand-lg">
      <div class="container">
        <a href="/" class="navbar-brand">
          <img
            src="https://cdn.shopify.com/s/files/1/0170/5859/4880/products/SP-Kenny-Stand-28_1024x1024.jpg?v=1618604105"
            height="30"
            alt="MDB Logo"
            loading="lazy"
            style="margin-top: -1px"
          />
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarTogglerDemo03"
          aria-controls="navbarTogglerDemo03"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            class="bi"
            fill="currentColor"
            viewBox="0 0 16 16"
          >
            <path
              fill-rule="evenodd"
              d="M2.5 11.5A.5.5 0 0 1 3 11h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4A.5.5 0 0 1 3 7h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4A.5.5 0 0 1 3 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"
            ></path>
          </svg>
        </button>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a href="/" class="nav-link text-secondary">Home</a>
            </li>
            <li class="nav-item">
              <a href="/characters" class="nav-link">Лист персонажей</a>
            </li>
            <li class="nav-item">
              <a href="/charlist" class="nav-link">Мой персонаж</a>
            </li>
          </ul>
          <button type="button" class="btn p-0">
            Имя аккаунта {{ $store.state.auth.name }}
          </button>
          <form class="d-flex pt-2" role="search">
            <input
              type="search"
              class="form-control"
              placeholder="Search..."
              aria-label="Search"
            />
          </form>
          <div class="mt-2" v-if="$store.state.auth.name">
            <button type="button" class="btn btn-warning" @click="logout">
              Logout
            </button>
          </div>
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
