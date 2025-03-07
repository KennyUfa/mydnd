<template>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="handleRegister">
      <input v-model="username" placeholder="Имя пользователя" required />
      <input v-model="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Пароль" required />
      <button type="submit">Зарегистрироваться</button>
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
const email = ref('');
const password = ref('');
const errorMessage = ref('');

const handleRegister = async () => {
  try {
    await authStore.register({
      username: username.value,
      email: email.value,
      password: password.value,
    });
    router.push('/login'); // Перенаправляем на страницу входа
  } catch (error) {
    errorMessage.value = 'Ошибка регистрации: ' + error.message;
  }
};
</script>