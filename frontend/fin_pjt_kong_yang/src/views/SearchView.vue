<template>
  <div id="search">

  
    <h2 class = "search_title">비디오 검색</h2>
    <input v-model="query" @keyup.enter="onSearch" class="search-input"></input>
    <button @click="onSearch" class = "search-btn">찾기</button>

    <div class="video-list">
      <div v-for="video in videos" :key="video.id.videoId" class="video-card">
    <router-link
    :to="{ name: 'VideoDetail', params: { videoId: video.id.videoId } }"
    class="video-card"
    >
    <img :src="video.snippet.thumbnails.medium.url" :alt="video.snippet.title" />
    <p>{{ video.snippet.title }}</p>
    </router-link>
      </div>
    </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const query = ref('');
const videos = ref([]);

const API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY;

const onSearch = async () => {
  if (!query.value) return;

  const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=8&q=${encodeURIComponent(query.value)}&type=video&key=${API_KEY}`;

  try {
    const res = await fetch(url)
    const data = await res.json()
    videos.value = data.items
  } catch (err) {
    console.error('유튜브 API 호출 실패:', err)
  }
}
</script>

<style scoped>
*{
  /* border:1px dashed red; */
  color:#333;
}
#search{
  width:1200px;
  margin:150px auto;
  text-align: center;

}
.search_title{
  text-align: center;
  margin-bottom:30px;
}

.search-btn {
  background-color: #555;
  color:#fff;
  padding: 10px;
  border: none;
  border-radius: 3px;
  width:100px;
  margin-left:15px;
  transition: all 0.2s ease;
  height:43px;
}
.search-btn:hover {
  background-color: #ccc;
  color: #333;
  transition: all 0.2s ease;
}

.search-input {
  padding: 8px;
  padding-left:15px;
  width: 500px;
  font-size: 16px;
  border:1px solid #333;
  border-radius: 3px;
}
.video-list {
  display: flex;
  flex-wrap: wrap;
  gap: 13px;
  margin-top:80px;

}

.video-card {
  width: 290px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s;
}

.video-card:hover {
  transform: scale(1.03);
}

.video-card img {
  width: 100%;
}

.video-card p {
  margin: 8px;
  font-size: 14px;
}
</style>