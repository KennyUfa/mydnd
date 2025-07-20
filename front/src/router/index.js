import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';
import Character from '@/views/CharacterView/Character.vue';
import { useCharacterStore } from '@/stores/characterStore.js';

const routes = [
  { path: '/login', component: () => import('@/views/Login.vue') },
  { path: '/', component: () => import('@/views/Login.vue') },
  { path: '/register', component: () => import('@/views/Register.vue') },
  {
    path: '/characters',
    component: () => import('@/views/AccountList/CharactersView.vue'),
  },

  {
    path: '/character',
    component: Character,
    async beforeEnter(to, from, next) {
      const characterStore = useCharacterStore();
      const championId = localStorage.getItem('champion_id'); // Получаем ID из URL

      try {
        // Проверяем, загружены ли данные персонажа
        if (
          !characterStore.character ||
          characterStore.character.id !== championId
        ) {
          await characterStore.fetchCharacter(championId); // Загружаем данные
        }
        // Если данные успешно загружены, разрешаем переход
        next();
      } catch (error) {
        console.error('Ошибка при загрузке данных:', error);
        next('/characters'); // Перенаправляем на страницу списка персонажей
      }
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;
