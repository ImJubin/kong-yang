<template>
  <div>
    <ul>
      <li v-for="article in store.articles" :key="article.id">
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        <!-- ✅ 수정 / 삭제 버튼 -->
        <button @click="goEdit(article.id)">수정</button> |
        <button @click="deleteArticle(article.id)">삭제</button>
      </li>
    </ul>
    <!-- 
    <RouterLink :to="{ name: 'create' }"> [글쓰기] </RouterLink> -->
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useArticleStore } from "@/stores/articles";
import { RouterLink } from "vue-router";

const router = useRouter();
const store = useArticleStore();

// 이동: 수정 페이지로
const goEdit = (articleId) => {
  router.push({ name: "ArticleUpdateView", params: { id: articleId } });
};

// 삭제
const deleteArticle = async (articleId) => {
  if (confirm("정말 삭제할까요?")) {
    await store.deleteArticle(articleId);
    store.getArticles(); // 삭제 후 목록 새로고침
  }
};
onMounted(async () => {
  const res = await axios.get("http://localhost:8000/api/v1/posts/");
  posts.value = res.data;
});
</script>

<style lang="scss" scoped></style>
