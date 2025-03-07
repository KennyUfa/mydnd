<template>
  <div>
    <h2>Вход</h2>
    <form @submit.prevent="handleLogin">
      <input v-model="username" placeholder="Имя пользователя" required />
      <input v-model="password" type="password" placeholder="Пароль" required />
      <button type="submit">Войти</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/authStore.js';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();

const username = ref('');
const password = ref('');
const errorMessage = ref('');
const handleLogin = async () => {
  try {
    await authStore.login(username.value, password.value);
    router.push('/characters'); // Перенаправляем на защищенную страницу
  } catch (error) {
    errorMessage.value = 'Ошибка входа: ' + error.message;
  }
};
</script>