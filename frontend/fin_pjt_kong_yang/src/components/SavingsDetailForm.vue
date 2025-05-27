<template>
  <div class="saving">
    <h4 class="saving-title">적금 상품 정보</h4>

    <div>
      <label>상품명</label><br>
      <input
        type="text"
        :value="modelValue.product_name"
        @input="update('product_name', $event.target.value)"
      />
    </div>

    <div>
      <label>금리 (%)</label><br>
      <input
        type="number"
        step="0.01"
        :value="modelValue.interest_rate"
        @input="update('interest_rate', +$event.target.value)"
      />
    </div>

    <div>
      <label>기간 (개월)</label><br>
      <input
        type="number"
        :value="modelValue.duration_months"
        @input="update('duration_months', +$event.target.value)"
      />
    </div>

    <div>
      <label>시작일</label><br>
      <input
        type="date"
        :value="modelValue.started_at"
        @input="update('started_at', $event.target.value)"
      />
    </div>

    <div>
      <label>만기일</label><br>
      <input
        type="date"
        :value="modelValue.ends_at"
        @input="update('ends_at', $event.target.value)"
      />
    </div>

    <div>
      <label>불입일</label><br>
      <input
        type="date"
        :value="modelValue.payment_date"
        @input="update('payment_date', $event.target.value)"
      />
    </div>

    <div>
      <label>현재 회차</label><br>
      <input
        type="number"
        :value="modelValue.round_number"
        @input="update('round_number', +$event.target.value)"
      />
    </div>

    <div>
      <label>총 회차</label><br>
      <input
        type="number"
        :value="modelValue.total_round"
        @input="update('total_round', +$event.target.value)"
        class="border p-2 w-full"
      />
    </div>

    <div>
      <label>목표 금액</label><br>
      <input
        type="number"
        :value="modelValue.goal_amount"
        @input="update('goal_amount', +$event.target.value)"
        class="border p-2 w-full"
      />
    </div>
  </div>
</template>

<script setup>
const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const update = (key, value) => {
  emit('update:modelValue', {
    ...props.modelValue,
    [key]: value,
  })
}
</script>

<style scoped>
.saving{
  margin-top:25px;
}
.saving-title{
  margin-bottom:15px;
}
input{
  border:1px solid #aaa;
  padding:5px 10px;
  width:500px;
  height:35px;
  margin-top:5px;
  margin-bottom:15px;
}
select{
  border:1px solid #aaa;
  height:35px;
  width:500px;
  margin-top:5px;
  margin-bottom:15px;
}
</style>
