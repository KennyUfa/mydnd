<template>
  <div class="container">
    <list-champions></list-champions>
    <form-add></form-add>
  </div>
</template>

<script>
import ListChampions from "@/views/AccountList/ListChampions.vue";
import FormAdd from "@/views/AccountList/FormAdd.vue";

export default {
  components: {
    FormAdd,
    ListChampions,
  },
};
</script>

<style scoped></style>
