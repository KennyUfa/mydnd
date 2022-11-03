<template>
  <div class="container-fluid">
    <div class="row">
      <div class="player-name col-md-3">
        <p class="info">Имя персонажа</p>
        <p class="info">{{ name_champion }}</p>
      </div>
      <div class="col-md-9">
        <div class="row">
          <div class="div col player-info p-1">
            <p>Класс - {{ class_name }}</p>
          </div>
          <div class="div col player-info p-1">
            <p>предистория - {{ pre_history }}</p>
          </div>
          <div class="div col player-info p-1">
            <p>Имя игрока - {{ account }}</p></div>
        </div>
        <div class="row">
          <div class="col player-info p-1"><p>
            Расса - {{ race }}
          </p></div>
          <div class="col player-info p-1">
            <p>Мировозрение
              - {{ world_outlook }}</p>
          </div>
          <div class="col player-info p-1"><p>Опыт
            - {{ experience }}</p></div>
          <div class="col player-info p-1">
            <div id="row counter">
              <button @click="plus"
                      :disabled="$data.lvl>19">+</button>

              <div id="buttonCountNumber">{{ lvl }}</div>
              <button @click="minus"
              :disabled="$data.lvl<2">-</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",

  data() {
    return {
      name_champion: 'defaultt',
      class_name: 'defaultt',
      pre_history: 'defaultt',
      race: 'defaultt',
      world_outlook: 'defaultt',
      account: 'defaultt',
      experience: 'defaultt',
      lvl: 1,
    };
  },
  methods: {
    plus () {
      this.lvl += 1
    },
    minus () {
      this.lvl -= 1
    },
    decrement () {
      if (this.lvl === 20) return
      this.lvl -= 1
    }
  }
};

</script>
