import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';
import { useAuthStore } from './stores/authStore';

import './assets/index.css'; // Подключаем Tailwind CSS

const app = createApp(App);
const pinia = createPinia();

app.use(router).use(pinia);

// Инициализируем authStore при загрузке приложения
const authStore = useAuthStore();
authStore.init();

app.mount('#app');
