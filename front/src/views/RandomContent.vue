<script setup>
const props = defineProps({
    result: {
        type: Object,
        required: true,
    },
});
</script>

<template>
    <p v-if="result.d4">d4- {{ result.d4 }}</p>
    <p v-if="result.d6">d6- {{ result.d6 }}</p>
    <p v-if="result.d8">d8- {{ result.d8 }}</p>
    <p v-if="result.d10">d10- {{ result.d10 }}</p>
    <p v-if="result.d12">d12- {{ result.d12 }}</p>
    <p v-if="result.d20">d20- {{ result.d20 }}</p>
    <strong>Итого: {{ result.total }}</strong>

</template>

<style scoped>

</style>