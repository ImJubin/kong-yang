<template>
  <form @submit.prevent="onSubmit" class="form-container">
    <h2>회원정보 수정</h2>

    <label>
      아이디 (수정 불가)<br>
      <input type="text" v-model="form.username" readonly />
    </label>

    <label>
      이름<br>
      <input type="text" v-model="form.first_name" required />
    </label>

    <label>
      성<br>
      <input type="text" v-model="form.last_name" required />
    </label>

    <label>
      이메일<br>
      <input type="email" v-model="form.email" required />
    </label>

    <label>
      전화번호<br>
      <input type="text" v-model="form.phone_number" required />
    </label>

    <button type="submit">저장</button>

    <p v-if="successMessage" class="success">{{ successMessage }}</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </form>
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

const form = reactive({
  username: '',
  first_name: '',
  last_name: '',
  email: '',
  phone_number: ''
})

const successMessage = ref('')
const errorMessage = ref('')

onMounted(() => {
  if (userStore.user) {
    Object.assign(form, userStore.user)
  }
})

const onSubmit = async () => {
  const result = await userStore.updateUserInfo({
    first_name: form.first_name,
    last_name: form.last_name,
    email: form.email,
    phone_number: form.phone_number,
  })

  if (result.success) {
    successMessage.value = '회원 정보가 수정되었습니다.'
    errorMessage.value = ''
  } else {
    errorMessage.value = '수정 실패: ' + (result.message?.detail || '오류 발생')
    successMessage.value = ''
  }
}
</script>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 400px;
}

input {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  width:100%;
  margin-top:8px;
  height:45px;
}

button {
  height:45px;
  padding: 0.6rem;
  background-color: #555;
  color:#fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top:30px;
  transition: all 0.2s ease;
}
button:hover{
  background-color: #ccc;
  color: #333;
  transition: all 0.2s ease;
}

.success {
  color: green;
}

.error {
  color: red;
}
</style>
