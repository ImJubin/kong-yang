<template>
  <div class="p-4 border rounded bg-white shadow relative">
    <div v-if="product.recommended" class="absolute top-2 right-2 bg-red-400 text-white px-2 rounded text-xs">
      추천
    </div>
    <h3 class="font-bold">{{ product.fin_prdt_nm }}</h3>
    <p>{{ product.kor_co_nm }}</p>
    <p>이율: {{ product.bestRate != null ? product.bestRate + '%' : '정보 없음' }}</p>
    <p>예상 수익: {{ product.predictedProfit != null ? `${product.predictedProfit}원` : '-' }}</p>
  </div>
</template>

<script setup>
defineProps({
  product: Object
})
</script>
