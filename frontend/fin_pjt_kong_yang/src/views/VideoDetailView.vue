<template>
  <div v-if="video" id = "video-detail">
    <iframe
    width="560"
    height="315"
    :src="`https://www.youtube.com/embed/${videoId}`"
    frameborder="0"
    allowfullscreen
    ></iframe>
    
    <h2 class = "video-title">{{ video.snippet.title }}</h2>
    <div class = "description_sub">
      <div class = "left">
      <p class="publishedAt">게시 시간 : {{ video.snippet.publishedAt }}</p>
      <p class="channelTitle">게시자 : {{ video.snippet.channelTitle }}</p>
      </div>
      <div class = "right">
      <button class = "save-button" @click="toggleSave"
      v-if="userStore.isLoggedIn">
        {{ isSaved ? '저장 취소' : '저장 하기' }}
      </button>
      </div>
    </div>
    <div class = "line"></div>
    <p class="description">{{ video.snippet.description }}</p>

  </div>

  <div v-else>
    <p>로딩 중...</p>
  </div>
</template>


<script setup>
import { useRoute } from 'vue-router'
import { useYoutubeStore } from '@/stores/YoutubeStore.js'
import { onMounted, computed, ref } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

const route = useRoute()
const store = useYoutubeStore()

const videoId = route.params.videoId
const video = ref(null)

// 저장 여부 확인
const isSaved = computed(() =>
  store.laterVideos.some(v => {
    const savedId = typeof v.id === 'object' ? v.id.videoId : v.id
    return savedId === videoId
  })
)

onMounted(async () => {
  const API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY
  const url = `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=${API_KEY}`
  const res = await fetch(url)
  const data = await res.json()
  video.value = data.items[0]
})

// 저장 토글
const toggleSave = function () {
    console.log(video)
  if (!video.value) return
  const videoData = { ...video.value, id: videoId }
  if (isSaved.value) {
    store.removeLaterVideo(videoId)
  } else {
    store.saveLaterVideo(videoData)
  }
}
</script>


<style scoped>
#video-detail{
  margin:50px auto;
  width:1200px;
  color:#333;

}
#video-detail iframe {
  border-radius: 12px;
  width: 100%;
  height: 600px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  margin:50px 0;
}
.description {
  white-space: pre-wrap;
  line-height: 1.6;
  color: #444;
}
.description_sub{
  display: flex;
  width:100%;
  margin-top:25px;
}
.left{
  width:300px;
}
.left>p{
  line-height:2;
  }
  .right{
    width:1000px;
    /* right:0%; */
    text-align: right;
}
.line{
  border-top:1px solid #aaa;
  margin:25px 0;
}

.save-button {
  background-color: #555;
  color:#fff;
  /* margin-top: 20px; */
  padding: 10px;
  border: none;
  border-radius: 3px;
  width:100px;
  /* height:px; */
  margin-top:33px;
  transition: all 0.2s ease;
}
.save-button:hover {
  background-color: #ccc;
  color: #333;
  transition: all 0.2s ease;
}
</style>

