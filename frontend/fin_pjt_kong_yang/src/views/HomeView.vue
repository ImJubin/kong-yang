<script setup>
// import TheWelcome from '../components/TheWelcome.vue'
import { useUserStore } from '@/stores/user'
import MainCalendar from '@/components/MainCalendar.vue'
const userStore = useUserStore()
import axios from "axios";
import { onMounted } from "vue";
import { useArticleStore } from "@/stores/articles";
import { RouterLink } from "vue-router";
import { useRoute } from "vue-router";
import ArticleList from "@/components/ArticleList.vue";

// const store = getArticles();
const store = useArticleStore();
// const route = useRoute();

onMounted(() => {
  store.getArticles();
});
</script>

<template>
  <div>
    <RouterLink :to="{ name: 'create' }">게시글 생성하기</RouterLink>
    <ArticleList />
  </div>

</template>
<style scoped>
div{
  width: 1200px;
  margin: 30px auto;
}
a{
  display: block;
  text-align: right;
}
</style>