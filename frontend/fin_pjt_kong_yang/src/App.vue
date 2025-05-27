<script setup>
import NavBar from "@/components/NavBar.vue";

import { RouterLink, RouterView } from "vue-router";
import { onMounted } from "vue";
import { useUserStore } from "@/stores/user";
const userStore = useUserStore();
onMounted(() => {
  const token = sessionStorage.getItem("authToken");
  if (token) {
    userStore.fetchUserInfo();
    console.log("✅ 로그인된 토큰 있음, 유저 정보 요청함", token);
  } else {
    console.log("❌ 토큰 없음");
  }
});
import LandingPage from '@/views/LandingPageView.vue'
</script>

<template>
  <NavBar />
  <RouterView />
</template>


<style>
*{
  margin:0;
  padding:0;
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
}
.text-yellow{
  color:#FDC200;
}
a{
  text-decoration: none;
  color:#333;
}
a:hover{
  color:#FDC200;
}


</style>