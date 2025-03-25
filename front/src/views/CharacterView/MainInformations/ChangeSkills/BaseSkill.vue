<script setup>
const props = defineProps({
    skillName: String,
    skillValue: Number,
});
</script>

<template>
    <div class="relative flex items-center justify-center mb-1">
        <!-- Основной блок skill -->
        <div class="text-center -mx-3 ">
            <div class="text-xs font-bold">{{ skillName }}</div>
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
    </div>
</template>

<style scoped>

</style>