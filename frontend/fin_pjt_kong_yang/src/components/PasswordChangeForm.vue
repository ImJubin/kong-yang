<template>
  <form @submit.prevent="onSubmit" class="form-container">
    <h2>비밀번호 변경</h2>

    <label>
      현재 비밀번호<br>
      <input type="password" v-model="form.old_password" required />
    </label>

    <label>
      새 비밀번호<br>
      <input type="password" v-model="form.new_password1" required />
    </label>

    <label>
      새 비밀번호 확인<br>
      <input type="password" v-model="form.new_password2" required />
    </label>

    <button type="submit">비밀번호 변경</button>

    <p v-if="successMessage" class="success">{{ successMessage }}</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </form>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

const form = reactive({
  old_password: '',
  new_password1: '',
  new_password2: ''
})

const successMessage = ref('')
const errorMessage = ref('')

const onSubmit = async () => {
  if (form.new_password1 !== form.new_password2) {
    errorMessage.value = '새 비밀번호가 일치하지 않습니다.'
    successMessage.value = ''
    return
  }

  const result = await userStore.changePassword({ ...form })

  if (result.success) {
    successMessage.value = '비밀번호가 성공적으로 변경되었습니다.'
    errorMessage.value = ''
    form.old_password = ''
    form.new_password1 = ''
    form.new_password2 = ''
  } else {
    errorMessage.value = '❌ 변경 실패: ' + (result.message?.detail || '오류 발생')
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
  width:100%;
  border-radius: 4px;
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