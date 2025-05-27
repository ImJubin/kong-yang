
<template>
  <div class="deposit">
    <h4 class="deposit-title">예금 상품 정보</h4>

    <div>
      <label>상품명</label><br>
      <input :value="modelValue.product_name" @input="update('product_name', $event.target.value)" />
    </div>

    <div>
      <label>금리 (%)</label><br>
      <input type="number" :value="modelValue.interest_rate" @input="update('interest_rate', +$event.target.value)" />
    </div>

    <div>
      <label>기간 (개월)</label><br>
      <input type="number" :value="modelValue.duration_months" @input="update('duration_months', +$event.target.value)" />
    </div>

    <div>
      <label>시작일</label><br>
      <input type="date" :value="modelValue.started_at" @input="update('started_at', $event.target.value)" />
    </div>

    <div>
      <label>만기일</label><br>
      <input type="date" :value="modelValue.ends_at" @input="update('ends_at', $event.target.value)" />
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
.deposit{
  margin-top:25px;
}
.deposit-title{
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