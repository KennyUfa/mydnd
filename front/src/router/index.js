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
    meta: { requiresAuth: true },
  },

  {
    path: '/character',
    component: Character,
    meta: { requiresAuth: true },
    async beforeEnter(to, from, next) {
      const authStore = useAuthStore();
      const characterStore = useCharacterStore();

      // Проверяем авторизацию
      if (!authStore.isAuthenticated) {
        next('/login');
        return;
      }

      // Получаем ID персонажа из localStorage
      const championId = localStorage.getItem('champion_id');

      if (!championId) {
        // Если нет ID персонажа, перенаправляем на список персонажей
        next('/characters');
        return;
      }

      try {
        // Проверяем, загружены ли данные персонажа
        if (
          !characterStore.character ||
          characterStore.character.id !== championId
        ) {
          await characterStore.fetchCharacter(championId);
        }
        // Если данные успешно загружены, разрешаем переход
        next();
      } catch (error) {
        console.error('Ошибка при загрузке данных персонажа:', error);
        // Если ошибка 401 (неавторизован), перенаправляем на логин
        if (error.response && error.response.status === 401) {
          authStore.logout();
          next('/login');
        } else {
          // Иначе перенаправляем на список персонажей
          next('/characters');
        }
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

  // Проверяем, требует ли маршрут авторизации
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;
