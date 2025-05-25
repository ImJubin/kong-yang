<script setup>
// import TheWelcome from '../components/TheWelcome.vue'
import { useUserStore } from '@/stores/user'
import MainCalendar from '@/components/MainCalendar.vue'
const userStore = useUserStore()
</script>

<template>
  <div>
    <h1>홈</h1>
    <div v-if="userStore.user">👋 {{ userStore.user.first_name }}님 환영합니다!
    <MainCalendar />


    </div>
    <div v-else>로그인 해주세요</div>
  </div>
</template>