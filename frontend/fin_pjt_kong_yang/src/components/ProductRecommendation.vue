<template>
  <div class="recommendation-com">
    <!-- 추천 카드 -->
    <div v-if="recommendations.length" class="mb-6">
      <h2 class="title"> 추천 상품</h2>
      <div class="recommedation-card-list">
        <ProductRecommendationCard
          v-for="product in recommendations"
          :key="product.id + '-' + product.save_trm"
          :product="product"
        />
      </div>
    </div>


  </div>
</template>

<script setup>
import { watch, onMounted, ref } from 'vue'
import axios from 'axios'
import ProductRecommendationCard from './ProductRecommendationCard.vue'
import { useAccountStore } from '@/stores/userAccount'
import { useAmountStore } from '@/stores/amountCalculate'

const API_URL = 'http://127.0.0.1:8000'
const recommendations = ref([])
const amountStore = useAmountStore()
const accountStore = useAccountStore()

// 서버에 추천 상품 요청
const fetchRecommendation = async (amount = null) => {
  try {
    const token = sessionStorage.getItem('authToken')
    const res = await axios.post(`${API_URL}/products/recommend/`, {
      amount
    }, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    recommendations.value = res.data
  } catch (err) {
    console.error('추천 요청 실패:', err)
  }
}

// 금액이 바뀔 때마다 추천 요청
watch(() => amountStore.amount, (newAmount) => {
  if (newAmount && newAmount > 0) {
    fetchRecommendation(newAmount)
  }
})

// 초기 진입 시 유저 계좌 기반 금액 + 추천 요청
onMounted(async () => {
  if (!amountStore.amount) {
    await amountStore.fetchInitialAmount()
  }
  fetchRecommendation(amountStore.amount)
})
</script>
<style scope>
.title{
  margin-top:30px;
  margin-left:30px;
}
.recommedation-card-list{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem; /* 카드 간 간격 */
  width: 100%;
  box-sizing: border-box;
  /* border: 1px solid blue; */
  padding:0;
}
</style>