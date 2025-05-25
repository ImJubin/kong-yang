<!-- src/views/ProductPage.vue -->
<template>
  <!-- <div class="p-4"> -->
    <!-- 추천 영역 -->
         <!-- 💰 금액 입력 -->
    <!-- <input v-model.number="amount" type="number" placeholder="금액을 입력하세요" class="border p-2 rounded" />
    <button @click="store.generateRecommendations(amount)" class="ml-2 bg-blue-500 text-white px-3 py-1 rounded">추천 업데이트</button> -->

    <!-- <ProductRecommendation /> -->

    <!-- 카테고리 선택 -->
    <!-- <div class="mt-6 flex gap-4">
      <button @click="store.selectedTab = '전체'">전체</button>
      <button @click="store.selectedTab = '예금'">예금</button>
      <button @click="store.selectedTab = '적금'">적금</button>
    </div> -->

    <!-- 🏦 은행 선택 필터 -->
    <!-- <select v-model="selectedBank" class="border p-2 w-full my-4">
      <option value="">전체 은행</option>
      <option v-for="bank in uniqueBanks" :key="bank" :value="bank">
        {{ bank }}
      </option>
    </select> -->

    <!-- 상품 목록 -->
     <!-- <div v-if="isLoading" class="text-gray-500 text-center my-6">상품 정보를 불러오는 중입니다...</div>

    <div v-else class="grid grid-cols-3 gap-4 mt-6">
      <ProductCard
        v-for="item in filteredProducts"
        :key="item.id"
        :product="item"
      />
    </div>
  </div> -->

  <div class="p-4">
    <!-- 추천 예적금 영역 -->
    <ProductRecommendation />

    <!-- 🔸 상품 종류 필터 버튼 -->
    <div class="mt-6 flex gap-4">
      <button
        v-for="tab in ['전체', '예금', '적금']"
        :key="tab"
        @click="selectedTab = tab"
        :class="[
          'px-4 py-2 rounded border',
          selectedTab === tab ? 'bg-blue-500 text-white' : 'bg-white text-black'
        ]"
      >
        {{ tab }}
      </button>
    </div>

    <!-- 🔸 은행 선택 드롭다운 -->
    <select v-model="selectedBank" class="border p-2 w-full my-4">
      <option value="">전체 은행</option>
      <option v-for="bank in uniqueBanks" :key="bank" :value="bank">{{ bank }}</option>
    </select>

    <!-- 🔸 상품 목록 -->
    <div v-if="isLoading" class="text-gray-500 text-center my-6">상품 정보를 불러오는 중입니다...</div>

    <div v-else-if="!filteredProducts.length" class="text-gray-500 text-center my-6">
      조건에 맞는 상품이 없습니다.
    </div>

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

// 🔸 데이터 불러오기
onMounted(async () => {
  await store.fetchDeposits()
  await store.fetchSavings()
  isLoading.value = false
})





// import { computed, onMounted, ref, watch } from 'vue'
// import { useDepositStore } from '@/stores/finProduct.js'
// import ProductCard from '@/components/ProductCard.vue'
// import ProductRecommendation from '@/components/ProductRecommendation.vue'

// const store = useDepositStore()
// const amount = ref(null)
// const isLoading = ref(true)
// const selectedBank = ref('')

// onMounted(() => {
//   store.fetchDeposits()
//   store.fetchSavings()
//   isLoading.value = false
// })

// const filteredProducts = computed(() => {
//   if (store.selectedTab === '예금') return store.deposits
//   if (store.selectedTab === '적금') return store.savings
//   return [...store.deposits, ...store.savings]
// })

// const uniqueBanks = computed(() => {
//   const bankSet = new Set(store.recommendedProducts.map(p => p.kor_co_nm))
//   return [...bankSet]
// })

// const filteredProducts = computed(() => {
//   if (!selectedBank.value) return store.recommendedProducts
//   return store.recommendedProducts.filter(p => p.kor_co_nm === selectedBank.value)
// })

// // 💡 금액 변경 감지하여 추천 상품 재계산
// watch(inputAmount, (newAmount) => {
//   if (newAmount && newAmount > 0) {
//     store.generateRecommendations(newAmount)
//   }
// })

// // 💡 처음 들어왔을 때 자동 계산
// onMounted(() => {
//   const defaultAmount = accountStore.getEarliestMaturityAmount?.() || 1000000
//   inputAmount.value = defaultAmount
//   store.generateRecommendations(defaultAmount)
// })

// // 💡 버튼 클릭 수동 실행
// const recalculate = () => {
//   if (inputAmount.value && inputAmount.value > 0) {
//     store.generateRecommendations(inputAmount.value)
//   }
// }

</script>
