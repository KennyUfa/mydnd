<template>
  <div class="container-fluid">
    <div class="user_login" v-if="auth">{{ this.login }}</div>

    <div class="user_login" v-if="auth">
      <input v-model="login" type="text" placeholder="Логин"/>
      <input v-model="password" type="password" placeholder="Пароль"/>
      <button @click="setLogin">Войти</button>
    </div>
    <button @click="getInfo">test</button>
    <div class="row">
      <div class="player-name col-md-3">
        <p class="info">Имя персонажа</p>
        <p class="info"><input
            v-model="data_champion.name_champion"></p>
      </div>
      <div class="col-md-9">
        <div class="row">
          <div class="div col player-info p-1">
            <p>Класс - {{ data_champion.champion_class }}</p>
          </div>
          <div class="div col player-info p-1">
            <p>предистория - {{ data_champion.pre_history }}</p>
          </div>
          <div class="div col player-info p-1">
            <p>Имя игрока - {{ data_champion.account }}</p></div>
        </div>
        <div class="row">
          <div class="col player-info p-1"><p>
            Расса - {{ data_champion.race }}
          </p></div>
          <div class="col player-info p-1">
            <p>Мировозрение
              - {{ data_champion.world_outlook }}</p>
          </div>
          <div class="col player-info p-1"><p>Опыт
            - {{ data_champion.experience }}</p></div>
          <div class="col player-info p-1">
            <div id="row counter">
              <button @click="data_champion.lvl++"
                      :disabled="data_champion.lvl>19">+
              </button>

              <div id="buttonCountNumber">{{ data_champion.lvl }}</div>
              <button @click="data_champion.lvl--"
                      :disabled="data_champion.lvl<2">-
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
      login: '',
      password: '',
      data_champion: {
        name_champion: 'default',
        champion_class: 'default',
        re_history: 'default',
        race: 'default',
        world_outlook: 'default',
        account: 'default',
        experience: 'default',
        lvl: 1,
      },
    }
  },
  computed: {
    auth() {
      if (localStorage.getItem("Bearer")) {
        return true
      }
    }
  }
  ,
  methods: {
    async getInfo() {
      const token = localStorage.getItem('Bearer');

      const res = await fetch('http://127.0.0.1:8000/dnd/character/', {
        method: 'GET',
        headers: {
          'Content-type': 'application/json',
          'Authorization': `Bearer ${token}`, // notice the Bearer before your token
        }
      });
      this.data_champion = await res.json();
    },
    reLogin() {
      fetch("http://127.0.0.1:8000/api/token/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          username: this.login,
          password: this.password,
        }),
      })
    },
    setLogin() {
      fetch("http://127.0.0.1:8000/api/token/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          username: this.login,
          password: this.password,
        }),
      })
          .then(response => response.json())
          .then(response => localStorage.setItem('Bearer', response.access));
    }
  },

  mounted() {
    this.getInfo();
  }

}
</script>
