import { defineStore } from 'pinia';
import AuthService from '@/services/auth.service';
import TokenService from '@/services/token.service';

export const useAuthStore = defineStore('auth', {
  state: () => {
    const user = JSON.parse(localStorage.getItem('user'));
    return {
      user: user || null,
      isLoggedIn: !!user,
    };
  },
  actions: {
    // Авторизация пользователя
    async login(username, password) {
      try {
        const response = await AuthService.login(username, password);
        this.user = response;
        this.isLoggedIn = true;
        TokenService.setUser(response); // Сохраняем токен в localStorage
      } catch (error) {
        this.logout();
        throw error; // Передаем ошибку дальше
      }
    },

    // Выход из системы
    logout() {
      this.user = null;
      this.isLoggedIn = false;
      TokenService.removeUser(); // Удаляем токен из localStorage
    },

    // Регистрация пользователя
    async register(userData) {
      try {
        await AuthService.register(userData);
      } catch (error) {
        throw error; // Передаем ошибку дальше
      }
    },

    // Обновление токена
    refreshToken(accessToken) {
      if (this.user) {
        this.user.accessToken = accessToken;
        TokenService.setUser(this.user); // Обновляем токен в localStorage
      }
    },
  },
  getters: {
    // Проверка аутентификации
    isAuthenticated: (state) => !!state.user,
    token: (state) => state.user?.access || null,
  },
});