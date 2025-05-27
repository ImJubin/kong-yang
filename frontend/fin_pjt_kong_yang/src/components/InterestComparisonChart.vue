<template>
  <div class="chart">
    <Bar
        v-if="chartData.labels.length"
        :data="chartData"
        :options="chartOptions"
        :height="chartData.labels.length * 45" 
      />
    <p v-else>표시할 데이터가 없습니다.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
} from 'chart.js'
import axios from 'axios'

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend)

const chartData = ref({
  labels: [],
  datasets: []
})

const chartOptions = {
  responsive: true,
  indexAxis: 'y',
  interaction: {
    mode: 'nearest',
    axis: 'y',
    intersect: false
  },
  plugins: {
    legend: { position: 'top' },
    title: {
      display: true,
      text: '내 계좌 금리 vs 기준금리'
    },
    tooltip: {
      callbacks: {
        label: ctx => `${ctx.dataset.label}: ${ctx.parsed.x}%`
      }
    }
  },
  scales: {
    x: {
      beginAtZero: true,
      title: {
        display: true,
        text: '금리 (%)'
      }
    },
    y: {
      ticks: {
        font: {
          size: 13
        }
      }
    }
  }
}

const API_URL = 'http://127.0.0.1:8000'

onMounted(async () => {
  const token = sessionStorage.getItem('authToken')
  const res = await axios.get(`${API_URL}/users/my-interest/`, {
    headers: {
      Authorization: `Token ${token}`
    }
  })

  const baseRate = parseFloat(res.data.base_rate)
  const accounts = res.data.my_accounts || []

  const isValidRate = (rate) =>
    rate !== null && rate !== undefined && rate !== '' && !isNaN(parseFloat(rate))

  const validAccounts = accounts.filter(acc => isValidRate(acc.interest_rate))

  // 금리 순 정렬
  const sortedAccounts = [...validAccounts].sort((a, b) => b.interest_rate - a.interest_rate)

  // 상품명 + 계좌번호
  const labels = ['기준금리'].concat(
  sortedAccounts.map(acc => {
    // 별칭 우선
    if (acc.alias_name) return acc.alias_name

    // 상품명
    const productName =
      acc.account_type === '적금'
        ? acc.savings_detail?.product_name
        : acc.deposit_detail?.product_name

    // 상품명 + 계좌번호 or 계좌번호만
    if (productName) {
      return `${productName} (${acc.account_number})`
    } else {
      return `${acc.account_number}`
    }
  })
)

  // ✅ 데이터: 기준금리 + 내 금리들
  const data = [baseRate].concat(sortedAccounts.map(acc => parseFloat(acc.interest_rate)))

  chartData.value = {
    labels: labels,
    datasets: [
      {
        label: '금리',
        data: data,
        backgroundColor: [
          '#FDC200',
          ...Array(sortedAccounts.length).fill('#aaa')  // 상품들 색상
        ],
        barThickness: 30 
      }
    ]
  }

  // console.log('응답:', res.data)
  // console.log('유효한 계좌:', sortedAccounts)
  // console.log('차트 라벨:', chartData.value.labels)
  // console.log('차트 데이터:', chartData.value.datasets[0].data)
})
</script>
<style scoped>
  .chart{
    border:1px solid #eee;
    border-radius: 15px;
    padding:15px;
    box-shadow: 0 2px 5px rgba(170, 170, 170, 0.1);
    margin-right: 15px;
    height:700px;
  }
  
</style>
