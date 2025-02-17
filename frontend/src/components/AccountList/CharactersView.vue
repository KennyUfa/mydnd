<template>
  <div class="container">
    <list-champions></list-champions>
    <form-addchampion></form-addchampion>
  </div>
</template>

<script>
import ListChampions from "./ListChampions.vue";
import FormAddchampion from "./FormAddсhampion.vue";

export default {
  components: {
    ListChampions,
    FormAddchampion,
  },
};
</script>

<style scoped></style>
