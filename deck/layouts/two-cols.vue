<script setup lang="ts">
const props = defineProps({
  class: {
    type: String,
  },
  layoutClass: {
    type: String,
  },
})
</script>

<template>
  <div class="slidev-layout two-columns w-full h-full flex flex-col deck-layout" :class="props.layoutClass">
    <div v-if="$frontmatter.kicker && !$frontmatter.hideKicker" class="kicker deck-kicker">
      {{ $frontmatter.kicker }}
    </div>
    <div class="w-full flex-1 grid grid-cols-2 min-h-0">
      <div class="col-left min-h-0" :class="props.class">
        <slot />
        <slot name="left" />
      </div>
      <div class="col-right min-h-0" :class="props.class">
        <slot name="right" />
      </div>
    </div>
  </div>
</template>

