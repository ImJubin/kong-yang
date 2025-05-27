<!-- src/components/CountUp.vue -->
<template>
  <span>{{ formattedNumber }}</span>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

const props = defineProps({
  end: { type: Number, required: true },
  duration: { type: Number, default: 2000 },
  decimals: { type: Number, default: 0 }
})

const number = ref(0)

const formattedNumber = computed(() => {
  return number.value.toFixed(undefined, {
    minimumFractionDigits: props.decimals,
    maximumFractionDigits: props.decimals
  })
})

onMounted(() => {
  const startTime = performance.now()
  const startValue = 98615299

  const animate = (currentTime) => {
    const elapsed = currentTime - startTime
    const progress = Math.min(elapsed / props.duration, 1)
    number.value = startValue + progress * (props.end - startValue)

    if (progress < 1) {
      requestAnimationFrame(animate)
    }
  }

  requestAnimationFrame(animate)
})
</script>
