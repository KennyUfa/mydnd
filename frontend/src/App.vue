<template>
  <div class="container-fluid">
    <button @click="getInfo">test</button>
    <div class="row">
      <div class="player-name col-md-3">
        <p class="info">Имя персонажа</p>
        <p class="info"><input
        v-model="name_champion"></p>
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
                      :disabled="$data.lvl>19">+
              </button>

              <div id="buttonCountNumber">{{ lvl }}</div>
              <button @click="minus"
                      :disabled="$data.lvl<2">-
              </button>
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
      experience: 'default',
      lvl: 1,
    };
  },
  methods: {
    getInfo() {
      fetch('http://127.0.0.1:8000/users/')
          .then(Response => Response.json())
          // .then(datajson => console.log(datajson[0].username))
          .then(datajson => this.name_champion = datajson[0].username)
    },
  }
};

</script>
