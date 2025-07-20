<template>
<div class="rounded-2xl px-1">
    <div
      class="grid grid-cols-3 md:grid-cols-7 border-b border-gray-700 bg-gray-900 ">
      <button
        v-for="(tab, index) in tabs"
        :key="index"
        @click="activeTab = tab.value"
        class="flex-1 py-2 text-center font-medium transition-colors md:py-3"
        :class="{
            'border-b-2 border-yellow-500 text-yellow-400':
              activeTab === tab.value,
            'text-gray-400 hover:text-white': activeTab !== tab.value,
          }"
      >
        {{ tab.label }}
      </button>
    </div>

    <!--    основная информация   -->
    <div v-if="activeTab === 'character'">
      <h3 class="text-2xl font-bold mb-4  bg-gray-800">
        <MainInformation></MainInformation>
        <hit-view></hit-view>
        <inform></inform>

        <saving-throw-view
          @callRandomWindow="callRandomWindowMethod"
        ></saving-throw-view>
        <ability-view
          @callRandomWindow="callRandomWindowMethod"></ability-view>
      </h3>
    </div>

    <!--    книга заклинаний   -->
    <div v-if="activeTab === 'spells'">
      <h3 class="text-2xl font-bold mb-4 text-yellow-400">
        Книга Заклинаний
      </h3>
      <spell-book-view></spell-book-view>
    </div>

    <!--    класс и уровень   -->
    <div v-if="activeTab === 'class-information'">
      <h3 class="text-2xl font-bold mb-4 text-yellow-400">
        Класс
      </h3>
      <class-information-view></class-information-view>
    </div>


    <!-- раса -->
    <div v-if="activeTab === 'race'">
      <h3 class="text-2xl font-bold mb-4 text-yellow-400">
        Раса
      </h3>
      <race-and-origin></race-and-origin>
    </div>

    <!--    предыстория    -->

    <div v-if="activeTab === 'background'">
      <h3 class="text-2xl font-bold mb-4 text-yellow-400">
        Предыстория
      </h3>
      <background-view></background-view>
    </div>
    <!--    база предметов    -->
    <div v-if="activeTab === 'item-list'">
      <h3 class="text-2xl font-bold mb-4 text-yellow-400">
        База предметов
      </h3>
      <ItemsView></ItemsView>
    </div>

    <!--    инвентарь  -->

    <div v-if="activeTab === 'inventory'">
      <h3 class="text-2xl font-bold mb-4 text-yellow-400">
        Инвентарь
      </h3>
      <InventoryView></InventoryView>
    </div>
  </div>
  <!--  кубы  -->
  <DropdownMenu>
    <DropdownMenuTrigger>
      <Button
        variant="outline"
        class="fixed bottom-0 w-16 h-16 rounded-lg mb-2"
      >
        <img src="@/assets/152068.svg" alt="Куб" class="w-10 h-10"/>
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent class="relative w-1 ml-2">
      <DropdownMenuLabel
        class="bg-green-500 rounded-xl"
        v-if="rollStatus"
        @click="roll"
      >Бросить кубы
      </DropdownMenuLabel>
      <DropdownMenuSeparator/>
      <DropdownMenuGroup>
        <DropdownMenuItem>
          <div @click.stop="d4 += 1" class="w-full">D4</div>
          <DropdownMenuShortcut>{{ d4 }}</DropdownMenuShortcut>
        </DropdownMenuItem>
        <DropdownMenuItem>
          <div @click.stop="d6 += 1" class="w-full">D6</div>
          <DropdownMenuShortcut>{{ d6 }}</DropdownMenuShortcut>
        </DropdownMenuItem>
        <DropdownMenuItem>
          <div @click.stop="d8 += 1" class="w-full">D8</div>
          <DropdownMenuShortcut>{{ d8 }}</DropdownMenuShortcut>
        </DropdownMenuItem>
        <DropdownMenuItem>
          <div @click.stop="d10 += 1" class="w-full">D10</div>
          <DropdownMenuShortcut>{{ d10 }}</DropdownMenuShortcut>
        </DropdownMenuItem>
        <DropdownMenuItem>
          <div @click.stop="d12 += 1" class="w-full">D12</div>
          <DropdownMenuShortcut>{{ d12 }}</DropdownMenuShortcut>
        </DropdownMenuItem>
        <DropdownMenuItem>
          <div @click.stop="d20 += 1" class="w-full">D20</div>
          <DropdownMenuShortcut>{{ d20 }}</DropdownMenuShortcut>
        </DropdownMenuItem>
        <DropdownMenuSeparator/>
      </DropdownMenuGroup>
    </DropdownMenuContent>
  </DropdownMenu>
</template>

<script setup>
import MainInformation
  from '@/views/CharacterView/MainInformations/MainInformation.vue';
import ClassInformationView
  from '@/views/CharacterView/ClassInformations/ClassInformationsView.vue';
import AbilityView from '@/views/CharacterView/Skills/АbilityView.vue';
import BackgroundView
  from '@/views/CharacterView/Background/BackgroundView.vue';
import SavingThrowView from '@/views/CharacterView/Skills/SavingThrowView.vue';
import RaceAndOrigin
  from '@/views/CharacterView/RaceAndOrigin/RaceAndOrigin.vue';
import ItemsView from '@/views/CharacterView/Inventory/ItemsView.vue';
import {useToast} from '@/components/ui/toast/use-toast';
import {h, ref, watch} from 'vue';
import ToastContent from '@/views/ToastContent.vue';
import InventoryView from '@/views/CharacterView/Inventory/InventoryView.vue';
import SpellBookView from '@/views/CharacterView/SpellBook/SpellBookView.vue';
import Inform from '@/views/CharacterView/CharacterInfo/Inform.vue';
import HitView from '@/views/CharacterView/HitView/HitVue.vue';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu/index.js';
import {Button} from '@/components/ui/button/index.js';
import {useCharacterStore} from '@/stores/characterStore.js';
import RandomContent from '@/views/RandomContent.vue';

const {toast} = useToast();

// Метод для показа тоста
const callRandomWindowMethod = (responseData) => {
  toast({
    class: '',
    title: 'Бросок кубиков!',
    description: h(ToastContent, {data: responseData}),
  });
};

const champion = useCharacterStore();

const rollStatus = ref(false);
const d6 = ref(0);
const d4 = ref(0);
const d8 = ref(0);
const d10 = ref(0);
const d12 = ref(0);
const d20 = ref(0);

watch([d4, d6, d8, d10, d12, d20], () => {
  rollStatus.value = true;
});

const roll = () => {
  champion
    .rollDice(d4.value, d6.value, d8.value, d10.value, d12.value, d20.value)
    .then((result) => {
      toast({
        title: 'Бросок кубиков!',
        description: h(RandomContent, {
          result: result,
        }),
      });
      d6.value = 0;
      d4.value = 0;
      d8.value = 0;
      d10.value = 0;
      d12.value = 0;
      d20.value = 0;
      rollStatus.value = false;
    });
};


const activeTab = ref('character');
const tabs = [
  {label: 'Главная', value: 'character'},
  {label: 'Заклинания', value: 'spells'},
  {label: 'Класс', value: 'class-information'},
  {label: 'Раса', value: 'race'},
  {label: 'Предыстория', value: 'background'},
  {label: 'База предметов', value: 'item-list'},
  {label: 'Инвентарь', value: 'inventory'},
];
</script>
