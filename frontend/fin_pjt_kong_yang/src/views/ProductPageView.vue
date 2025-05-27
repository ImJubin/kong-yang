<!-- src/views/ProductPage.vue -->
<template>
  <div id = "product-view">
      <!-- 💰 금액 입력: 전역 store와 연결 -->
    <input
      v-model.number="amountStore.amount"
      type="number"
      class="border p-2 w-full mb-2"
      placeholder="예: 5000000"
    />
  <div class="p-4">
    <!-- 추천 예적금 영역 -->
    <ProductRecommendation />

    

    <!-- 🔸 은행 선택 드롭다운 -->

    <select v-model="selectedBank" class="bank-select">
      <option value="">전체 은행</option>
      <option v-for="bank in uniqueBanks" :key="bank" :value="bank">{{ bank }}</option>
    </select>


    <!-- 🔸 상품 종류 필터 버튼 -->
    <div class="filter-option">
  <button
    v-for="tab in ['전체', '예금', '적금']"
    :key="tab"
    @click="selectedTab = tab"
    :class="[
      'px-4 py-2 rounded border transition',
      selectedTab === tab ? 'bg-blue-500 text-white active' : 'bg-white text-black'
    ]"
  >
    {{ tab }}
  </button>
</div>
    <!-- 🔸 상품 목록 -->
    <div v-if="isLoading" class="text-gray-500 text-center my-6">상품 정보를 불러오는 중입니다...</div>

    <div v-else-if="!filteredProducts.length" class="text-gray-500 text-center my-6">
      조건에 맞는 상품이 없습니다.
    </div>

    <div v-else class="product-list">
      <ProductCard
        v-for="item in filteredProducts"
        :key="item.id"
        :product="item"
      />
    </div>
  </div>

</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useDepositStore } from '@/stores/finProduct.js'
import ProductCard from '@/components/ProductCard.vue'
import ProductRecommendation from '@/components/ProductRecommendation.vue'

const store = useDepositStore()

const isLoading = ref(true)

// 🔸 선택된 필터
const selectedTab = ref('전체')        // '전체', '예금', '적금'
const selectedBank = ref('')           // '' = 전체 은행

// 🔸 은행 목록 만들기
const uniqueBanks = computed(() => {
  const allProducts = [...store.deposits, ...store.savings]
  const bankSet = new Set(allProducts.map(p => p.kor_co_nm))
  return [...bankSet]
})

// 🔸 필터 적용
const filteredProducts = computed(() => {
  let baseProducts = []

  // 상품 종류 필터
  if (selectedTab.value === '예금') {
    baseProducts = store.deposits
  } else if (selectedTab.value === '적금') {
    baseProducts = store.savings
  } else {
    baseProducts = [...store.deposits, ...store.savings]
  }

  // 은행명 필터
  if (selectedBank.value) {
    baseProducts = baseProducts.filter(p => p.kor_co_nm === selectedBank.value)
  }

  return baseProducts
})
import { useAmountStore } from '@/stores/amountCalculate.js'
const amountStore = useAmountStore()
// 🔸 데이터 불러오기
onMounted(async () => {
  await store.fetchDeposits()
  await store.fetchSavings()
  amountStore.fetchInitialAmount()
  isLoading.value = false
})

</script>
<style scoped>
#product-view{
  width:1200px;
  margin:20px auto;
  border:1px dashed red;
}
.bank-select{
  margin-left:30px;
  border:1px solid #aaa;
  padding:7px;
  width:300px;
}
.product-list{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem; /* 카드 간 간격 */
  width: 100%;
  box-sizing: border-box;
  /* border: 1px solid blue; */
  padding:0;
}

.recommendation-com{
  margin-bottom: 25px;;
}
.filter-option{
  margin-left:30px;
  margin-top:30px;
}
.filter-option>button{
  background-color: #fff;
  border:none;
  padding:5px 20px;
  font-size: 16px;
  color:#aaa;
}
.filter-option>button.active{
  border-bottom:3px solid #FDDE88;
  font-size: 16px;
  font-weight: 600;
  color:#333;
}
</style>
