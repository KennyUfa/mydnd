<template>
    <!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <!-- Container wrapper -->
    <div class="container">
      <!-- Navbar brand -->
      <a class="navbar-brand me-2" href="/">
        <img
          src="https://cdn.shopify.com/s/files/1/0170/5859/4880/products/SP-Kenny-Stand-28_1024x1024.jpg?v=1618604105"
          height="30"
          alt="MDB Logo"
          loading="lazy"
          style="margin-top: -1px;"
        />
      </a>
  
      <!-- Toggle button -->
      <button
        class="navbar-toggler"
        type="button"
        data-mdb-toggle="collapse"
        data-mdb-target="#navbarButtonsExample"
        aria-controls="navbarButtonsExample"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <i class="fas fa-bars"></i>
      </button>
  
      <!-- Collapsible wrapper -->
      <div class="collapse navbar-collapse" id="navbarButtonsExample">
        <!-- Left links -->
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="/charlist">CharList</a>
          </li>
        </ul>
        <!-- Left links -->
  
        <div class="d-flex align-items-center">
          <button type="button" class="btn btn-primary me-3">
            Login
          </button>
          <button type="button" class="btn btn-primary me-3" @click="logout">
            Logout
          </button>
        </div>
      </div>
      <!-- Collapsible wrapper -->
    </div>
    <!-- Container wrapper -->
  </nav>
  <!-- Navbar -->
</template>
<script>

export default {
  name: "LoginView",
  methods:{
    logout(){
      this.$store.dispatch('auth/logout');
      this.$router.push({ path: '/' });
    }
  }
}
</script>