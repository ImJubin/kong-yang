
<template>
  <div class = "update">
    <div class="tabs">
      <button :class="{ active: activeTab === 'info' }" @click="activeTab = 'info'">회원정보 수정</button>
      <button :class="{ active: activeTab === 'password' }" @click="activeTab = 'password'">비밀번호 변경</button>
    </div>
    <div class="tab-content">
      <UserInfoForm v-if="activeTab === 'info'" />
      <PasswordChangeForm v-if="activeTab === 'password'" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import UserInfoForm from '@/components/UserInfoForm.vue'
import PasswordChangeForm from '@/components/PasswordChangeForm.vue'

const activeTab = ref('info')
</script>

<style scoped>
button{
  border:none;
  background-color: #fff;
  padding:5px 15px;
  margin-top: 15px;;
  margin-bottom:35px;

}
button.active{
  border-bottom:3px solid #FDC200;
}
.update{
  width:1200px;
  margin:30px 38%;

}
</style>

