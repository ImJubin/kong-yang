<template>
  <div id="mypage-container">
    
    <div v-if="userStore.user">
      <div class = "profile">
        <div class = "profile-name">
      <p class = "user-name">{{ userStore.user.username }}</p>
      <h1 class = "hello"><span class = "name">{{ userStore.user.last_name }} {{ userStore.user.first_name }}</span> 님 안녕하세요!</h1>
      
      <div class = "user-info">
        <p>{{ userStore.user.email }}</p>
        <p>{{ userStore.user.phone_number }}</p>
      </div>
        <p><RouterLink :to="{ name: 'UpdateMyData' }" class = "change">회원 정보 수정</RouterLink></p>
      </div>
    </div>
      <div class = "my-pages">
        <InterestComparisonChart />
        <AccountOverview />
      </div>
      <button class = "delete" @click="handleDelete">회원 탈퇴</button>


    </div>
    
    <div v-else>
      <p>유저 정보를 불러오는 중이거나 로그인되지 않았습니다.</p>
    </div>
  </div>
</template>


<script setup>
import { ref } from "vue";
import { useUserStore } from '@/stores/user'
import AccountOverview from '@/components/AccountOverview.vue'
import InterestComparisonChart from '@/components/InterestComparisonChart.vue'

const userStore = useUserStore()
const showAccountForm = ref(false)

const handleDelete = () => {
  if (confirm('정말 탈퇴하시겠어요?')) {
    userStore.deleteUser()
  }
}
</script>

<style scoped>
#mypage-container {
  width:1200px;
  margin: 30px auto;
}
.delete{
  color:red;
  background-color: #fff;
  border:none;
  /* border-bottom:1px solid red; */
  font-size:16px;
}
.user-name{
  color:#aaa;
  font-weight: 600;
  text-indent: 5px;;
}
.hello{
  font-size:28px;
}
.name{
  font-size:32px;
}
.my-pages{
  display:flex;
}
.account-overview{
  width:70%;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 0.75rem;
}
strong {
  display: inline-block;
  width: 120px;
}
.profile{
  display: relative;
  margin-bottom:20px;
  width:100%
}
.user-info{
  position: absolute;
  bottom:0%;
  left:29%;

}
.user-info>p{
  display: inline-block;
  color:#888;
  
}
.change{
  position: absolute;
  bottom:0%;
  right:0%

}
.profile-name{
  position: relative;
  width:100%;
}
</style>