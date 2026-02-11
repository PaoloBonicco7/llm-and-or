# Slidev deck — LLM per Operations Research

Deck Slidev per la presentazione.

## Struttura
- `slides.md` è l’entrypoint e importa le sezioni da `pages/`
- `pages/` contiene le slide divise per capitoli (più facile da mantenere)
- `components/` contiene componenti riusabili (es. `Callout`, `Figure`)
- `layouts/` override di layout base (default, two-cols, section) per supportare `kicker:` in frontmatter

## Prerequisiti
- Node.js + npm

## Avvio
```bash
npm ci
npm run dev
```

## Build / export
```bash
npm run build
npm run export
```
