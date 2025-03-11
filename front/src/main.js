
import {createApp} from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';
// import 'bootstrap/dist/css/bootstrap.min.css';

import "./assets/index.css"; // Подключаем Tailwind CSS



const app = createApp(App);
const pinia = createPinia();

app.use(router).use(pinia);
app.mount('#app');