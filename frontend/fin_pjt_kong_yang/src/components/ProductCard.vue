<!-- <template>
  <div class="p-4 border rounded bg-white shadow relative cursor-pointer hover:bg-gray-100 transition"
    @click="goToDetail"
  >
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
import { useRouter } from 'vue-router'
const router = useRouter()

// defineProps({
//   product: Object
// })
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
</script> -->


<template>
  <div class="p-4 border rounded bg-white shadow relative hover:bg-gray-100 transition space-y-2">
    <div v-if="product.recommended" class="absolute top-2 right-2 bg-red-400 text-white px-2 rounded text-xs">
      추천
    </div>

    <h3 class="font-bold text-lg">{{ product.fin_prdt_nm }}</h3>
    <p class="text-sm text-gray-600">{{ product.kor_co_nm }}</p>

    <p><strong>이율:</strong> {{ product.bestRate != null ? product.bestRate + '%' : '정보 없음' }}</p>
    <p><strong>예상 수익:</strong> {{ product.predictedProfit != null ? `${product.predictedProfit}원` : '-' }}</p>

    <!-- 상품 정보 -->
    <div class="mt-2 text-sm text-gray-700 space-y-1">
      <p><strong>공시월:</strong> {{ product.dcls_month }}</p>
      <p><strong>금융회사 코드:</strong> {{ product.fin_co_no }}</p>
      <p><strong>상품 코드:</strong> {{ product.fin_prdt_cd }}</p>
      <p><strong>가입 방법:</strong> {{ product.join_way }}</p>
      <p><strong>만기 후 이자율:</strong> {{ product.mtrt_int }}</p>
      <p><strong>우대 조건:</strong> {{ product.spcl_cnd || '없음' }}</p>
      <p><strong>가입 대상:</strong> {{ product.join_member }}</p>
      <p><strong>기타 유의사항:</strong> {{ product.etc_note || '없음' }}</p>
      <p><strong>최고 한도:</strong> {{ product.max_limit != null ? product.max_limit + '원' : '제한 없음' }}</p>
      <p><strong>공시 기간:</strong> {{ product.dcls_strt_day }} ~ {{ product.dcls_end_day || '제한 없음' }}</p>
      <p><strong>제출일:</strong> {{ product.fin_co_subm_day }}</p>
    </div>

    <!-- 옵션 정보 -->
    <div v-if="product.options?.length" class="mt-4">
      <h4 class="font-semibold text-sm mb-1">금리 옵션 정보</h4>
      <table class="w-full border text-xs text-center">
        <thead class="bg-gray-100">
          <tr>
            <th class="border p-1">금리유형</th>
            <th class="border p-1">저축기간</th>
            <th class="border p-1">기본금리</th>
            <th class="border p-1">최고금리</th>
            <th v-if="product.options[0]?.rsrv_type_nm" class="border p-1">적립유형</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(opt, i) in product.options" :key="i">
            <td class="border p-1">{{ opt.intr_rate_type_nm }}</td>
            <td class="border p-1">{{ opt.save_trm }}개월</td>
            <td class="border p-1">{{ opt.intr_rate != null ? opt.intr_rate + '%' : '-' }}</td>
            <td class="border p-1">{{ opt.intr_rate2 != null ? opt.intr_rate2 + '%' : '-' }}</td>
            <td v-if="opt.rsrv_type_nm" class="border p-1">{{ opt.rsrv_type_nm }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 상세페이지로 이동 버튼 -->
    <button @click="goToDetail" class="mt-4 w-full py-1 text-sm bg-blue-500 hover:bg-blue-600 text-white rounded">
      상세 보기
    </button>
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
