<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  cols: {
    type: [Number, String],
    default: 3,
  },
})

const isTwoCols = computed(() => Number(props.cols) === 2)
</script>

<template>
  <div class="card-grid" :class="{ two: isTwoCols }">
    <slot />
  </div>
</template>

