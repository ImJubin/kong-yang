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
        parseFloat(opt.intr_rate2) > parseFloat(max?.intr_rate2 || 0) ? opt : max, null)

      const rate = parseFloat(bestOption?.intr_rate2 ?? 0)
      const period = Number(bestOption?.save_trm) || 12
      let profit = 0

      if (p.type === 'deposit') {
        profit = amount * rate / 100 * (period / 12)
      } else {
        profit = amount * rate / 100 * ((period + 1) / 2 / 12)
      }

      return {
        ...p,
        bestRate: rate,
        predictedProfit: Math.round(profit)
      }
    })

    const top3 = scored
    .filter(p => p.bestRate != null && p.save_trm > 0)
    .sort((a, b) => {
      const aMonthly = a.predictedProfit / a.save_trm
      const bMonthly = b.predictedProfit / b.save_trm
      return bMonthly - aMonthly || a.save_trm - b.save_trm  // tie-breaker: 짧은 기간 우선
    })
    .slice(0, 3)
    const topIds = new Set(top3.map(p => p.id))

    // 추천 여부 부여
    deposits.value = deposits.value.map(p => {
      const match = scored.find(i => i.id === p.id)
      return {
        ...p,
        bestRate: match?.bestRate ?? null,
        predictedProfit: match?.predictedProfit ?? null,
        recommended: topIds.has(p.id)
      }
    })

    savings.value = savings.value.map(p => {
      const match = scored.find(i => i.id === p.id)
      return {
        ...p,
        bestRate: match?.bestRate ?? null,
        predictedProfit: match?.predictedProfit ?? null,
        recommended: topIds.has(p.id)
      }
    })
  }



  return {
    deposits,
    savings,
    top3,  
    fetchDeposits,
    fetchSavings,
    generateRecommendations,
    selectedTab,
  }
}, {
  persist: true
})
