<!-- src/components/ProductRecommendation.vue -->
<template>
  <div class="p-4 bg-gray-100 rounded">
    <h2 class="text-lg font-bold mb-2">추천 예적금 계산기</h2>

    <p class="text-sm text-gray-600 mb-2">
      예적금 예상 수익을 확인하고 싶으신 금액을 입력해주세요.
    </p>

    <input
      v-model.number="inputAmount"
      type="number"
      class="border p-2 w-full mb-2"
      placeholder="예: 5000000"
    />

    <button @click="recalculate" class="bg-blue-500 text-white px-4 py-2 rounded">
      계산하기
    </button>
    
    <p v-if="inputAmount" class="mt-4">
      예상 수익 기반 추천 상품을 아래에서 확인하세요!
    </p>
    
    <!-- <div class="p-4 bg-gray-100 rounded">
    <h2 class="text-lg font-bold mb-2">추천 예적금 계산기</h2>
    <input v-model.number="inputAmount" type="number" class="border p-2 w-full mb-2" placeholder="예: 5000000" />
    <p v-if="inputAmount" class="mt-2 text-sm text-gray-600">
      아래는 AI가 추천하는 상품이에요!
    </p>
    <div v-if="recommendedProducts.length" class="grid grid-cols-3 gap-4 mt-4">
      <ProductCard
        v-for="item in recommendedProducts"
        :key="item.fin_prdt_cd"
        :product="item"
      />
    </div>
  </div> -->

  </div>
</template>


<script setup>
import { ref, watch, onMounted } from 'vue'
import { useDepositStore } from '@/stores/finProduct.js'
import { useAccountStore } from '@/stores/userAccount'
import axios from 'axios'
import ProductCard from './ProductCard.vue'

const API_URL = 'http://127.0.0.1:8000'
const store = useDepositStore()
const accountStore = useAccountStore()

const inputAmount = ref(null)

// const recommendedProducts = ref([])


// const getAIRecommendation = async (amount) => {
//   try {
//     const res = await axios.post(`${API_URL}/products/recommend/`, { amount })
//     recommendedProducts.value = res.data.recommendations
//   } catch (err) {
//     console.error('AI 추천 실패:', err)
//   }
// }
// // AI 추천
// watch(inputAmount, (newAmount) => {
//   if (newAmount > 0) {
//     getAIRecommendation(newAmount)
//   }
// })

// getAIRecommendation(inputAmount.value)

// ✅ watch로 실시간 반응형 계산
watch(inputAmount, (newAmount) => {
  if (newAmount && newAmount > 0) {
    store.generateRecommendations(newAmount)
  }
})

// 최초 로딩 시 기본값 추천 계산
onMounted(() => {
  const defaultAmount = accountStore.getEarliestMaturityAmount?.() || 1000000
  inputAmount.value = defaultAmount
  store.generateRecommendations(defaultAmount)
})




</script>
