import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useDepositStore = defineStore('deposit', () => {
  const deposits = ref([])
  const savings = ref([])
  const top3 = ref([])   // ✅ 바깥에서 ref로 선언
  const API_URL = 'http://127.0.0.1:8000'
  const selectedTab = ref('전체')


  const fetchDeposits = async () => {
    try {
      const res = await axios.get(`${API_URL}/products/deposits/`)
      deposits.value = res.data
    } catch (error) {
      console.error('예금 데이터 불러오기 실패:', error)
    }
  }

  const fetchSavings = async () => {
    try {
      const res = await axios.get(`${API_URL}/products/savings/`)
      savings.value = res.data
    } catch (error) {
      console.error('적금 데이터 불러오기 실패:', error)
    }
  }

  const generateRecommendations = (amount) => {
  const merged = [...deposits.value, ...savings.value].map(p => ({ ...p }))

  const scored = merged.map(p => {
    const bestOption = p.options?.reduce((max, opt) =>
      opt.intr_rate2 > (max?.intr_rate2 || 0) ? opt : max
    , null)

    const predictedProfit = amount * (bestOption?.intr_rate2 ?? 0) / 100

    return {
      ...p,
      bestRate: bestOption?.intr_rate2 ?? null,
      predictedProfit: predictedProfit || 0,
    }
  })

  // 추천 top3 기준
  top3.value = scored.sort((a, b) => b.bestRate - a.bestRate).slice(0, 3)
  const topIds = new Set(top3.value.map(p => p.id))

  // ✅ deposits 업데이트 (scored에서 매칭)
  deposits.value = deposits.value.map(p => {
    const match = scored.find(i => i.id === p.id)
    return {
      ...p,
      bestRate: match?.bestRate ?? null,
      predictedProfit: match?.predictedProfit ?? null,
      recommended: topIds.has(p.id),
    }
  })

  // ✅ savings 업데이트 (scored에서 매칭)
  savings.value = savings.value.map(p => {
    const match = scored.find(i => i.id === p.id)
    return {
      ...p,
      bestRate: match?.bestRate ?? null,
      predictedProfit: match?.predictedProfit ?? null,
      recommended: topIds.has(p.id),
    }
  })
}


  return {
    deposits,
    savings,
    top3,  // ✅ 이제 정상적으로 return 가능
    fetchDeposits,
    fetchSavings,
    generateRecommendations,
    selectedTab,
  }
}, {
  persist: true
})
