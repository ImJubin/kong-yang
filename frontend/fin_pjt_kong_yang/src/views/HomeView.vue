<script setup>
// import TheWelcome from '../components/TheWelcome.vue'
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()
</script>

<template>
  <div>
    <h1>홈</h1>
    <p v-if="userStore.user">👋 {{ userStore.user.first_name }}님 환영합니다!</p>
    <p v-else>로그인 해주세요</p>
  </div>
</template>