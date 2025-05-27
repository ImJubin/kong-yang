<template>
  <div id = "sign-up">
    <h1 class = "title">회원가입</h1>
    <form @submit.prevent="signUp">

      <label for="username">아이디 <span class = "require">*</span></label><br />
      <input id="username" v-model="username" placeholder="ex.userId"/>
      <p v-if="showError && !username" class="error-msg">이 칸은 비어있을 수 없습니다.</p><br />

      <label for="email">이메일 <span class = "require">*</span></label><br />
      <input id="email" v-model="email" placeholder="ex. abcd@email.com"/>
      <p v-if="showError && !email" class="error-msg">이 칸은 비어있을 수 없습니다.</p><br />

      <label for="password">비밀번호 <span class = "require">*</span></label><br />
      <input id="password" v-model="password" type="password" placeholder="8자리 이상 영문, 숫자 혼합"/>
      <p v-if="showError && !password" class="error-msg">이 칸은 비어있을 수 없습니다.</p><br />

      <label for="password2">비밀번호 확인 <span class = "require">*</span></label><br />
      <input id="password2" v-model="password2" type="password" placeholder="8자리 이상 영문, 숫자 혼합"/>
      <p v-if="showError && !password2" class="error-msg">이 칸은 비어있을 수 없습니다.</p>
      <p v-if="passwordMismatch" class="error-msg">비밀번호가 일치하지 않습니다.</p><br />

      <label for="first_name">이름 <span class = "require">*</span></label><br />
      <input id="first_name" v-model="first_name" placeholder="싸피"/>
      <p v-if="showError && !first_name" class="error-msg">이 칸은 비어있을 수 없습니다.</p><br />

      <label for="last_name">성 <span class = "require">*</span></label><br />
      <input id="last_name" v-model="last_name" placeholder="김"/>
      <p v-if="showError && !last_name" class="error-msg">이 칸은 비어있을 수 없습니다.</p><br />

      <label for="phone_number">전화번호 <span class = "require">*</span></label><br />
      <input id="phone_number" v-model="phone_number" placeholder="- 없이 입력"/>
      <p v-if="showError && !phone_number" class="error-msg">이 칸은 비어있을 수 없습니다.</p><br />

      <button type="submit">회원가입</button>
    </form>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from "vue-router";
const router = useRouter()

const userStore = useUserStore()

const username = ref('')
const email = ref('')
const password = ref('')
const password2 = ref('')
const first_name = ref('')
const last_name = ref('')
const phone_number = ref('')

const showError = ref(false)

// 비밀번호 불일치 여부
const passwordMismatch = computed(() =>
  password.value && password2.value && password.value !== password2.value
)

const signUp = async () => {
  // 필수 필드 체크
  if (
    !username.value ||
    !email.value ||
    !password.value ||
    !password2.value ||
    !first_name.value ||
    !last_name.value ||
    !phone_number.value
  ) {
    showError.value = true
    return
  }

  if (passwordMismatch.value) {
    showError.value = true
    return
  }

  try {
    await userStore.signUp({
      username: username.value,
      email: email.value,
      password: password.value,
      password2: password2.value,
      first_name: first_name.value,
      last_name: last_name.value,
      phone_number: phone_number.value
    })
    router.push({ name: 'LandingPage' }) 
  } 
  
  // 로그인 실패인 경우
  catch (err) {
  const errors = err.response?.data

  if (errors) {
    const messages = Object.entries(errors)
      .map(([field, msgs]) => `${field}: ${msgs.join(', ')}`)
      .join('\n')

    alert(`회원가입에 실패했습니다:\n${messages}`)
  } else {
    alert('알 수 없는 오류가 발생했습니다.')
  }
  console.error('전체 에러:', err)
  console.error('회원가입 실패:', err.response?.data)
}
}
</script>

<style scoped>
*{
  color:#333;
}
.require {
    color:red;
}
.error-msg {
  color: red;
  font-size: 0.85rem;
  margin: 2px 0;
}
#sign-up{
  width:350px;
  margin: 80px auto;

}
.title{
  text-align: center;
}
form{
  margin-top:25px;

}
input{
  width: 100%;
  padding: 0.7rem 0.5rem;
  margin: 0.2rem 0 1rem;
  border-radius: 3px;
  border:1px solid #aaa;
  width:350px;

}
button {
  padding: 0.5rem 1rem;
  width:350px;
  margin-top:20px;
  background-color: #555;
  color:#fff;
  font-size: 16px;
  border:none;
  transition: all 0.2s ease;
  border-radius: 3px;
  padding:13px 80px;
}
button:hover{
  background-color: #ccc;
  color: #333;
  transition: all 0.2s ease;
}
</style>