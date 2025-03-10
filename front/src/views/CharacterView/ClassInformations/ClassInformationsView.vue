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
        <th v-if="champion_class.levels[0].specific_columns.length>0">
          Дополнительные свойства
        </th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(levelData, index) in allLevelsWithAbilities" :key="index">
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
        <td v-if="champion_class.levels[0].specific_columns.length > 0">
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
    <div v-if="store.allAbilities.length > 0" class="ability-descriptions">
      <h3>Описание способностей</h3>
      <div
        v-for="ability in store.allAbilities"
        :key="ability.name"
        :id="`ability-${ability.name.toLowerCase().replace(/\s+/g, '-')}`"
      >
        <!-- Переключатель для оригинального описания -->
        <Switch
          class="ml-5"
          v-model="ability.custom_description.hide_original"
          @click="updateHideOriginal(ability)"
        />
        Скрыть оригинальное описание

        <!-- Переключатель для пользовательского описания -->
        <Switch
          class="ml-5"
          v-model="ability.custom_description.hide_custom"
          @click="updateHideCustomAbility(ability)"
        />
        Скрыть пользовательское описание

        <p>
          <strong>{{ ability.name }}</strong>
          <div class="inline-block"
               v-if="!ability.custom_description?.hide_custom">
            <button class="btn" @click="toggleEdit(ability)">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-pencil"
                viewBox="0 0 16 16"
              >
                <path
                  d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325"
                />
              </svg>
            </button>
          </div>
        </p>

        <!-- Оригинальное описание -->
        <div v-if="!ability.custom_description?.hide_original">
          {{ ability.description }}
        </div>

        <!-- Кастомное описание -->
        <div v-if="!ability.custom_description?.hide_custom">
          <div v-if="!ability.isEditing">
            {{ ability.custom_description.custom_description }}
          </div>
          <textarea
            v-else
            v-model="ability.custom_description.custom_description"
            rows="4"
            class="w-full border rounded p-2"
          ></textarea>
        </div>

        <div class="line"></div>
      </div>
    </div>
  </div>
</template>


<script setup>
import {computed} from "vue";
import {useClassInformationStore} from "@/stores/classStore.js";
import {Switch} from '@/components/ui/switch'

const store = useClassInformationStore();
const champion_class = computed(() => store.class_info);

const updateHideOriginal = (ability) => {
  store.updateHideOriginal(ability)

}

const updateHideCustomAbility = (ability) => {
  store.updateHideCustomAbility(ability)
}


const toggleEdit = (ability) => {
  // Если свойство isEditing отсутствует, добавляем его
  if (ability.isEditing === undefined) {
    ability.isEditing = false;
  }

  if (ability.isEditing) {
    // Если уже в режиме редактирования, отправляем данные на сервер
    updateCustomDescription(ability);
  } else {
    // Включаем режим редактирования
    ability.isEditing = true;
  }
};


const updateCustomDescription = async (ability) => {
  try {
    // Отправляем данные на сервер
    await store.updateCustomDescriptionOnServer(ability.custom_description);

    // Выключаем режим редактирования
    ability.isEditing = false;
  } catch (error) {
    console.error("Ошибка при обновлении описания:", error);
  }
};


const allLevelsWithAbilities = computed(() => {
  const levelsMap = new Map();

  // Добавляем уровни из основного класса
  champion_class.value.levels.forEach(level => {
    levelsMap.set(level.level, {
      ...level,
      abilities: [...(level.abilities || [])], // Копируем способности
    });
  });

  // Добавляем уровни из архетипов
  if (champion_class.value.archetypes && Array.isArray(champion_class.value.archetypes)) {
    champion_class.value.archetypes.forEach(archetype => {
      if (archetype.levels && Array.isArray(archetype.levels)) {
        archetype.levels.forEach(archetypeLevel => {
          if (levelsMap.has(archetypeLevel.level)) {
            // Если уровень уже существует, добавляем способности из архетипа
            const existingLevel = levelsMap.get(archetypeLevel.level);
            existingLevel.abilities.push(...(archetypeLevel.abilities || []));
          } else {
            // Если уровня нет, создаем новый
            levelsMap.set(archetypeLevel.level, {
              ...archetypeLevel,
              abilities: [...(archetypeLevel.abilities || [])],
            });
          }
        });
      }
    });
  }

  // Преобразуем Map обратно в массив и сортируем по уровню
  return Array.from(levelsMap.values()).sort((a, b) => a.level - b.level);
});
</script>
<style>
table {
  border-collapse: collapse;
  color: #212529;
}

.line {
  border-bottom: 1px solid #f00;
}

td,
th {
  border: 1px solid #dee2e6;
}

th {
  border-bottom: 2px solid #dee2e6;
}
</style>