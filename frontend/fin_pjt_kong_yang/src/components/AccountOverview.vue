<template>
  <div class="account-overview">
    <!-- <h2 class="account-title">내 계좌 현황</h2> -->

    <div v-if="store.accounts.length">
      <div
        v-for="account in store.accounts"
        :key="account.id"
        class="account-card"
      >
        <h3 class="account-name">
          {{ account.alias_name || account.account_number }}
          <span class = "balance">{{ account.current_balance.toLocaleString() }}원</span>
          <span class ="account-bank">{{ account.bank_name }}</span>
          <span class="account-type">{{ account.account_type }}</span>
        </h3>
        <div class = "detail">

        <!-- 예금 상세 -->
         
        <div v-if="account.deposit_detail" class = "account-detail">
          <div class = "detail-left-deposit">
          <p>{{ account.deposit_detail.product_name }}</p>
          <p>{{ account.deposit_detail.duration_months }}개월</p>
          <!-- <p>{{ account.deposit_detail.started_at }}</p> -->
          <p>{{ account.deposit_detail.ends_at }}</p>
        </div>
        
        <div class = "interest">
          <p class = "simulated_interest">
            {{ parseFloat(account.deposit_detail.simulated_interest || account.deposit_detail.interest_accumulated).toLocaleString() }}원
          </p>
          <p>{{ account.deposit_detail.interest_rate }}%</p>
        </div>

        </div>

        <!-- 적금 상세 -->
        <div v-else-if="account.savings_detail" class = "account-detail">
          <div class = "detail-left-saving">
            <div class = "saving-left">
          <p>{{ account.savings_detail.product_name }}</p>
          <p>{{ account.savings_detail.duration_months }}개월</p>
          <!-- <p>시작일: {{ account.savings_detail.started_at }}</p> -->
          <!-- <p>계약 만기일: {{ account.savings_detail.ends_at }}</p> -->
          <!-- <p>총 회차: {{ account.savings_detail.total_round }}</p> -->
          <p>목표 금액<br>
            {{ account.savings_detail.goal_amount.toLocaleString() }}원</p>
          
          
          
          
          <p>계약 수령일<br>
            {{ account.savings_detail.contract_receive_date }}</p>
          <p>예상 수령일<br>{{ account.savings_detail.expected_receive_date }}</p>
          <!-- <p>납입 상태: {{ account.savings_detail.delay_label }}</p> -->
          <p>누적 연체 {{ account.savings_detail.accumulated_delay_days }}일</p>
          <!-- <p>예상 만기일: {{ account.savings_detail.calculated_ends_at }}</p> -->
          <!-- <p>연체 개월: {{ account.savings_detail.delay_months }}개월</p> -->
          
          <p v-if="account.savings_detail.payments.length">
            최근 불입일: {{ account.savings_detail.payments.at(-1).paid_at }}
          </p>
          
        </div>
        <!-- 납입 이력 전체 -->
        <div class="saving-list">
          <p v-if="account.savings_detail.payments.length" class = "saving-number">현재 {{ account.savings_detail.payments.at(-1).round_number }}회차
          </p>
          <p class="font-semibold text-sm">납입 이력</p>
          <ul>
            <li
            v-for="payment in account.savings_detail.payments"
            :key="payment.id"
            >
            {{ payment.round_number }}회차 - {{ payment.paid_at }} - {{ payment.amount.toLocaleString() }}원
          </li>
        </ul>
      </div>
      
    </div>
    <div class = "interest">
      <p class = "simulated_interest">
        {{ parseFloat(account.savings_detail.simulated_interest || account.savings_detail.interest_accumulated).toLocaleString() }}원
      </p>
      <p>{{ account.savings_detail.interest_rate }}%</p>
      <p>{{ account.savings_detail.delay_status }}</p>
    </div>
  </div>
    </div>
  </div>
</div>

    <div v-else>
      <p>계좌 정보가 없습니다.</p>
    </div>
    <!-- 계좌 추가 폼 토글  -->
        <!-- <button @click="showAccountForm = !showAccountForm" class = "account-plus">
          {{ showAccountForm ? '계좌 추가 폼 닫기' : ' 계좌 추가' }}
        </button>
        <AccountAddForm v-if="showAccountForm" /> -->
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAccountStore } from '@/stores/userAccount'
import AccountAddForm from '@/components/AccountAddForm.vue'
import axios from 'axios'

const store = useAccountStore()

// 실시간 이자 시뮬레이션 함수
const startInterestSimulation = function(detail) {
  if (!detail || !detail.started_at || !detail.ends_at || !detail.interest_total) return

  const start = new Date(detail.started_at)
  const end = new Date(detail.ends_at)
  const totalSeconds = (end - start) / 1000

  const totalInterest = parseFloat(detail.interest_total)
  const interestPerSecond = totalInterest / totalSeconds
  let simulatedInterest = parseFloat(detail.interest_accumulated)

  detail.simulated_interest = simulatedInterest.toFixed(2)

  setInterval(function() {
    simulatedInterest += interestPerSecond
    detail.simulated_interest = simulatedInterest.toFixed(2)
  }, 1000)
}

// 컴포넌트가 마운트되면 실행
onMounted(async function() {
  const token = sessionStorage.getItem('authToken')

  try {
    // 0. 누적 이자 서버에서 갱신
    await axios.post('http://127.0.0.1:8000/users/update-interest/', {}, {
      headers: {
        Authorization: `Token ${token}`
      }
    })

    // 1. 계좌 정보 불러오기
    await store.fetchAccounts()

    // 2. 각 계좌에 대해 실시간 이자 시뮬레이션 시작
    store.accounts.forEach(function(acc) {
      if (acc.savings_detail) startInterestSimulation(acc.savings_detail)
      if (acc.deposit_detail) startInterestSimulation(acc.deposit_detail)
    })

  } catch (err) {
    console.error('이자 갱신 또는 계좌 조회 실패:', err)
  }
})
</script>

<style scoped>
*{
  /* border:1px dashed blue; */
  color:#333;
}
.saving-number{
  font-weight: 700;
}
.balance{
  margin-left:15px;
  font-size:16px;
  font-weight: 500;
  color:#FDC200;
}
.account-card{
  border:1px solid #eee;
  margin-bottom:15px;
  border-radius: 15px;
  padding:15px;
  box-shadow: 0 2px 5px rgba(170, 170, 170, 0.1);
}
.account-bank{
  margin-left:24px;
  font-size:16px;
  color:#555;
}

.detail{
  display: flex;
  width:100%;
  line-height:1.8;
}
.account-detail{
  display: flex;
  width:100%
}

.account-type{
  color:#555;
  font-size:16px;
  position:absolute;
  right:26%;
  bottom: 0%

}
.account-name{
  border-bottom:1px solid #aaa;
  width:100%;
  line-height: 2;
  position:relative;
}
ul>li{
  list-style: none;
}

.detail-left-deposit{
  width:70%
}
.simulated_interest{
  font-weight: 800;
  font-size:22px;
}
.interest{
  width:30%;
}
.detail-left-saving{
  width:71%;
  display: flex;
}
.saving-left{
  width:40%
}
.saving-list{
  width:60%
}
.account-plus{
  border:none;
  background-color: #fff;
}

</style>