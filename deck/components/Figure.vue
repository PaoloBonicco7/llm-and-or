<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  src: {
    type: String,
    required: true,
  },
  alt: {
    type: String,
    default: '',
  },
  maxHeight: {
    type: [String, Number],
    default: '',
  },
  description: {
    type: String,
    default: '',
  },
  caption: {
    type: String,
    default: '',
  },
  source: {
    type: String,
    default: '',
  },
})

const figureCaption = computed(() => props.caption || props.description)

const imgStyle = computed(() => {
  if (!props.maxHeight)
    return undefined
  const maxHeight = typeof props.maxHeight === 'number' ? `${props.maxHeight}px` : props.maxHeight
  return { maxHeight }
})
</script>

<template>
  <figure class="deck-figure">
    <img :src="props.src" :alt="props.alt" :style="imgStyle">

    <figcaption v-if="figureCaption" class="deck-figure__caption" v-html="figureCaption" />

    <figcaption v-if="$slots.source || props.source" class="small-source">
      Source:
      <slot name="source">{{ props.source }}</slot>
    </figcaption>
  </figure>
</template>
