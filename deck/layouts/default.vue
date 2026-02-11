<template>
  <div class="slidev-layout default deck-layout">
    <div v-if="$frontmatter.kicker && !$frontmatter.hideKicker" class="kicker deck-kicker">
      {{ $frontmatter.kicker }}
    </div>
    <slot />
  </div>
</template>

