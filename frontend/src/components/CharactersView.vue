<template>
  <div class="container">
    <list-champions></list-champions>
    <form-addchampion></form-addchampion>
  </div>
</template>

<script>
import ListChampions from "../components/AccountList/ListChampions.vue";
import FormAddchampion from "../components/AccountList/FormAddсhampion.vue";

export default {
  components: {
    ListChampions,
    FormAddchampion,
  },
};
</script>

<style scoped></style>
