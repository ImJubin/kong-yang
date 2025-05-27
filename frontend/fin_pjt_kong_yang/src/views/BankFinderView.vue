<template>
    <div id = "bank-finder">
      <h2 class = "title">은행 위치 조회</h2>
      <MapSearch />
    </div>
</template>

<script setup>
import MapSearch from '@/components/MapSearch.vue'
</script>
<style scoped>
#bank-finder{
  width: 1200px;
  margin: 80px auto;
}
*{
  color:#333;
  }
</style>
