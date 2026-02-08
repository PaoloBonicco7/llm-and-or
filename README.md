# LLM per Operations Research — Slidev deck

Repository per gestire una presentazione (Slidev) su alcuni paper di *LLM + Operations Research*.

## Struttura

- `deck/` — progetto Slidev (slide + assets)
- `report.md` — outline + speaker notes / evidence

I PDF dei paper sono tenuti in locale e ignorati da Git (vedi `.gitignore`). Se vuoi versionarli, valuta **Git LFS**.

## Requisiti

- Node.js + npm

## Uso (sviluppo)

```bash
cd deck
npm ci
npm run dev
```

## Build / export

```bash
cd deck
npm run build
npm run export
```

L’export genera tipicamente un file tipo `slides-export.pdf` dentro `deck/` (ignorato da Git).
