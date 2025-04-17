<template>

    <navbar-view></navbar-view>
    <router-view></router-view>
    <Toaster/>
</template>

<script setup>
import NavbarView from "./components/NavbarView.vue";
import Toaster from '@/components/ui/toast/Toaster.vue'
</script>