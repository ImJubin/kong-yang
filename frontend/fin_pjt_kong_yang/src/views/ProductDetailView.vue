
<template>
  <div id="product-detail" class = "product-detail">
    <div v-if="product">
      <div class = "product-detail-title">
      <h1 class = "product-name">{{ product.fin_prdt_nm }}<span class = "code">({{ product.fin_prdt_cd }})</span></h1>
      <p class = "bank"> {{ product.kor_co_nm }}</p>
      </div>

      <div class = "sub-detail">
      <p class = "sub">가입 방법</p>
      <p> {{ product.join_way }}</p>
      <p class = "sub">만기 후 이자율</p> 
      <p>{{ product.mtrt_int }}</p>
      <p class = "sub">우대 조건</p>
      <p> {{ product.spcl_cnd || '없음' }}</p>
      <p class = "sub">가입 대상:</p> 
      <p>{{ product.join_member }}</p>
      <p class = "sub">기타 유의사항:</p>
      <p>{{ product.etc_note || '없음' }}</p>
      <p class = "sub">최고 한도:</p> 
      <p>{{ product.max_limit ? product.max_limit + '원' : '제한 없음' }}</p>
      <p class = "sub">공시 기간:</p> 
      <p>{{ product.dcls_strt_day }} ~ {{ product.dcls_end_day || '제한 없음' }}</p>
      <p class = "sub">제출일:</p> 
      <p>{{ product.fin_co_subm_day }}</p>
      </div>

      <div class="options-table">
        <h3 class="options">금리 옵션</h3>

        <!-- 금리 옵션 -->
        <div v-if="product.options?.length" class="rate-options-container">
          
          <div class="option-row option-header">
            <div class="cell">유형</div>
            <div class="cell">기간(개월)</div>
            <div class="cell">기본 금리</div>
            <div class="cell">최고 금리</div>
            <div
              v-if="product.options[0]?.rsrv_type_nm"
              class="cell"
            >
              적립 유형
            </div>
          </div>

          <!-- 데이터 -->
          <div
            v-for="(opt, i) in product.options"
            :key="i"
            class="option-row"
          >
            <div class="cell">{{ opt.intr_rate_type_nm }}</div>
            <div class="cell">{{ opt.save_trm }}</div>
            <div class="cell">{{ opt.intr_rate != null ? opt.intr_rate + '%' : '-' }}</div>
            <div class="cell">{{ opt.intr_rate2 != null ? opt.intr_rate2 + '%' : '-' }}</div>
            <div
              v-if="opt.rsrv_type_nm"
              class="cell"
            >
              {{ opt.rsrv_type_nm }}
            </div>
          </div>
        </div>
      </div>
      <PurchaseForm :product="product" :type="product.type" v-if="userStore.isLoggedIn"/>
    </div>
    
    <div v-else class="text-gray-500">로딩 중...</div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import PurchaseForm from '@/components/PurchaseForm.vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

const route = useRoute()
const product = ref(null)

onMounted(async () => {
  try {
    const res = await axios.get(`http://127.0.0.1:8000/products/${route.params.type}/${route.params.id}/`)
    product.value = res.data
  } catch (err) {
    console.error('상품 로드 실패', err)
  }
})
</script>

<style scoped>
*{
  color:#333;
  line-height: 1.8;
  
}

.product-detail{
  margin-top:80px;
  color:#333;
  width:1200px;
  margin:80px auto;

}
.product-name{
  margin-top:25px;
  font-size:28px;
}
.code{
  font-size: 20px;
  color:#aaa;
}
.options-table{
  margin-bottom:50px;
}
.sub{
  margin-top:20px;
  font-size:18px;
  font-weight: 600;
  border-bottom:1px solid #aaa;
  line-height: 1.8;
  margin-bottom: 10px;
}
.sub-detail{
  margin-bottom:50px;
}
.rate-options-container {
  margin-top: 1rem;
  font-size: 0.875rem;
  border: 1px solid #ccc;
}

.option-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  padding: 0.5rem;
  border-bottom: 1px solid #ddd;
  text-align: center;
}options-table

.option-header {
  background-color: #f3f3f3;
  font-weight: bold;
  border-bottom: 2px solid #999;
}

.cell {
  padding: 0.5rem;
  border-right: 1px solid #ddd;
}

.cell:last-child {
  border-right: none;
}

</style>