<template>
  <div class="card" style="">
    <div class="card-body">
      <h5 class="card-title">{{ champion_class.name }}</h5>
      <p class="card-text">{{
          champion_class.description
        }}</p>
    </div>
    <table class="class-table">
      <thead>
      <tr>
        <th>Уровень</th>
        <th>Бонус мастерства</th>
        <th>Способности</th>
        <th>Дополнительные свойства</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(levelData, index) in champion_class.levels" :key="index">
        <td>{{ levelData.level }}</td>
        <td>+{{ levelData.proficiency_bonus }}</td>
        <td>
          <ul>
            <li v-for="ability in levelData.abilities" :key="ability.name">
              <!-- Якорная ссылка на описание способности -->
              <a
                :href="`#ability-${ability.name.toLowerCase().replace(/\s+/g, '-')}`">
                {{ ability.name }}
              </a>
            </li>
          </ul>
        </td>
        <td>
          <ul>
            <li v-for="column in levelData.specific_columns" :key="column.name">
              {{ column.name }}: {{ column.value }}
            </li>
          </ul>
        </td>
      </tr>
      </tbody>
    </table>
    <!-- Описание способностей -->
    <div v-if="allAbilities.length > 0" class="ability-descriptions">
      <h3>Описание способностей</h3>
      <div
        v-for="ability in allAbilities"
        :key="ability.name"
        :id="`ability-${ability.name.toLowerCase().replace(/\s+/g, '-')}`"
      >
        <h4>{{ ability.name }}</h4>
        <label>
          <input
            type="checkbox"
            v-model="ability.custom_description.hide_original"
            @change="updateHideOriginal(ability)"
          />
          Скрыть оригинальное описание
        </label>
        <label>
          <input
            type="checkbox"
            v-model="ability.custom_description.hide_custom"
            @change="updateHideCustomAbility(ability)"
          />
          Скрыть пользовательское описание
        </label>
        <!-- Оригинальное описание -->
        <p v-if="!ability.custom_description?.hide_original">
          {{ ability.description }}
        </p>
        <!-- Кастомное описание -->
        <p v-if="!ability.custom_description?.hide_custom">
          {{ ability.custom_description.custom_description }}
        </p>
      </div>
    </div>
  </div>
</template>


<script>
import {mapGetters} from "vuex";

export default {

  name: "ClassInformationView",
  computed: {
    ...mapGetters('champion', ['getChampionClass']),
    champion_class() {
      return this.getChampionClass;
    },
    allAbilities() {
      const abilitiesMap = new Map(); // Используем Map для уникальности
      this.champion_class.levels.forEach(level => {
        level.abilities.forEach(ability => {
          if (!abilitiesMap.has(ability.name)) {
            abilitiesMap.set(ability.name, ability);
          }
        });
      });
      return Array.from(abilitiesMap.values());
    },
  },
  methods: {
    async updateHideOriginal(ability) {
      try {
        await this.$store.dispatch('champion/updateHideOriginal', {
          ability
        });
      } catch (error) {
        console.error("Ошибка при обновлении данных updateHideOriginal:", error);
      }
    },
    async updateHideCustomAbility(ability) {
      try {
        await this.$store.dispatch('champion/updateHideCustomAbility', {
          ability
        });
      } catch (error) {
        console.error("Ошибка при обновлении данных updateHideCustomAbility:", error);
      }
    }
  },
};

</script>
<style scoped>
table {
  border-collapse: collapse;

  color: #212529;
}

td,
th {
  border: 1px solid #dee2e6;
}

th {
  border-bottom: 2px solid #dee2e6;
}
</style>