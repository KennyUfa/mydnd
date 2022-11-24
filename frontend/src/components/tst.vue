<div class="user_login" v-if="auth">{{ this.login }}</div>
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