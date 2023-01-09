<template>
  <div class="row">
    <div class="player-name col-md-3">
      <p class="info">Имя персонажа</p>
      <p class="info">
        {{ $store.state.champion.listInfo.name_champion }}
      </p>

    </div>
    <div class="col-md-9">
      <div class="row">
        <div class="div col player-info p-1">
          <p>Класс - {{ $store.state.champion.listInfo.champion_class }}</p>
        </div>
        <div class="div col player-info p-1">
          <p>
            предистория - {{ $store.state.champion.listInfo.pre_history }}
          </p>
        </div>
        <div class="div col player-info p-1">
          <p>Имя игрока - {{ $store.state.auth.user.name }}</p>
        </div>
      </div>
      <div class="row">
        <div class="col player-info p-1">
          <p>Расса - {{ $store.state.champion.listInfo.race }}</p>
        </div>
        <div class="col player-info p-1">
          <p>
            Мировозрение - {{ $store.state.champion.listInfo.world_outlook }}
          </p>
        </div>
        <div class="col player-info p-1">
          <p>Опыт - {{ $store.state.champion.listInfo.experience }}</p>
        </div>
        <div class="col player-info p-1">
          <div id="row counter">
            <div id="buttonCountNumber" class="col">
              {{ $store.state.champion.listInfo.lvl }}
            </div>
            <button
                class="col"
                @click="$store.state.champion.listInfo.lvl++"
                :disabled="$store.state.champion.listInfo.lvl > 19"
            >
              +
            </button>
            <button
                class="col"
                @click="$store.state.champion.listInfo.lvl--"
                :disabled="$store.state.champion.listInfo.lvl < 2"
            >
              -
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainInfoView"
}
</script>

<style scoped>

</style>