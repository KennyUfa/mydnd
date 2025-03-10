<template>
  <header class="border-b">
    <div class="container mx-auto flex items-center justify-between py-4">
      <!-- Логотип -->
      <router-link to="/" class="text-lg font-bold">Kenny's site</router-link>

      <!-- Приветствие пользователя -->
      <div v-if="authStore.user" class="flex items-center space-x-4">
        <span class="text-sm text-muted-foreground">Hello {{ authStore.user.name }}</span>
        <Button variant="destructive" @click="logout">Logout</Button>
      </div>

      <!-- Кнопки входа/регистрации -->
      <div v-else class="flex items-center space-x-4">
        <router-link to="/">
          <Button variant="outline">Log In</Button>
        </router-link>
        <router-link to="/signup">
          <Button>Sign Up</Button>
        </router-link>
      </div>

      <!-- Меню навигации -->
      <NavigationMenu>
        <NavigationMenuList>
          <NavigationMenuItem>
            <router-link to="/">Home</router-link>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <router-link to="/character">Текущий персонаж</router-link>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <router-link to="/characters">Лист персонажей</router-link>
          </NavigationMenuItem>
        </NavigationMenuList>
      </NavigationMenu>
    </div>
  </header>
</template>
<script setup>
import { useAuthStore } from '@/stores/authStore';
import { useRouter } from 'vue-router';
import { Button } from '@/components/ui/button';
import { NavigationMenu, NavigationMenuList, NavigationMenuItem } from '@/components/ui/navigation-menu';

const authStore = useAuthStore();
const router = useRouter();

const logout = () => {
  authStore.logout();
  router.push({ path: '/' });
};
</script>