<template>
  <footer
    v-if="!$frontmatter.hideFooter && $nav.currentLayout !== 'cover' && $nav.currentLayout !== 'section'"
    class="deck-footer"
  >
    <div class="deck-footer__right">
      {{ $nav.currentPage }} / {{ $nav.total }}
    </div>
    <div class="deck-footer__bar" aria-hidden="true">
      <div
        class="deck-footer__barFill"
        :style="{ width: $nav.total ? `${($nav.currentPage / $nav.total) * 100}%` : '0%' }"
      />
    </div>
  </footer>
</template>
