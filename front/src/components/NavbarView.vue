<template>
  <header>
    <nav class="navbar navbar-expand-lg">
      <a class="navbar-brand" href="#">Kenny's site</a>
      <a class="btn btn-light name-account" v-if="authStore.user"
      >Hello {{ authStore.user.name }}</a
      >
      <div class="logging">
        <div class="ms-auto actions" v-if="authStore.isLoggedIn">
          <button type="button" class="btn btn-warning" @click="logout">
            Logout
          </button>
        </div>
        <div class="ms-auto navbar-text actions" v-else>
          <a class="btn login btn-warning" href="/">Log In</a>
          <a
            class="btn btn-light action-button"
            role="button"
            href="signup.html"
          >Sign Up</a
          >
        </div>
      </div>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarTogglerDemo01"
        aria-controls="navbarTogglerDemo01"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/charlist">Текущий персонаж</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/characters" aria-disabled="true"
            >Лист персонажей</a
            >
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>
<script setup>
import {useAuthStore} from '@/stores/authStore';
import {useRouter} from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();


const logout = () => {
  authStore.logout();
  router.push({path: '/'});
};
</script>
