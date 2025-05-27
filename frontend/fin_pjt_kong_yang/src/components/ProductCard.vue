<template>
  <div class="product-card">
    <!-- 기본 정보 -->
    <div class="card-container">
      <div class="info-card">
        <div class="tag">
          <p>{{ bestRate != null ? bestRate + '%' : '정보 없음' }}</p>
        </div>
        <div class = "base-info">
        <h3 class="product-name">{{ product.fin_prdt_nm }}</h3>
        <p class="text-sm text-gray-600">{{ product.kor_co_nm }}</p>
          
          <p class = "interest"><strong>예상 수익:</strong> {{ predictedProfit.toLocaleString() }}원</p>
        </div>
          <div class="card-content">
        
          <!-- 옵션 테이블 -->
        <div v-if="product.options?.length" class="rate-options-container">
          <h4 class="option-title">금리 옵션 정보</h4>

          <!-- 헤더 -->
          <div class="option-row option-header">
            <div>금리유형</div>
            <div>저축기간</div>
            <div>기본금리</div>
            <div>최고금리</div>
            <div v-if="product.options[0]?.rsrv_type_nm">적립유형</div>
          </div>

          <!-- 옵션 데이터 -->
          <div
            v-for="(opt, i) in product.options"
            :key="i"
            class="option-row"
          >
            <div>{{ opt.intr_rate_type_nm }}</div>
            <div>{{ opt.save_trm }}개월</div>
            <div>{{ opt.intr_rate != null ? opt.intr_rate + '%' : '-' }}</div>
            <div>{{ opt.intr_rate2 != null ? opt.intr_rate2 + '%' : '-' }}</div>
            <div v-if="opt.rsrv_type_nm">{{ opt.rsrv_type_nm }}</div>
          </div>
        </div>
      </div>

        <!-- 상세 페이지 이동 -->
        <button @click="goToDetail" class="corner-button">
          →
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { computed } from 'vue'
import { useAmountStore } from '@/stores/amountCalculate.js'

const router = useRouter()
const amountStore = useAmountStore()

const props = defineProps({
  product: Object
})

// 가장 높은 금리 옵션 계산
const bestOption = computed(() => {
  return props.product.options?.reduce((max, opt) =>
    parseFloat(opt.intr_rate2 || 0) > parseFloat(max?.intr_rate2 || 0) ? opt : max
  , null)
})

const bestRate = computed(() => {
  return bestOption.value?.intr_rate2 ?? null
})

const saveTrm = computed(() => {
  return Number(bestOption.value?.save_trm ?? 12)
})

// 예상 수익 계산
const predictedProfit = computed(() => {
  const amount = amountStore.amount || 0
  const rate = parseFloat(bestRate.value || 0)
  const months = saveTrm.value
  const type = props.product.type

  if (rate === 0 || !type) return 0

  if (type === 'deposit') {
    return Math.round(amount * rate / 100 * (months / 12))
  } else if (type === 'savings') {
    return Math.round(amount * rate / 100 * ((months + 1) / 2 / 12))
  }
  return 0
})

const goToDetail = () => {
  router.push({
    name: 'ProductDetail',
    params: {
      type: props.product.type,
      id: props.product.id
    }
  })
}
</script>



<style scoped>
*{
  box-sizing: border-box;
}
.card-container {
  box-sizing: border-box;
  width: 450px;
  height:550px;
  padding:25px;
  position: relative;
}

.info-card {
  background-color: #FDDE88;
  border-radius: 2rem 2rem 0 2rem;
  padding: 1.7rem;
  height: 100%;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0,0,0,0.05);
}
.tag {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background-color: white;
  padding: 0.4rem 1rem;
  border-radius: 2rem;
  font-weight: bold;
  font-size: 0.9rem;
}
.base-info{
  margin-bottom:40px;
}
.product-name{
  display: block;
  width:70%;
  white-space: nowrap;
  overflow: hidden; 
  text-overflow: ellipsis; 
}

.card-text {
  font-weight: 600;
  text-align: center;
  color: #222;
  line-height: 1.5;
  font-size: 1rem;
}

.corner-button {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 56px;
  height: 56px;
  background-color: black;
  color: white;
  font-size: 1.5rem;
  border-radius: 2rem 0 0 0 ;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.rate-options-container {
  margin-top: 1rem;
  font-size: 0.875rem;
  color: #333;
}

.option-title {
  font-weight: 600;
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
}

.option-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.5rem;
  padding: 0.5rem 0.25rem;
  border-bottom: 1px solid #333;
  text-align: center;
}

.option-header {
  /* background-color: #f3f3f3; */
  font-weight: bold;
  border-top: 1px solid #333;
  border-bottom: 2px solid #333;
}

</style>
