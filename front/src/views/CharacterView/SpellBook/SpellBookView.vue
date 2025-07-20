<template>
  <div class="spell-slots-container">
    <div
      v-for="levelSlots in spell_slots.slot_levels"
      :key="levelSlots.id"
      class="spell-level-section"
    >
      <!--     Кнопки добавления ячеек-->
      <div class="header">
        <div class="buttons-left">
          <button @click="addSlot(levelSlots)" class="add-button">+</button>
          <button
            @click="removeSlot(levelSlots)"
            :disabled="levelSlots.spell_slot_level.count === 0"
            class="remove-button"
          >
            -
          </button>
        </div>
        <span class="level-title" v-if="levelSlots.spell_slot_level.level === 0"
          >Фокусы</span
        >
        <span class="level-title" v-else
          >Ячейки {{ levelSlots.spell_slot_level.level }}го уровня</span
        >
      </div>

      <!-- Отображение ячеек -->
      <div class="slots-display">
        <div
          v-for="(slot, index) in Array(levelSlots.spell_slot_level.count)"
          :key="index"
          class="slot"
          :class="{ used: isSlotUsed(levelSlots, index) }"
          @click="toggleSlotUsage(levelSlots, index)"
        ></div>
      </div>

      <!-- Список заклинаний -->
      <div class="spells-list">
        <div
          v-for="(spell, spellIndex) in levelSlots.spells"
          :key="spellIndex"
          class="spell-row"
        >
          <Dialog>
            <DialogTrigger class="spell-block" as-child>
              <Button
                variant="outline "
                class="text-balance"
                @click="getSpellDetails(spell)"
              >
                {{ spell.name }}
              </Button>
            </DialogTrigger>
            <DialogContent class="overflow-y-auto max-h-[80vh]">
              <DialogHeader v-if="spell_details">
                <DialogTitle
                  >{{ spell_details.name }} - Уровень:
                  {{ spell_details.level }}
                </DialogTitle>
                <DialogDescription>
                  <div>{{ spell_details.class_actor }}</div>
                  <div>{{ spell_details.archetype }}</div>
                  <div>{{ spell_details.school }}</div>
                  <div>{{ spell_details.timing }}</div>
                  <div>{{ spell_details.instruction }}</div>
                </DialogDescription>
              </DialogHeader>
            </DialogContent>
          </Dialog>

          <button
            @click="removeSpell(levelSlots, spellIndex, spell.id)"
            :disabled="levelSlots.spells.length === 0"
            class="remove-button"
          >
            Х
          </button>
        </div>
        <change-spell
          :level_slots="levelSlots.spell_slot_level.level"
        ></change-spell>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useSpellBook } from '@/stores/SpellBookStore.js';
import { computed, onMounted, ref } from 'vue';
import ChangeSpell from '@/views/CharacterView/SpellBook/ChangeSpell.vue';
import { useCreateCharacter } from '@/stores/create.character.js';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog/index.js';
import { Button } from '@/components/ui/button/index.js';

const polling = ref(null);
const spellBook = useSpellBook();
const spell_slots = computed(() => spellBook.my_spellbook);
const spell_details = computed(() => spellBook.spell_details);
const create_character = useCreateCharacter();

// Метод для добавления ячейки
function addSlot(levelSlots) {
  levelSlots.spell_slot_level.count += 1;
  patchSlots(levelSlots.spell_slot_level);
}

// Метод для удаления ячейки
function removeSlot(levelSlots) {
  if (levelSlots.spell_slot_level.count > 0) {
    levelSlots.spell_slot_level.count -= 1;
  }
  patchSlots(levelSlots.spell_slot_level);
}

const patchSlots = (levelSlot) => {
  destroyInterval();
  createTimer(levelSlot);
};
const destroyInterval = () => {
  if (polling.value) {
    clearInterval(polling.value);
  }
};
const createTimer = (levelSlot) => {
  pollData(levelSlot);
};

const pollData = (levelSlot) => {
  polling.value = setTimeout(() => {
    spellBook.patchLevelSlots(levelSlot);
  }, 2000);
};

function getSpellDetails(spell) {
  spellBook.getSpellDetails(spell.id);
}

// Метод для удаления строки заклинания
function removeSpell(levelSlots, spellIndex, spell_id) {
  levelSlots.spells.splice(spellIndex, 1);
  spellBook.removeSpell(levelSlots.spell_slot_level, spellIndex, spell_id);
}

// Метод для проверки использования конкретной ячейки
function isSlotUsed(levelSlots, index) {
  return index < levelSlots.spell_slot_level.used;
}

// Метод для переключения состояния использования ячейки
function toggleSlotUsage(levelSlots, index) {
  const currentUsed = levelSlots.spell_slot_level.used;
  if (index < currentUsed) {
    // Если кликнули на уже использованную ячейку, уменьшаем счетчик used
    levelSlots.spell_slot_level.used = Math.max(0, currentUsed - 1);
  } else if (index < levelSlots.spell_slot_level.count) {
    // Если кликнули на свободную ячейку, увеличиваем счетчик used
    levelSlots.spell_slot_level.used = Math.min(
      levelSlots.spell_slot_level.count,
      currentUsed + 1
    );
  }
  patchSlots(levelSlots.spell_slot_level);
}

onMounted(() => {
  if (create_character.class_list.length === 0) {
    create_character.fetchClassList();
  }
});
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
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.buttons-left {
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
</style>
