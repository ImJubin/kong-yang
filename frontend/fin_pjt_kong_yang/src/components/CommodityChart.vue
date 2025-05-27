<template>
  <div class="price-chart-container">
    <Line :data="chartData" :options="chartOptions" class="mb-8" />

    <div class="price-list">
      <div v-for="(item, idx) in data" :key="idx">
        <!-- 날짜 구분선 -->
        <div v-if="idx > 0 && isDateChanged(data[idx - 1].x, item.x)" class="date-divider">
          📅 {{ formatDate(item.x) }}
        </div>

        <!-- 가격 항목 카드 -->
        <div class="price-row">
          <div class="time">{{ formatDateTime(item.x) }}</div>
          <div
            class="price"
            :class="{ up: isPriceUp(idx), down: isPriceDown(idx) }"
          >
            {{ item.y.toFixed(2) }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
} from "chart.js";
import { ref, watch } from "vue";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale
);

const props = defineProps(["data"]);

const chartData = ref({
  labels: props.data.map((d) => new Date(d.x).toLocaleTimeString()),
  datasets: [
    {
      label: "Price",
      data: props.data.map((d) => d.y),
      fill: true,
      backgroundColor: "#AAAAAA22",
      borderColor: "#FDC200",
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4,
      pointBackgroundColor: "#FDC200",
    },
  ],
});

const chartOptions = ref({
  responsive: true,
  plugins: {
    legend: {
      labels: {
        font: {
          family: "Noto Sans KR",
        },
      },
    },
    title: {
      display: true,
      text: "상품 시세 차트",
      font: {
        size: 18,
        family: "Noto Sans KR",
      },
    },
  },
  scales: {
    x: {
      ticks: {
        font: {
          family: "Noto Sans KR",
        },
      },
    },
    y: {
      ticks: {
        font: {
          family: "Noto Sans KR",
        },
      },
    },
  },
});

const formatDateTime = (iso) => {
  return new Date(iso).toLocaleString("ko-KR", {
    dateStyle: "short",
    timeStyle: "medium",
  });
};

const formatDate = (iso) => {
  const d = new Date(iso);
  return `${d.getFullYear()}. ${d.getMonth() + 1}. ${d.getDate()}`;
};

const isDateChanged = (prevIso, currIso) => {
  return formatDate(prevIso) !== formatDate(currIso);
};

const isPriceUp = (idx) => {
  return idx > 0 && props.data[idx].y > props.data[idx - 1].y;
};

const isPriceDown = (idx) => {
  return idx > 0 && props.data[idx].y < props.data[idx - 1].y;
};

watch(
  () => props.data,
  (newData) => {
    chartData.value = {
      labels: newData.map((d) => new Date(d.x).toLocaleTimeString()),
      datasets: [
        {
          label: "Price",
          data: newData.map((d) => d.y),
          fill: true,
          backgroundColor: "#AAAAAA22",
          borderColor: "#FDC200",
          borderWidth: 2,
          tension: 0.3,
          pointRadius: 4,
          pointBackgroundColor: "#FDC200",
        },
      ],
    };
  },
  { immediate: true }
);
</script>

<style scoped>
.price-chart-container {
  font-family: "Noto Sans KR", sans-serif;
}

.price-list {
  max-height: 300px;
  overflow-y: auto;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 4px 0;
  box-shadow: 0 2px 4px #ccc;
  background-color: white;
}

.date-divider {
  text-align: center;
  font-size: 12px;
  color: #666;
  background-color: #f0f0f0;
  padding: 4px 0;
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
}

.price-row {
  display: flex;
  justify-content: space-between;
  padding: 6px 12px;
  border-bottom: 1px solid #eee;
}

.time {
  color: #333;
  font-size: 13px;
}

.price {
  font-weight: bold;
  font-size: 14px;
}

.price.up {
  color: #e11d48; /* red-600 */
}

.price.down {
  color: #2563eb; /* blue-600 */
}
</style>
