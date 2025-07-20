<template>
    <div class="max-w-6xl mx-auto min-h-screen text-amber-200">
        <navbar-view></navbar-view>
        <router-view></router-view>
        <Toaster/>
    </div>
</template>

<script setup>
import NavbarView from './components/NavbarView.vue';
import Toaster from '@/components/ui/toast/Toaster.vue';
</script>