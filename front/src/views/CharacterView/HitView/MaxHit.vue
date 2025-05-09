<template>
    <AlertDialog>
        <AlertDialogTrigger as-child>
            <button class="absolute right-1 top-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none"
                     viewBox="0 0 24 24" stroke-width="1.5"
                     stroke="currentColor" class="size-5">
                    <path stroke-linecap="round" stroke-linejoin="round"
                          d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125"/>
                </svg>
            </button>
        </AlertDialogTrigger>
        <AlertDialogContent class="max-w-96">
            <AlertDialogHeader>
                <AlertDialogTitle
                        class="font-bold uppercase italic">Изменение
                    максимального значения здоровья
                </AlertDialogTitle>
                <AlertDialogDescription
                        class="flex flex-row items-center justify-between">

                    <Badge @click="incrementMaxHit(1)"
                           class="border-2 rounded-md w-30 h-30">
                        +1
                    </Badge>
                    <Badge @click="incrementMaxHit(10)"
                           class="border-2 rounded-md w-30 h-30">
                        +10
                    </Badge>
                    <Badge @click="incrementMaxHit(100)"
                           class="border-2 rounded-md w-30 h-30">
                        +100
                    </Badge>
                    <div class="p-2 border-3 ">
                        {{ tempMaxHit }}
                    </div>

                    <Badge @click="decrementMaxHit(1)"
                           :disabled="tempMaxHit < 1"
                           class="border-2 rounded-md w-30 h-30">
                        -1
                    </Badge>

                    <Badge @click="decrementMaxHit(10)"
                           class="border-2 rounded-md w-30 h-30">
                        -10
                    </Badge>
                    <Badge @click="decrementMaxHit(100)"
                           class="border-2 rounded-md w-30 h-30">
                        -100
                    </Badge>
                </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogHeader>
                <AlertDialogTitle
                        class="font-bold uppercase italic">Изменение
                    временного значения здоровья
                </AlertDialogTitle>
                <AlertDialogDescription
                        class="flex flex-row items-center justify-between">

                    <Badge @click="incrementTempHit(1)"
                           class="border-2 rounded-md w-30 h-30">
                        +1
                    </Badge>
                    <Badge @click="incrementTempHit(10)"
                           class="border-2 rounded-md w-30 h-30">
                        +10
                    </Badge>
                    <Badge @click="incrementTempHit(100)"
                           class="border-2 rounded-md w-30 h-30">
                        +100
                    </Badge>
                    <div class="p-2 border-3 ">
                        {{ tempTempHit }}
                    </div>

                    <Badge @click="decrementTempHit(1)"
                           :disabled="tempMaxHit < 1"
                           class="border-2 rounded-md w-30 h-30">
                        -1
                    </Badge>

                    <Badge @click="decrementTempHit(10)"
                           class="border-2 rounded-md w-30 h-30">
                        -10
                    </Badge>
                    <Badge @click="decrementTempHit(100)"
                           class="border-2 rounded-md w-30 h-30">
                        -100
                    </Badge>
                </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogAction @click="applyChanges()">Изменить
                </AlertDialogAction>
                <AlertDialogCancel @click="cancelChanges()">Отмена
                </AlertDialogCancel>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>
</template>

<script setup>

import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
    AlertDialogTrigger
} from "@/components/ui/alert-dialog/index.js";
import {Button} from "@/components/ui/button/index.js";
import {computed, ref} from "vue";
import {useCharacterStore} from "@/stores/characterStore.js";
import {Badge} from "@/components/ui/badge/index.js";

const store = useCharacterStore();
const character = computed(() => store.character);

// Изначальное максимальное значение здоровья, используется для отмены изменений
const originalMaxHit = ref(character.value.max_hit);
const tempMaxHit = ref(character.value.max_hit);


const originalTempHit = ref(character.value.temp_hit);
const tempTempHit = ref(character.value.temp_hit);

// Увеличение значения
const incrementMaxHit = (amount) => {
    tempMaxHit.value += amount;
};


const incrementTempHit = (amount) => {
    tempTempHit.value += amount;
};
// Применение изменений
const applyChanges = () => {
    character.value.max_hit = tempMaxHit.value; // Применяем новое значение
    character.value.temp_hit = tempTempHit.value; // Применяем новое значение
    store.updateCharacterHit(character.value.max_hit, character.value.temp_hit);
    resetDialog(); // Сбрасываем диалог
};

// Уменьшение значения
const decrementMaxHit = (amount) => {
    if (tempMaxHit.value - amount >= 0) {
        tempMaxHit.value -= amount;
    } else {
        tempMaxHit.value = 0;
    }
};

const decrementTempHit = (amount) => {
    if (tempTempHit.value - amount >= 0) {
        tempTempHit.value -= amount;
    } else {
        tempTempHit.value = 0;
    }
};
// Отмена изменений
const cancelChanges = () => {
    tempMaxHit.value = originalMaxHit.value; // Восстанавливаем исходное значение
    tempTempHit.value = originalTempHit.value; // Восстанавливаем исходное значение
    resetDialog(); // Сбрасываем диалог
};

// Сброс диалога
const resetDialog = () => {
    originalMaxHit.value = character.value.max_hit; // Обновляем исходное значение
    originalTempHit.value = character.value.temp_hit; // Обновляем исходное значение
    tempMaxHit.value = character.value.max_hit;   // Сбрасываем временное значение
    tempTempHit.value = character.value.temp_hit;   // Сбрасываем временное значение
};
</script>