<template>
   <div class="product-card">
    <!-- 기본 정보 -->
    <div class="card-container">
      <div class="info-card">
        <div class="tag">
          <p>{{ product.intr_rate2 != null ? product.intr_rate2 + '%' : '정보 없음' }}</p>
        </div>
        <div class = "base-info">
        <h3 class="product-name">{{ product.fin_prdt_nm }}</h3>
        <p class="text-sm text-gray-600">{{ product.kor_co_nm }}</p>
          
          <p class = "interest"><strong>예상 수익:</strong> {{ product.predicted_profit.toLocaleString() }}원</p>
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
const router = useRouter()

const props = defineProps({
  product: Object
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
  height:250px;
  padding:25px;
  position: relative;
}

.info-card {
  background-color: #333;
  border-radius: 2rem 2rem 0 2rem;
  padding: 1.7rem;
  height: 100%;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0,0,0,0.05);
  color:#fff;
}
.interest{
  margin-top:70px;
  font-size:20px;
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
  color:#333;
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
  color: #fff;
  line-height: 1.5;
  font-size: 1rem;
}

.corner-button {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 56px;
  height: 56px;
  background-color: #eee;
  color: 333;
  font-size: 1.5rem;
  border-radius: 2rem 0 0 0 ;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border:none;
  border:1px solid #333;
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
