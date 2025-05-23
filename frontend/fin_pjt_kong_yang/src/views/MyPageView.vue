<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
// const user = userStore.user
</script>

<template>
  <div class="mypage-container">
    <h1>🧑 마이페이지</h1>

    <div v-if="userStore.user">
      <ul>
        <li><strong>아이디:</strong> {{ userStore.user.username }}</li>
        <li><strong>이메일:</strong> {{ userStore.user.email }}</li>
        <li><strong>이름:</strong> {{ userStore.user.first_name }} {{ userStore.user.last_name }}</li>
        <li><strong>전화번호:</strong> {{ userStore.user.phone_number }}</li>
        <li><strong>회원 번호 (pk):</strong> {{ userStore.user.pk }}</li>
      </ul>
    </div>
    
    <div v-else>
      <p>유저 정보를 불러오는 중이거나 로그인되지 않았습니다.</p>
    </div>
  </div>
</template>

<style scoped>
.mypage-container {
  max-width: 500px;
  margin: 2rem auto;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 0.75rem;
}
strong {
  display: inline-block;
  width: 120px;
}
</style>