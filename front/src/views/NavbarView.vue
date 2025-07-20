<template>
  <header class="flex p-2 justify-between items-center relative min-h-[60px]">
    <!-- Логотип -->
    <div class="flex-shrink-0">
      <router-link class="block" to="#">
        <h1
          class="text-xl sm:text-2xl md:text-3xl lg:text-4xl font-bold text-yellow-400 mb-1 md:mb-2 leading-tight"
        >
          Лист Персонажа
        </h1>
        <p class="text-xs sm:text-sm text-gray-400 hidden sm:block">
          Dungeons & Dragons 5th Edition
        </p>
      </router-link>
    </div>

    <!-- Центрированное имя пользователя -->
    <div
      v-if="authStore.user"
      class="absolute left-1/2 transform -translate-x-1/2 hidden sm:block"
    >
      <span class="text-sm md:text-xl text-white"
        >Hello {{ authStore.user.name }}</span
      >
    </div>

    <!-- Кнопки авторизации справа -->
    <div v-else class="flex items-center space-x-2 sm:space-x-4">
      <router-link to="/public">
        <Button
          variant="outline"
          class="text-xs sm:text-sm px-2 sm:px-4 py-1 sm:py-2"
          >Log In</Button
        >
      </router-link>
      <router-link to="/signup">
        <Button class="text-xs sm:text-sm px-2 sm:px-4 py-1 sm:py-2"
          >Sign Up</Button
        >
      </router-link>
    </div>

    <!-- Мобильное меню -->
    <Menubar class="flex-shrink-0">
      <MenubarMenu value="file">
        <MenubarTrigger
          class="py-1 p-2 sm:py-2 sm:p-3 space-y-1 flex-col outline-none select-none font-semibold leading-none rounded text-grass11 text-xs flex items-center justify-between gap-[2px] data-[highlighted]:bg-green4 data-[state=open]:bg-green4"
        >
          <span
            v-for="(line, index) in 3"
            :key="index"
            class="block w-4 sm:w-6 h-0.5 bg-gray-700 transition duration-300 ease-in-out"
          ></span>
        </MenubarTrigger>
        <MenubarContent
          class="min-w-[200px] sm:min-w-[220px] outline-none bg-white rounded-lg p-[5px] border shadow-sm [animation-duration:_400ms] [animation-timing-function:_cubic-bezier(0.16,_1,_0.3,_1)] will-change-[transform,opacity]"
          align="end"
          :side-offset="5"
          :align-offset="-3"
        >
          <MenubarItem>
            <router-link
              class="px-3 sm:px-4 text-gray-700 text-sm sm:text-lg md:text-xl lg:text-2xl transition duration-300 ease-in-out whitespace-nowrap block"
              to="/public"
            >
              Home
            </router-link>
          </MenubarItem>
          <MenubarSeparator />
          <MenubarItem>
            <router-link
              class="px-3 sm:px-4 text-gray-700 text-sm sm:text-lg md:text-xl lg:text-2xl transition duration-300 ease-in-out whitespace-nowrap block"
              to="/character"
            >
              Текущий персонаж
            </router-link>
          </MenubarItem>
          <MenubarSeparator />
          <MenubarItem>
            <router-link
              class="px-3 sm:px-4 text-gray-700 text-sm sm:text-lg md:text-xl lg:text-2xl transition duration-300 ease-in-out whitespace-nowrap block"
              to="/characters"
            >
              Лист персонажей
            </router-link>
          </MenubarItem>
          <MenubarItem v-if="authStore.user">
            <Button
              variant="destructive"
              @click="logout"
              class="w-full text-xs sm:text-sm px-2 sm:px-4 py-1 sm:py-2"
            >
              Logout
            </Button>
          </MenubarItem>
        </MenubarContent>
      </MenubarMenu>
    </Menubar>
  </header>
</template>
<script setup>
import { useAuthStore } from '@/stores/authStore.js';
import { useRouter } from 'vue-router';
import { Button } from '@/components/ui/button/index.js';
import { ref } from 'vue';
import {
  Menubar,
  MenubarContent,
  MenubarItem,
  MenubarMenu,
  MenubarSeparator,
  MenubarTrigger,
} from '@/components/ui/menubar/index.js';

const authStore = useAuthStore();
const router = useRouter();

const logout = () => {
  authStore.logout();
  router.push({ path: '/' });
};

const isMenuOpen = ref(false);

function toggleMenu() {
  isMenuOpen.value = !isMenuOpen.value;
  console.log('isMenuOpen:', isMenuOpen.value);
}
</script>
