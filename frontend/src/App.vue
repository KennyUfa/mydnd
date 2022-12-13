<template>
  <div class="container-fluid">
    <navbar-view></navbar-view>
    <router-view></router-view>
  </div>
</template>

<script>
import NavbarView from './components/NavbarView.vue';
export default {
  components: { NavbarView },
  name: "App",
}
</script>
