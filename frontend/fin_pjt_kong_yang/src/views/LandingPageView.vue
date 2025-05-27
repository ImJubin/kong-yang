<!-- src/views/LandingPage.vue -->
<template>
  <div class="landing text-center">
    <!-- 메인 문구 -->
  <div class="landing1">
    <section class="text">
      <p class="catch">매일 쌓이는 <br> 당신의 <span class="text-yellow font-semibold">금융</span> 메이트</p>
      <div class= logo><img src="@/assets/logo_gray.svg"></div>
      <button class="button">시작하기</button>
    </section>

    <!-- 카운트업 숫자 -->
    <section class="landing-count-up mt-14 text-yellow-300 text-[120px] font-black leading-none">
      <CountUp :end="489564865132" :duration="8888885809101" />
    </section>
  </div>
    <!-- 소개 문구 -->
    <section class="landing2 bg-yellow-400 p-6 text-black font-bold text-lg leading-relaxed">
      <p class="landing-text">
        나의 예적금 일정과 이자들을 한 곳에서 관리하세요.<br />
        오늘도 한 냥 두 냥 쌓이는<br />
        나의 금융 생활의 페이스메이커
      </p>
    </section>

    <!-- 이자 정보 -->
  <section class="landing3">
    <div class="landing3-text">
      <p class="subtext">내 자산 조회</p>
      <h2 class="maintext">
        일 분 일 초 변하는<br />
        당신의 <span class="yello-point">이자 내역</span>
      </h2>
      <p class="sub">
        하루 하루 만기까지 함께 쌓아가는<br />
        나의 이자 카운트업
      </p>
    </div>
    <div class="text-right">
      <p class="landing-dday">D - 195</p>
      <p class="landing-count-up2">456.87</p>
    </div>
  </section>
  </div>

  <!-- 예적금 정보 -->
  <div class="landing4">
    <div class="landing4-text">
      <p class="subtext">예적금 상품</p>
      <h2 class="maintext">
        원하는 금액을 바탕으로<br>
        추천하는 금융상품
      </h2>
      <p class="sub">
        원하는 금액을 입력하면<br>
        이자 자동 계산, 상품 추천까지
      </p>
    </div>
  </div>

    <!-- 실물 자산산 정보 -->
  <div class="landing3">
    <div class="landing3-text">
      <p class="subtext">안전자산 투자</p>
      <h2 class="maintext">
        안전 자산 실시간 조회
      </h2>
      <p class="sub">
        금 은 구리 등 안전자산 시세 조회
      </p>
    </div>
  </div>

    <!-- 검색색 정보 -->
  <div class="landing4">
    <div class="landing4-text">
      <p class="subtext">정보 검색</p>
      <h2 class="maintext">
        투자 전에 정보 수집까지
      </h2>
      <p class="sub">
        내 자산을 투자 하기 전에 <br>
        후회 없는 판단을 위한 정보 수집
      </p>
    </div>
  </div>

 <!-- 마무리 -->
  <section class="landing2">
  <p class="landing-text color-w">
    오늘부터 시작하는 당신의 금융 메이트
  </p>
  <img class="landing-logo" src="@/assets/logo_w.svg">
</section>




  <!-- 마우스 커서 -->
   <div class="hide-default-cursor">
    <img src="@/assets/coin.png" class="main-cursor" :style="{ left: x + 'px', top: y + 'px' }" alt="cursor" />
  </div>
</template>

<script setup>
import CountUp from '@/components/CountUp.vue'

import { ref, onMounted } from 'vue'

const x = ref(0)
const y = ref(0)

onMounted(() => {
  window.addEventListener('mousemove', (e) => {
    x.value = e.clientX
    y.value = e.clientY
  })
})

</script>

<style scoped>
*{
  /* border: 1px dashed red; */
  font-family: 'Noto Sans KR', sans-serif;
}
.text-center{
  text-align: center;
}
.landing-count-up{
  margin-bottom:0px auto;
}
.landing {
  font-family: 'Noto Sans KR', sans-serif;
}
.landing1{
  background-color: #fafafa;
  width:100%;
  height:1024px;
  position: relative;
  border:1px dashed blue;
  overflow: hidden;
}
.landing2{
  background-color: #FFDC52;
  height:500px;
}
section{
  margin:0 auto;
}
.text{
  position: absolute;
  left:50%;
  margin-left:-212px;
  top:20%;
  z-index: 50;
}
.catch{
  color:#333;
  font-size:48px;
  margin-bottom:20px;
  letter-spacing: -3px;
  font-weight: 200;
}
.button{
  margin-top:30px;
  padding:13px 80px;
  border-radius: 7px;
  background-color: #555;
  color:#fff;
  font-size: 16px;
  border:none;
  transition: all 0.2s ease;
}
.button:hover{
  background-color: #ccc;
  color: #333;
  transition: all 0.2s ease;
}
.landing-count-up {
  position: absolute;
  bottom: -21%;
  left: 50%;
  transform: translateX(-50%);
  font-size: 750px;
  font-weight: 900;
  color: #FDDE88;
  opacity: 0.5;
  white-space: nowrap;
  pointer-events: none;
  z-index: 0;
  letter-spacing: -25px;
}

.landing-count-up2{
    position: absolute;
    bottom: 0%;
    right:10%;
    font-size: 370px;
    font-weight: 900;
    color: #ffd153;
    opacity: 0.5;
    white-space: nowrap;
    pointer-events: none;
    z-index: 0;
    letter-spacing: -25px;
    text-align: right;
}
.landing-dday{
  position: absolute;
  font-size:110px;
  right:10%;
  color:#aaa;
  top:28%;
  font-weight: 800;

}

.landing-text{
  padding-top:180px;
  font-size :30px;
  font-weight:700;
  letter-spacing:-1px;
  line-height: 50px;
  color:#472C00;
  text-align: center;
  
}
.landing3{
  background-color: #fff;
  position: relative;
  width:100%;
  height:770px;
}
.landing3-text{
  width:1200px;
  border:1px dashed red;
  margin:0 auto;
  text-align: left;
  margin-top:83px;
  letter-spacing: -0.5px;;
}

.subtext{
  color:#555;
  font-weight: 700;
  font-size:18px;
  margin-bottom:5px;
}
.maintext{
  margin-bottom:20px;
  font-weight: 700;
  font-size:38px
}
.sub{
  font-size:20px;
  line-height: 35px;
}
.yello-point{
  color:#FDC200;
}

.landing4{
  background-color: #eee;
  width:100%;
  height:900px;
  position: relative;
  padding-top:83px;
}

.landing4-text{
  width:1200px;
  margin:0 auto;
  text-align: right;
  /* margin-top:83px; */
  letter-spacing: -0.5px;;
}
.landing-logo{
  text-align: center;
  display: block;
  /* border:1px dashed red; */
  margin:20px auto;
  width: 200px;

}
.color-w{
  color:white;
}




.main-cursor {
  position: fixed;
  width: 32px;
  height: 32px;
  pointer-events: none;
  transform: translate(-50%, -50%);
  z-index: 9999;
}
*{
  cursor: none;
}
</style>
