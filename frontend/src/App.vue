<template>
  <div class="container-fluid">
    <navbar-view></navbar-view>
    <router-view></router-view>
  </div>
</template>

<script>
import NavbarView from "./components/NavbarView.vue";
import ListChampions from "./components/AccountList/ListChampions.vue";
import FormAddchampion from "./components/AccountList/FormAddсhampion.vue";

export default {
  components: { NavbarView, ListChampions, FormAddchampion },
  name: "App",
};
</script>
ç