<template>
  <div
    class="min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 text-white p-4"
  >
    <header class="max-w-4xl mx-auto mb-8">
      <h1 class="text-4xl font-bold text-yellow-400 mb-2">Лист Персонажа</h1>
      <p class="text-gray-400">Dungeons & Dragons 5th Edition</p>
    </header>

    <div
      class="max-w-4xl mx-auto bg-gray-800 rounded-lg shadow-2xl overflow-hidden"
    >
      <!-- Character Info Header -->
      <div class="bg-gray-900 p-6 border-b border-gray-700">
        <div
          class="flex flex-col md:flex-row md:justify-between md:items-center"
        >
          <div>
            <h2 class="text-3xl font-bold">{{ character.name }}</h2>
            <p class="text-gray-400">
              {{ character.class }} {{ character.level }} уровня |
              {{ character.race }}
            </p>
          </div>
          <div class="mt-4 md:mt-0">
            <div
              class="inline-block bg-yellow-900 text-yellow-200 px-4 py-2 rounded-lg font-medium"
            >
              {{ character.alignment }}
            </div>
          </div>
        </div>
      </div>

      <!-- Tabs Navigation -->
      <div class="flex border-b border-gray-700">
        <button
          v-for="(tab, index) in tabs"
          :key="index"
          @click="activeTab = tab.value"
          class="flex-1 py-3 text-center font-medium transition-colors"
          :class="{
            'border-b-2 border-yellow-500 text-yellow-400':
              activeTab === tab.value,
            'text-gray-400 hover:text-white': activeTab !== tab.value,
          }"
        >
          {{ tab.label }}
        </button>
      </div>

      <!-- Tab Content -->
      <div class="p-6">
        <!-- Character Overview -->
        <div
          v-if="activeTab === 'character'"
          class="grid grid-cols-1 md:grid-cols-2 gap-8"
        >
          <!-- Attributes -->
          <div>
            <h3 class="text-xl font-bold mb-4 text-yellow-400">
              Характеристики
            </h3>
            <div class="grid grid-cols-2 gap-4">
              <div
                v-for="(value, key) in character.attributes"
                :key="key"
                class="bg-gray-700 p-3 rounded-lg"
              >
                <div class="text-sm text-gray-400 capitalize">{{ key }}</div>
                <div class="text-2xl font-bold">{{ value }}</div>
                <div class="text-sm text-gray-500">
                  Модификатор: {{ Math.floor((value - 10) / 2) }}
                </div>
              </div>
            </div>
          </div>

          <!-- Basic Info -->
          <div>
            <h3 class="text-xl font-bold mb-4 text-yellow-400">
              Основная Информация
            </h3>
            <div class="space-y-3">
              <div>
                <span class="text-gray-400">Здоровье:</span>
                <span class="ml-2 font-mono"
                  >[{{ character.health.current }}/{{
                    character.health.max
                  }}]</span
                >
              </div>
              <div>
                <span class="text-gray-400">Класс брони:</span>
                <span class="ml-2">{{ character.armorClass }}</span>
              </div>
              <div>
                <span class="text-gray-400">Инициатива:</span>
                <span class="ml-2">{{ character.initiative }}</span>
              </div>
              <div>
                <span class="text-gray-400">Скорость:</span>
                <span class="ml-2">{{ character.speed }}</span>
              </div>
              <div>
                <span class="text-gray-400">Опыт:</span>
                <span class="ml-2 font-mono">{{ character.experience }}</span>
              </div>
            </div>
          </div>

          <!-- Skills -->
          <div>
            <h3 class="text-xl font-bold mb-4 text-yellow-400">Навыки</h3>
            <div class="grid grid-cols-2 gap-2">
              <div
                v-for="skill in character.skills"
                :key="skill"
                class="bg-gray-700 p-2 rounded text-sm"
              >
                {{ skill }}
              </div>
            </div>
          </div>

          <!-- Features -->
          <div>
            <h3 class="text-xl font-bold mb-4 text-yellow-400">Особенности</h3>
            <ul class="space-y-2 text-sm">
              <li
                v-for="feature in character.features"
                :key="feature"
                class="bg-gray-700 p-2 rounded"
              >
                {{ feature }}
              </li>
            </ul>
          </div>
        </div>

        <!-- Spells -->
        <div v-if="activeTab === 'spells'">
          <h3 class="text-2xl font-bold mb-4 text-yellow-400">
            Книга Заклинаний
          </h3>
          <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
            <div
              v-for="spell in character.spells"
              :key="spell"
              class="bg-gray-700 p-3 rounded-lg hover:bg-gray-600 transition-colors"
            >
              <h4 class="font-semibold">{{ spell }}</h4>
              <div class="text-xs text-gray-400 mt-1">
                Уровень {{ Math.floor(Math.random() * 4) + 1 }}
              </div>
            </div>
          </div>
        </div>

        <!-- Inventory -->
        <div v-if="activeTab === 'inventory'">
          <h3 class="text-2xl font-bold mb-4 text-yellow-400">Инвентарь</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
            <div
              v-for="item in character.inventory"
              :key="item"
              class="bg-gray-700 p-3 rounded-lg hover:bg-gray-600 transition-colors"
            >
              {{ item }}
            </div>
          </div>
        </div>

        <!-- Class -->
        <div v-if="activeTab === 'class'">
          <h3 class="text-2xl font-bold mb-4 text-yellow-400">
            Класс: {{ character.class }}
          </h3>
          <div class="prose prose-invert max-w-none">
            <p class="mb-4">
              Бард - это художник, чьи таланты включают в себя не только музыку,
              но и магию. Способность бардов влиять на мир через свои песни и
              заклинания делает их уникальными мастерами как боя, так и
              дипломатии.
            </p>
            <h4>Классовые особенности:</h4>
            <ul class="list-disc pl-5 space-y-1">
              <li>Бардовское вдохновение (3 раза/день)</li>
              <li>Магическое обучение</li>
              <li>Многосторонний талант</li>
              <li>Бардовский репертуар</li>
            </ul>
          </div>
        </div>

        <!-- Race -->
        <div v-if="activeTab === 'race'">
          <h3 class="text-2xl font-bold mb-4 text-yellow-400">
            Раса: {{ character.race }}
          </h3>
          <div class="prose prose-invert max-w-none">
            <p class="mb-4">
              Человеки - это универсальная раса, известная своей способностью
              адаптироваться к любым ситуациям. Они обладают равновесием
              характеристик и часто становятся лидерами в любом сообществе.
            </p>
            <h4>Расовые особенности:</h4>
            <ul class="list-disc pl-5 space-y-1">
              <li>Бонус +1 к двум любым характеристикам</li>
              <li>Бонус +1 к проверкам характеристик при выборе языка</li>
              <li>Дополнительный язык</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <footer class="max-w-4xl mx-auto mt-8 text-center text-gray-500 text-sm">
      <p>© 2023 D&D Character Sheet Viewer</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: 'character',
      tabs: [
        { label: 'Обзор', value: 'character' },
        { label: 'Заклинания', value: 'spells' },
        { label: 'Инвентарь', value: 'inventory' },
        { label: 'Класс', value: 'class' },
        { label: 'Раса', value: 'race' },
      ],
      character: {
        name: 'Гордон Громовой',
        class: 'Бард',
        level: 5,
        race: 'Человек',
        alignment: 'Законный добрый',
        background: 'Путешественник',
        experience: 4500,
        attributes: {
          strength: 14,
          dexterity: 16,
          constitution: 13,
          intelligence: 10,
          wisdom: 12,
          charisma: 18,
        },
        health: {
          current: 45,
          max: 45,
          temp: 0,
        },
        armorClass: 15,
        initiative: '+3',
        speed: '30 футов',
        skills: [
          'Акробатика',
          'Знание (история)',
          'Восприятие',
          'Обаяние',
          'Рукопашный бой',
        ],
        proficiencies: [
          'Большинство оружия',
          'Лёгкая броня',
          'Инструменты (лютня)',
          'Языки: Общий, Эльфийский',
        ],
        features: [
          'Бардовское вдохновение (3 раза/день)',
          'Магическое обучение',
          'Многосторонний талант',
        ],
        inventory: [
          'Меч-катана +1',
          'Лютня',
          'Кожанная броня',
          'Алмаз (2 шт.)',
          'Свиток огненного шара',
        ],
        spells: [
          'Свет',
          'Темная волна',
          'Телепортация',
          'Гипноз',
          'Огненный шар',
        ],
      },
    };
  },
};
</script>

<style>
/* Добавьте здесь дополнительные стили, если необходимо */
</style>
