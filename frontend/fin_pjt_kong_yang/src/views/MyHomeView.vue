<template>
    <div class = "my-home">
        <AccountOverview />
        <!-- 내 계좌 리스트 단순화 리스트 만들기 -->
        <MainCalendar />
        <!-- 예적금 리스트 가져오는 컴포넌트 하나 더 만들기 -->
        <!-- 지금까지 모은 이자의 총 합을 가져오는 컴포넌트 하나 만들기 -->
    </div>
</template>
<script setup>
import AccountOverview from '@/components/AccountOverview.vue'
import MainCalendar from '@/components/MainCalendar.vue'
</script>