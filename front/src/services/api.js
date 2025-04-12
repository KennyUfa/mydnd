import axios from 'axios';
import { useAuthStore } from '@/stores/authStore';

const api = axios.create({
  // baseURL: 'http://88.218.62.253:8000',
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Добавляем перехватчик для установки токена
api.interceptors.request.use((config) => {
  const authStore = useAuthStore();
  const token = authStore.token;

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

export default api;