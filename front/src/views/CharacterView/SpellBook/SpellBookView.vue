<template>
  <div class="spell-slots-container">
    <div v-for="(levelSlots, level) in spellSlots" :key="level"
         class="spell-level-section">
      <!-- Заголовок с кнопками слева и справа -->
      <div class="header">
        <div class="buttons-left">
          <button @click="addSlot(level)" class="add-button">+</button>
          <button @click="removeSlot(level)"
                  :disabled="spellSlots[level].count === 0"
                  class="remove-button">-
          </button>
        </div>
        <span class="level-title">Ячейки {{ level }}го уровня</span>
        <div class="buttons-right">
          <button @click="addSpellRow(level)" class="add-button">+</button>
          <button @click="removeSpellRow(level)"
                  :disabled="spellSlots[level].spells.length === 0"
                  class="remove-button">-
          </button>
        </div>
      </div>

      <!-- Отображение ячеек -->
      <div class="slots-display">
        <div
          v-for="(slot, index) in Array(spellSlots[level].count)"
          :key="index"
          class="slot"
          :class="{ used: isSlotUsed(level, index) }"
          @click="toggleSlotUsage(level, index)"
        ></div>
      </div>

      <!-- Список заклинаний -->
      <div class="spells-list">
        <div
          v-for="(spell, spellIndex) in spellSlots[level].spells"
          :key="spellIndex"
          class="spell-row"
        >
          <!-- Блок для отображения названия заклинания -->
          <div
            class="spell-block"
            @click="openSpellList(level, spellIndex)"
          >
            {{ spell.name || "Выберите заклинание" }}
          </div>

          <!-- Кнопка выбора заклинания -->
          <button
            class="select-spell-button"
            @click="openSpellList(level, spellIndex)"
          >
            Выбрать
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {reactive} from "vue";
// {
// "1":{"count":0,"spells":[{"name":"впиывпиып"},{"name":""},{"name":""},{"name":""}]},
// "2":{"count":0,"spells":[]},
// "3":{"count":0,"spells":[]}
// }


// тестовое хранение ячеек
const spellSlots = reactive({
  1: { count: 0, spells: [], used: 0 }, // Ячейки 1-го уровня: count - общее количество, used - использованное
  2: { count: 0, spells: [], used: 0 }, // Ячейки 2-го уровня
  3: { count: 0, spells: [], used: 0 }, // Ячейки 3-го уровня
});

// Метод для добавления ячейки
function addSlot(level) {
  spellSlots[level].count += 1;
}

// Метод для удаления ячейки
function removeSlot(level) {
  if (spellSlots[level].count > 0) {
    spellSlots[level].count -= 1;
  }
}

// Метод для добавления заклинания
function addSpellRow(level) {
  spellSlots[level].spells.push({name: ""});
}

// Метод для удаления строки заклинания
function removeSpellRow(level) {
  if (spellSlots[level].spells.length > 0) {
    spellSlots[level].spells.pop();
  }
}

// Метод для открытия списка заклинаний
function openSpellList(level, spellIndex) {
  console.log(`Открываем список заклинаний для уровня ${level}, строка ${spellIndex}`);
  // Здесь вы можете добавить логику открытия списка заклинаний
}

// Метод для проверки использования конкретной ячейки
function isSlotUsed(level, index) {
  return index < spellSlots[level].used;
}

// Метод для переключения состояния использования ячейки
function toggleSlotUsage(level, index) {
  const currentUsed = spellSlots[level].used;

  if (index < currentUsed) {
    // Если кликнули на уже использованную ячейку, уменьшаем счетчик used
    spellSlots[level].used = Math.max(0, currentUsed - 1);
  } else if (index < spellSlots[level].count) {
    // Если кликнули на свободную ячейку, увеличиваем счетчик used
    spellSlots[level].used = Math.min(spellSlots[level].count, currentUsed + 1);
  }
}
</script>

<style scoped>

.slot.used {
  background-color: #ff5722; /* Оранжевый цвет для использованных ячеек */
}

.spell-slots-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.spell-level-section {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  width: 400px;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 8px;
}

.buttons-left,
.buttons-right {
  display: flex;
  gap: 5px;
}

.level-title {
  font-weight: bold;
  font-size: 16px;
}

.add-button,
.remove-button {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 3px;
}

.remove-button {
  background-color: #f44336;
}

.remove-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.slots-display {
  display: flex;
  gap: 5px;
  margin-top: 8px;
}

.slot {
  width: 20px;
  height: 20px;
  background-color: #2196f3;
  border: 1px solid #000;
  border-radius: 3px;
}

.spells-list {
  margin-top: 10px;
  width: 100%;
}

.spell-row {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
}

.spell-block {
  flex: 1;
  padding: 5px 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  background-color: #f9f9f9;
  text-align: center;
  cursor: pointer;
  user-select: none;
}

.spell-block:hover {
  background-color: #eaeaea;
}

.select-spell-button {
  margin-left: 10px;
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.select-spell-button:hover {
  background-color: #0056b3;
}
</style>