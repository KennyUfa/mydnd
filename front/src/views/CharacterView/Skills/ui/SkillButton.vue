<template>
    <div class="relative flex items-center justify-center mb-3">
        <!-- Кнопка декремента -->
        <button
                class="relative top-9"
                @click="decrementValue"
                :disabled="skillValue <= 1"
        >
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                 fill="currentColor" class="size-12">
                <path
                        fill-rule="evenodd"
                        d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25Zm3 10.5a.75.75 0 0 0 0-1.5H9a.75.75 0 0 0 0 1.5h6Z"
                        clip-rule="evenodd"
                />
            </svg>
        </button>

        <!-- Основной блок skill -->
        <div class="text-center -mx-3 ">
            <div class="text-xs font-bold mb-1">{{ skillName }}</div>
            <div
                    class="w-14 h-14 border-2 border-red-600 rounded-full flex flex-col items-center justify-center mx-auto"
            >
                <div class="text-3xl font-bold">
                    {{ Math.floor((skillValue - 10) / 2) }}
                </div>
            </div>
            <div
                    class="absolute -bottom-3 left-1/2 transform -translate-x-1/2 w-7 h-7 bg-white border-2 border-red-600 rounded-full flex items-center justify-center text-lg font-medium"
            >
                {{ skillValue }}
            </div>
        </div>

        <!-- Кнопка инкремента -->
        <button
                class="relative top-9"
                @click="incrementValue"
                :disabled="skillValue >= 30"
        >
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                 fill="currentColor" class="size-12">
                <path
                        fill-rule="evenodd"
                        d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM12.75 9a.75.75 0 0 0-1.5 0v2.25H9a.75.75 0 0 0 0 1.5h2.25V15a.75.75 0 0 0 1.5 0v-2.25H15a.75.75 0 0 0 0-1.5h-2.25V9Z"
                        clip-rule="evenodd"
                />
            </svg>
        </button>
    </div>
</template>

<script setup>
const props = defineProps({
    skillName: String,
    skillValue: Number,
});

const emit = defineEmits(["update:skillValue"]);


// Увеличение значения навыка
const incrementValue = () => {
    const newValue = props.skillValue + 1;
    if (newValue <= 30) {
        emit("update:skillValue", newValue); // Отправляем новое значение родителю
    }
};

// Уменьшение значения навыка
const decrementValue = () => {
    const newValue = props.skillValue - 1;
    if (newValue >= 1) {
        emit("update:skillValue", newValue); // Отправляем новое значение родителю
    }
};
</script>

<style scoped></style>