<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const username = ref('')
const password = ref('')
const errorMsg = ref('')
const router = useRouter()
const userStore = useUserStore()

const logIn = async () => {
  errorMsg.value = '' 

  if (!username.value || !password.value) {
    errorMsg.value = '아이디와 비밀번호를 모두 입력해주세요.'
    return
  }

  try {
    await userStore.logIn({
      username: username.value,
      password: password.value
    })
    // 로그인 성공 
  } catch (err) {
    errorMsg.value = '아이디 또는 비밀번호가 일치하지 않습니다.'
    console.error(err)
  }
}
</script>

<template>
  <div class="container">
  <div class="login-container">
    <h1 class="login_h1">로그인</h1>
    <form @submit.prevent="logIn">
      <!-- <label for="username">아이디</label><br /> -->
      <input id="username" v-model="username" placeholder="로그인"/><br />

      <!-- <label for="password">비밀번호</label><br /> -->
      <input id="password" v-model="password" type="password" placeholder="비밀번호"/><br />

      <p v-if="errorMsg" style="color: red;">{{ errorMsg }}</p>

      <button type="submit">로그인</button>
    </form>
  </div>
  </div>
</template>

<style scoped>
*{
  /* border:1px dashed red; */
}

.login_h1{
  text-align: center;
  margin-bottom:25px;
  color:#333;
}

.login-container {
  max-width: 400px;
  margin: 7rem auto;
  text-align: center;
}
input {
  width: 100%;
  padding: 0.7rem 0.5rem;
  margin: 0.2rem 0 1rem;
  border-radius: 3px;
  border:1px solid #aaa;
  width:350px;
}
label{
  font-weight: 500;
}
button {
  padding: 0.5rem 1rem;
  width:350px;
  margin-top:20px;
  
  color:#fff;
  font-size: 16px;
  border:none;
  transition: all 0.2s ease;
  border-radius: 3px;
  padding:13px 80px;
}
button:hover{
  background-color: #ccc;
  color: #333;
  transition: all 0.2s ease;
}
</style>