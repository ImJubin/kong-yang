<!-- src/views/ProductPage.vue -->
<template>
  <div class="p-4">
    <!-- 추천 영역 -->
         <!-- 💰 금액 입력 -->
    <!-- <input v-model.number="amount" type="number" placeholder="금액을 입력하세요" class="border p-2 rounded" />
    <button @click="store.generateRecommendations(amount)" class="ml-2 bg-blue-500 text-white px-3 py-1 rounded">추천 업데이트</button> -->

    <ProductRecommendation />

    <!-- 카테고리 선택 -->
    <div class="mt-6 flex gap-4">
      <button @click="store.selectedTab = '전체'">전체</button>
      <button @click="store.selectedTab = '예금'">예금</button>
      <button @click="store.selectedTab = '적금'">적금</button>
    </div>

    <!-- 상품 목록 -->
     <div v-if="isLoading" class="text-gray-500 text-center my-6">상품 정보를 불러오는 중입니다...</div>

    <div v-else class="grid grid-cols-3 gap-4 mt-6">
      <ProductCard
        v-for="item in filteredProducts"
        :key="item.id"
        :product="item"
      />
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useDepositStore } from '@/stores/finProduct.js'
import ProductCard from '@/components/ProductCard.vue'
import ProductRecommendation from '@/components/ProductRecommendation.vue'

const store = useDepositStore()
const amount = ref(null)
const isLoading = ref(true)

onMounted(() => {
  store.fetchDeposits()
  store.fetchSavings()
  isLoading.value = false
})

const filteredProducts = computed(() => {
  if (store.selectedTab === '예금') return store.deposits
  if (store.selectedTab === '적금') return store.savings
  return [...store.deposits, ...store.savings]
})
</script>
