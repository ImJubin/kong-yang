<template>
  <div class="detail-container">
    <div class="article-box">
      <h2 class="text-2xl font-bold mb-2">{{ article.title }}</h2>
      <p class="article-content">{{ article.content }}</p>

      <div class="button-group">
        <RouterLink
          :to="{ name: 'ArticleUpdateView', params: { id: article.id } }"
        >
          <button class="btn yellow-btn">✏ 수정</button>
        </RouterLink>
        <button class="btn gray-btn" @click="deleteArticle">🗑 삭제</button>
      </div>
      <div class="comment-box">
        <h3 class="comment-title">💬 댓글</h3>
        <ul class="comment-list">
          <li
            v-for="comment in comments"
            :key="comment.id"
            class="comment-item"
          >
            <div class="comment-content">
              {{ comment.content }}
            </div>
            <span> ❤️ {{ comment.likes }}</span>
            <button class="btn yellow-btn" @click="likeComment(comment.id)">
              좋아요
            </button>
          </li>
        </ul>
        <!-- 댓글 작성 -->
        <form @submit.prevent="createComment" class="comment-form">
          <textarea
            v-model="newComment"
            class="comment-input"
            placeholder="댓글을 입력하세요"
            required
          ></textarea>
          <button type="submit" class="btn yellow-btn w-full">댓글 작성</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import { useArticleStore } from "@/stores/articles";

const route = useRoute();
const router = useRouter();
const store = useArticleStore();

const article = ref({});
const comments = ref([]);
const newComment = ref("");

// 게시글 + 댓글 불러오기
onMounted(async () => {
  const res = await axios.get(
    `${store.API_URL}/api/v1/articles/${route.params.id}/`
  );
  article.value = res.data;

  const resComment = await axios.get(
    `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`
  );
  comments.value = resComment.data;
});

// 게시글 삭제
const deleteArticle = async () => {
  if (confirm("정말 삭제할까요?")) {
    await axios.delete(`${store.API_URL}/api/v1/articles/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${sessionStorage.getItem("authToken")}`,
      },
    });
    router.push({ name: "ArticleList" });
  }
};

// 댓글 작성
const createComment = async () => {
  const res = await axios.post(
    `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
    {
      content: newComment.value,
    },
    {
      headers: {
        Authorization: `Token ${sessionStorage.getItem("authToken")}`,
      },
    }
  );
  comments.value.push(res.data);
  newComment.value = "";
};

// 댓글 좋아요
const likeComment = async (commentId) => {
  const res = await axios.post(
    `${store.API_URL}/api/v1/comments/${commentId}/like/`,
    {},
    {
      headers: {
        Authorization: `Token ${sessionStorage.getItem("authToken")}`,
      },
    }
  );
  const updated = res.data;
  const idx = comments.value.findIndex((c) => c.id === commentId);
  if (idx !== -1) {
    comments.value[idx].likes = updated.likes;
  }
};
</script>

<style scoped>
textarea {
  width: 100%;
  height: 80px;
  margin-top: 8px;
  margin-bottom: 8px;
}
.detail-container {
  max-width: 700px;
  margin: 0 auto;
  padding: 2rem;
  font-family: "Noto Sans KR", sans-serif;
  color: #333;
  width: 100%;
  height: 80px;
  margin-top: 8px;
  margin-bottom: 8px;
}

.article-box {
  background-color: #fafafa;
  border: 1px solid #ddd;
  border-radius: 1rem;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 2px 8px rgba(170, 170, 170, 0.15);
}

.article-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.article-content {
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.button-group {
  display: flex;
  gap: 0.5rem;
}

.btn {
  border: none;
  border-radius: 8px;
  font-weight: bold;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: 0.2s;
  font-family: "Noto Sans KR", sans-serif;
}

.yellow-btn {
  background-color: #fdde88;
  color: #333;
}
.yellow-btn:hover {
  background-color: #ffdc52;
}

.gray-btn {
  background-color: #aaaaaa;
  color: white;
}
.gray-btn:hover {
  background-color: #888888;
}

.comment-box {
  background-color: white;
  border-radius: 1rem;
  padding: 1rem;
  border: 1px solid #eee;
  box-shadow: 0 2px 6px rgba(200, 200, 200, 0.1);
}

.comment-title {
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.comment-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.comment-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fafafa;
  padding: 0.5rem 1rem;
  border-radius: 8px;
}

.comment-content {
  flex-grow: 1;
  margin-right: 0.5rem;
}

.comment-input {
  width: 100%;
  height: 80px;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-family: "Noto Sans KR", sans-serif;
}

.w-full {
  width: 100%;
}
</style>
