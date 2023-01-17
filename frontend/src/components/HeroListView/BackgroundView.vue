<template>
  <div class="col">
    <button v-if="!show" v-on:click="show = !show">{{ this.show }} не
      видно
    </button>
    <button v-else v-on:click="postSkills">{{ this.show }}видно</button>

    <background-info backgroundName="черты характера"
                     v-model:backgroundValue="$store.state.champion.listInfo.background.personality_traits"
                     v-bind:show="show"
    ></background-info>

    <!--    <div class="card-body stat">-->
    <!--      <h5 class="card-title">ИДЕАЛЫ</h5>-->
    <!--      <p class="card-text">-->
    <!--        Lorem ipsum dolor sit amet, consectetur adipisicing elit.-->
    <!--        Dolorem est iusto laboriosam nulla quidem. Alias corporis cum-->
    <!--        quo tempore? Adipisci enim laboriosam nihil nobis omnis?-->
    <!--        Deleniti earum numquam quae repellat.-->
    <!--      </p>-->
    <!--    </div>-->
    <!--    <div class="card-body stat">-->
    <!--      <h5 class="card-title">ПРИВЯЗАННОСТИ</h5>-->
    <!--      <p class="card-text">-->
    <!--        Lorem ipsum dolor sit amet, consectetur adipisicing elit.-->
    <!--        Dolorem est iusto laboriosam nulla quidem. Alias corporis cum-->
    <!--        quo tempore? Adipisci enim laboriosam nihil nobis omnis?-->
    <!--        Deleniti earum numquam quae repellat.-->
    <!--      </p>-->
    <!--    </div>-->
    <!--    <div class="card-body stat">-->
    <!--      <h5 class="card-title">СЛАБОСТИ</h5>-->
    <!--      <p class="card-text">-->
    <!--        Lorem ipsum dolor sit amet, consectetur adipisicing elit.-->
    <!--        Dolorem est iusto laboriosam nulla quidem. Alias corporis cum-->
    <!--        quo tempore? Adipisci enim laboriosam nihil nobis omnis?-->
    <!--        Deleniti earum numquam quae repellat.-->
    <!--      </p>-->
    <!--    </div>-->
  </div>
</template>

<script>
import BackgroundInfo from "../UI/BackgroundInfo.vue";

export default {
  components: {
    BackgroundInfo
  },
  name: "BackgroundView",

  data() {
    return {
      show: false,
    }
  },
  methods: {
    postSkills() {
      this.show = !this.show
    },
  }
}
</script>

<style scoped>

</style>