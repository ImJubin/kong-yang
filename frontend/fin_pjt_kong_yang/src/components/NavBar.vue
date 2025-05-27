<script setup>
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
const userStore = useUserStore()
const router = useRouter()

const handleLogoClick = () => {
  if (userStore.isLoggedIn) {
    router.push({ name: 'LandingPage' })  // 로그인 된 경우
    console.log('login')
  } else {
    router.push({ name: 'LandingPage' })  // 비로그인 상태
    console.log('not')
  }
}
</script>

<template>
  <div class="nav-bar">
    <nav class="nav">
      <!-- ✅ 로고 영역 -->
      <div @click="handleLogoClick" class="logo cursor-pointer">
        <img src="@/assets/logo_gray.svg" alt="로고" />
      </div>

      <!-- ✅ 메뉴 영역 -->
      <ul class="menu">
        <li><RouterLink :to="{ name: 'ProductPage' }">상품 조회</RouterLink></li>
        <li><RouterLink :to="{ name: 'Compare' }">지수 비교</RouterLink></li>
        <li><RouterLink :to="{ name: 'bankFinder' }">은행 위치 조회</RouterLink></li>
        <li><RouterLink :to="{ name: 'Search' }">자료 검색하기</RouterLink></li>
        <li v-if="userStore.user"><RouterLink :to="{ name: 'MyPage' }">마이페이지</RouterLink></li>
      </ul>

      <!-- ✅ 로그인 영역 -->
      <div class="auth">
        <template v-if="userStore.user">
          <span>{{ userStore.user.first_name }}님</span>
          <button @click="userStore.logOut">로그아웃</button>
        </template>
        <template v-else>
          <RouterLink :to="{ name: 'SignUp' }">회원가입</RouterLink>
          <RouterLink :to="{ name: 'Login' }">로그인</RouterLink>
        </template>
      </div>
    </nav>
  </div>
</template>

<style scoped>
.nav-bar {
  width: 100%;
  /* background-color: #fafafa; */
  /* border-bottom: 1px solid #ddd; */
}

.nav {
  width: 1200px;
  height: 60px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo img {
  height: 40px;
  margin-top: 5px;
}

.menu {
  display: flex;
  gap: 2rem;
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 1rem;
  font-weight: 500;
}



.auth {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.auth button {
  background: none;
  border: none;
  cursor: pointer;
  font-weight: 500;
  color: #333;
}
::v-deep a:hover {
  color: #FDC200;
}

</style>