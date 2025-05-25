<script setup>
import NavBar from '@/components/NavBar.vue'


import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()
onMounted(() => {
  const token = sessionStorage.getItem('authToken')
  if (token) {
    userStore.fetchUserInfo()
    console.log('✅ 로그인된 토큰 있음, 유저 정보 요청함', token)
  }else {
    console.log('❌ 토큰 없음')
  }
})


</script>

<template>
  <nav>
    <!-- <RouterLink to="/">홈</RouterLink> | -->
    
    <RouterLink :to="{ name : 'Home'}" class = "nav">홈</RouterLink>
    <RouterLink :to="{ name : 'SignUp'}" class = "nav">회원가입</RouterLink>
    <RouterLink :to="{ name : 'Login'}" class = "nav">로그인</RouterLink>
    <RouterLink :to="{ name : 'MyPage'}" class = "nav">마이페이지</RouterLink>
    <RouterLink :to="{ name: 'UpdateMyData' }" class="nav">회원정보 수정</RouterLink> 
    <RouterLink :to="{ name: 'ProductPage' }" class="nav">상품 조회</RouterLink> 
    <RouterLink :to="{ name: 'bankFinder' }" class="nav">은행 위치 조회</RouterLink> 
    <!-- ✅ 추가 -->
  </nav>
   <NavBar />
  <RouterView />
</template>

<style scoped>
.nav {
  text-decoration: none;
}
</style>
