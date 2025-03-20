<template>
  <div class="card" style="">
    <div class="card-body">
      <h5 class="card-title">{{ champion_class.name }}</h5>
      <DropdownMenu>
        <DropdownMenuTrigger v-on:click="loadArchetypes">
          <Button variant="outline">
            {{ archetype?.name || 'Выбрать архетип' }}
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent>
          <DropdownMenuLabel>
            {{ archetype?.name || 'Выбрать архетип' }}
          </DropdownMenuLabel>
          <DropdownMenuSeparator/>
          <DropdownMenuItem
            v-for="arch in archetype_list"
            :key="arch.id"
            @click="changeArchetype(arch)">
            {{ arch.name }} <!-- Отображаем имя архетипа -->
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
      <p class="card-text">{{
          champion_class.description
        }}</p>
    </div>
    <div class="card-body" v-if="archetype">
      <h5 class="card-title">{{ archetype.name }}</h5>
      <p class="card-text">{{
          archetype.description
        }}</p>
    </div>

    <!--таблица способностей-->
    <table class="class-table">
      <thead>
      <tr>
        <!-- Общие столбцы -->
        <th>Уровень</th>
        <th>Бонус мастерства</th>
        <th>Способности</th>

        <!-- Динамические столбцы для specific_columns -->
        <th v-for="(specificColumn, index) in champion_class.specific_columns"
            :key="'specific-column-' + index">
          {{ specificColumn.name }}
        </th>
        <th v-for="(specificColumn, index) in
        archetype?.specific_columns"
            :key="'specific-column-' + index">
          {{ specificColumn.name }}
        </th>
        <th v-if="archetype?.spell_slots?.length > 0" v-for="(slotLevel,
        index) in archetype.spell_slots[0].slots"
            :key="'header-' + index"
        >
          Ячейки заклинаний ({{ index }})
        </th>
        <th v-if="champion_class?.spell_slots?.length > 0" v-for="(slotLevel,
        index) in champion_class.spell_slots[0].slots"
            :key="'header-' + index"
        >
          Ячейки заклинаний ({{ index }})
        </th>
      </tr>


      </thead>
      <tbody>
      <tr v-for="(levelData, index) in allLevelsWithAbilities" :key="index">
        <!-- Уровень -->
        <td>{{ levelData.level }}</td>

        <!-- Бонус мастерства -->
        <td>+{{ levelData.proficiency_bonus }}</td>

        <!-- Способности -->
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

        <!-- Значения для specific_columns -->
        <td
          v-for="(specificColumn, colIndex) in champion_class.specific_columns"
          :key="'specific-column-value-' + colIndex">
          {{ specificColumn.value[index] }}
        </td>
        <td
          v-if="archetype?.specific_columns?.length > 0"
          v-for="(specificColumn, colIndex) in archetype.specific_columns"
          :key="'specific-column-value-' + colIndex">
          {{ specificColumn.value[index] }}
        </td>
        <td v-if="archetype?.spell_slots?.length > 0"
            v-for="i in (archetype.spell_slots[0].slots)">
          {{ i[index + 1] }}
        </td>
        <td v-if="champion_class?.spell_slots?.length > 0"
            v-for="i in (champion_class.spell_slots[0].slots)">
          {{ i[index + 1] }}
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
          <div v-if="!ability.custom_description?.isEditing">
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
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import {Button} from '@/components/ui/button';

const store = useClassInformationStore();
const champion_class = computed(() => store.class_info);
const archetype = computed(() => store.archetype);
const archetype_list = computed(() => store.archetype_list);

const updateHideOriginal = (ability) => {
  store.updateHideOriginal(ability)

}

const updateHideCustomAbility = (ability) => {
  store.updateHideCustomAbility(ability)
}


const toggleEdit = (ability) => {
  if (ability.custom_description.isEditing) {
    // Если уже в режиме редактирования, отправляем данные на сервер
    updateCustomDescription(ability);
    ability.custom_description.isEditing = false;
  } else {
    // Включаем режим редактирования
    ability.custom_description.isEditing = true;
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
  if (champion_class.value.levels) {
    champion_class.value.levels.forEach(level => {
      levelsMap.set(level.level, {
        ...level,
        abilities: [...(level.abilities || [])], // Копируем способности
      });
    });
  }

  // Добавляем уровни из архетипа
  if (archetype.value?.levels) {
    archetype.value.levels.forEach(level => {
      if (levelsMap.has(level.level)) {
        // Если уровень уже существует, добавляем способности из архетипа
        const existingLevel = levelsMap.get(level.level);
        existingLevel.abilities.push(...(level.abilities || []));
      } else {
        // Если уровня нет, создаем новую запись
        levelsMap.set(level.level, {
          ...level,
          abilities: [...(level.abilities || [])],
        });
      }
    });
  }

  // Преобразуем Map обратно в массив и сортируем по уровню
  return Array.from(levelsMap.values()).sort((a, b) => a.level - b.level);
});

const loadArchetypes = () => {
  store.loadArchetypes()
}
const changeArchetype = (id) => {
  store.changeArchetype(id)
}
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