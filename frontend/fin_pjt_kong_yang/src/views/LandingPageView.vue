<!-- src/views/LandingPage.vue -->
<template>
  <div class="landing text-center">
    <!-- 헤더 -->
    <!-- <header class="flex justify-between items-center px-6 py-4 text-sm text-gray-600">
      <div class="font-bold text-lg">한냥두냥</div>
      <nav class="space-x-4">
        <a href="#">상품 조회</a>
        <a href="#">이자 시뮬</a>
        <a href="#">로그인</a>
        <a href="#">회원가입</a>
      </nav>
    </header> -->

    <!-- 메인 문구 -->
    <section class="mt-10">
      <p class="text-gray-500">매일 쌓이는 당신의 <span class="text-yellow-400 font-semibold">금융</span> 메이트</p>
      <h1 class="text-5xl font-black mt-1 mb-4">한냥두냥</h1>
      <button class="bg-black text-white px-6 py-2 rounded">시작하기</button>
    </section>

    <!-- 카운트업 숫자 -->
    <section class="mt-14 text-yellow-300 text-[120px] font-black leading-none">
      <CountUp :end="48462" :duration="2500" />
    </section>

    <!-- 소개 문구 -->
    <section class="bg-yellow-400 p-6 text-black font-bold text-lg leading-relaxed">
      나의 예적금 일정과 이자들을 한 곳에서 관리하세요.<br />
      오늘도 한 냥 두 냥 쌓이는<br />
      나의 금융 생활의 페이스메이커
    </section>

    <!-- 이자 정보 -->
    <section class="mt-10">
      <h2 class="text-3xl font-bold text-gray-700 mb-2">D - 195</h2>
      <div class="text-yellow-400 text-6xl font-extrabold">
        <CountUp :end="456.87" :duration="2500" :decimals="2" />
      </div>
    </section>
  </div>
</template>

<script setup>
import CountUp from '@/components/CountUp.vue'
</script>

<style scoped>
.landing {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>
