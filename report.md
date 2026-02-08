# Report — LLM per Operations Research (Survey + 2 case study)

Repo: `/Users/paolo.bonicco/Library/Mobile Documents/com~apple~CloudDocs/Università/Materie/OC/Tesina/`

## Deliverable
- Slidev deck: `/Users/paolo.bonicco/Library/Mobile Documents/com~apple~CloudDocs/Università/Materie/OC/Tesina/deck/slides.md`
- Asset figure: `/Users/paolo.bonicco/Library/Mobile Documents/com~apple~CloudDocs/Università/Materie/OC/Tesina/deck/public/fig/`

## Quickstart (locale)
```bash
cd deck
npm install
npm run dev
```

Nota: in questo ambiente il registry npm è bloccato (ENOTFOUND su `registry.npmjs.org`), quindi `npm install` qui non funziona.

---

## Abstract del talk (5–8 righe)
Questa presentazione (~20 minuti) introduce come i Large Language Models (LLM) vengono studiati e applicati in Operations Research (OR), seguendo come “spina dorsale” il survey di Wang & Li. Il survey organizza la letteratura in tre pathways: automatic modeling, LLM-assisted optimization e direct solving, mettendo in evidenza opportunità e limiti. La seconda parte discute due casi studio concreti: OR-LLM-Agent (Zhang et al.), che formalizza un workflow agentico con esecuzione e debugging per automatizzare modeling+solving, e “Bridging LLMs & Optimization” (Jiang et al.), che propone un framework end-to-end per collegare descrizioni testuali a componenti di ottimizzazione. Si conclude con una sintesi delle sfide aperte (benchmark/metriche, robustezza e deployment) ancorate al survey.

---

## Outline + timing (target 20 min)

| Slide | Titolo (deck) | Obiettivo | Tempo |
|---:|---|---|---:|
| 1 | Titolo / Setup | Contesto + paper | 1:00 |
| 2 | Perché OR + LLM adesso | Motivazione + framing | 2:00 |
| 3 | Survey: 3 pathways (mappa mentale) | Tassonomia | 2:00 |
| 4 | Pathway 1 — closed-loop | Pipeline + perché | 2:00 |
| 5 | Automatic modeling: famiglie di metodi | Trade-off | 2:00 |
| 6 | Pathway 2 — LLM-assisted optimization | LLM + solver loop | 2:00 |
| 7 | Direct solving: single-modal + technique-enhanced | Setting + limiti | 2:00 |
| 8 | Valutazione + sfide aperte | Benchmark/metriche/deploy | 2:00 |
| 9 | Case study 1 — OR-LLM-Agent | Architettura | 2:00 |
| 10 | OR-LLM-Agent: debugging loop + benchmark | Alg.1 + esperimenti | 2:00 |
| 11 | Case study 2 — Bridging | Framework + Fig.1 | 2:00 |
| 12 | Jiang: esperimenti + collegamento al survey | Messaggio + takeaways | 2:00 |
| 13 | Sintesi + direzioni future | Takeaways + sfide | 1:30 |
| 14 | References | Bib | 0:30 |

---

## Speaker script (slide-by-slide) + evidence

### Slide 1 — Titolo / Setup
**Script:** “Tema: LLM per OR. Prima parte: survey (Wang&Li). Seconda parte: due esempi concreti (Zhang; Jiang). Regola: ogni claim è attribuito e citato.”

### Slide 2 — Perché OR + LLM adesso
**Script:** “Il survey inquadra OR come area dove modellazione e solving richiedono expertise; gli autori motivano perché LLM potrebbero aiutare nel passaggio semantica→struttura, ma evidenziano la necessità di loop di verifica.”

**Evidence/Citations:**
- [Wang&Li 2025 (arXiv:2509.18180v3), Abstract, PDF p.1]
- [Wang&Li 2025 (arXiv:2509.18180v3), Sec.1, PDF p.1]

### Slide 3 — Survey: 3 pathways
**Script:** “Spina dorsale: tassonomia in tre pathways. La userò per agganciare sia i risultati del survey sia i case study.”

**Evidence/Citations:**
- [Wang&Li 2025 (arXiv:2509.18180v3), Fig.1, PDF p.2]

### Slide 4 — Pathway 1 (closed-loop)
**Script:** “Automatic modeling: dall’input testuale al modello OR eseguibile. Punto chiave: framework closed-loop generate–validate–repair per ridurre errori.”

**Evidence/Citations:**
- [Wang&Li 2025 (arXiv:2509.18180v3), Fig.2, PDF p.3]

### Slide 5 — Famiglie metodi + trade-off
**Script:** “Il survey raggruppa approcci per automatic modeling; messaggio: trade-off tra rapidità (prompting), costo di adattamento (fine-tuning), e controllabilità (knowledge-guided).”

**Evidence/Citations:**
- [Wang&Li 2025 (arXiv:2509.18180v3), Table 1, PDF p.3]
- [Wang&Li 2025 (arXiv:2509.18180v3), Table 2, PDF p.4]

### Slide 6 — Pathway 2 (LLM-assisted optimization)
**Script:** “Qui l’LLM è un co-pilota: genera euristiche/strategie; il solver valuta e la pipeline itera.”

**Evidence/Citations:**
- [Wang&Li 2025 (arXiv:2509.18180v3), Fig.3, PDF p.6]
- [Wang&Li 2025 (arXiv:2509.18180v3), Table 3, PDF p.6] / [Table 4, PDF p.8] / [Table 5, PDF p.9]

### Slide 7 — Pathway 3 (direct solving)
**Script:** “Direct solving: in alcuni setting l’LLM produce direttamente la soluzione. Il survey distingue anche varianti technique-enhanced (iterazione, meta-prompt, multi-round, ecc.) e discute limiti su vincoli e verificabilità.”

**Evidence/Citations:**
- [Wang&Li 2025 (arXiv:2509.18180v3), Table 6, PDF p.10]
- [Wang&Li 2025 (arXiv:2509.18180v3), PDF p.10] — esempi di technique-enhanced (meta-prompt, iterazione, multi-*, ecc.).

### Slide 8 — Valutazione + sfide
**Script:** “Valutare è difficile: benchmark frammentati e metriche non uniformi. Il survey sottolinea anche problemi di deployment e auditabilità.”

**Evidence/Citations:**
- [Wang&Li 2025 (arXiv:2509.18180v3), Sec.5, PDF p.13]

### Slide 9 — OR-LLM-Agent: idea e architettura
**Script:** “Zhang et al. propongono OR-LLM-Agent: un workflow agentico che separa modeling, code generation e debugging, ancorando il processo all’esecuzione.”

**Evidence/Citations:**
- [Zhang et al. 2025 (arXiv:2503.10009v3), Abstract, PDF p.1]
- [Zhang et al. 2025 (arXiv:2503.10009v3), Fig.2, PDF p.2]

### Slide 10 — OR-LLM-Agent: debugging loop + BWOR
**Script:** “Debugging: esegui, osservi errori/violazioni, e ripari in loop. Alg.1 formalizza la strategia. Gli autori riportano benchmark e confronti (reasoning vs non-reasoning) su più dataset, includendo BWOR.”

**Evidence/Citations:**
- [Zhang et al. 2025 (arXiv:2503.10009v3), Alg.1, PDF p.3]
- [Zhang et al. 2025 (arXiv:2503.10009v3), PDF p.1] — riferimento/link a BWOR nel paper.
- [Zhang et al. 2025 (arXiv:2503.10009v3), PDF p.5] — esperimenti e confronti.

### Slide 11 — Jiang: obiettivo e framework
**Script:** “Jiang et al. propongono un bridge end-to-end: LNCS (Language-based Neural COP Solver) codifica istanze testuali in uno spazio semantico e usa un generator; gli autori descrivono anche un training con conflict-free multi-task RL. Fig.1 riassume la pipeline.”

**Evidence/Citations:**
- [Jiang et al. 2024 (arXiv:2408.12214v2), Abstract, PDF p.1]
- [Jiang et al. 2024 (arXiv:2408.12214v2), Fig.1, PDF p.3]

### Slide 12 — Jiang: esperimenti + link al survey
**Script:** “Gli autori riportano risultati su più COP e discutono generalizzabilità; mostro una tabella con metriche tipo Gap (TSP/CVRP/KP). Chiudo collegando al survey: evaluation e feasibility restano centrali.”

**Evidence/Citations:**
- [Jiang et al. 2024 (arXiv:2408.12214v2), Abstract, PDF p.1] — claim SOTA + generalizability (attribuito).
- [Jiang et al. 2024 (arXiv:2408.12214v2), Table 4, PDF p.7] — tabella con Gap su TSP/CVRP/KP.
- [Wang&Li 2025 (arXiv:2509.18180v3), Sec.5, PDF p.13] — sfide evaluation/deployment (ancoraggio).

### Slide 13 — Sintesi + direzioni future
**Script:** “Tre takeaway: closed-loop verificabile; ibridi LLM+solver per affidabilità; direct solving richiede evaluation rigorosa. Tre sfide: benchmark/metriche, robustezza, deployment. I due case study attaccano due punti diversi: repair loop vs bridge end-to-end.”

**Evidence/Citations:**
- [Wang&Li 2025 (arXiv:2509.18180v3), Fig.2, PDF p.3] + [Zhang et al. 2025 (arXiv:2503.10009v3), Alg.1, PDF p.3] — closed-loop + repair.
- [Wang&Li 2025 (arXiv:2509.18180v3), Fig.3, PDF p.6] — ibridi LLM+solver.
- [Wang&Li 2025 (arXiv:2509.18180v3), Sec.5, PDF p.13] — sfide evaluation/deployment.
- [Jiang et al. 2024 (arXiv:2408.12214v2), Abstract, PDF p.1] + [Fig.1, PDF p.3] — bridge end-to-end.

### Slide 14 — References
**Script:** “Riferimenti principali.”

---

## TODO prima della consegna (audit)
1) Sostituire i placeholder in `deck/public/fig/` con le figure reali (e aggiornare “Source: …” se serve).
2) Completare i “TODO (audit)” nelle NOTE delle slide (numeri figura/tabella, pagine PDF se richieste).
3) Se si aggiungono numeri/metriche, riportare sempre metrica + benchmark + setting e citare tabella/figura specifica.

---

## Appendice: claim ledger (portanti)

1) **Tassonomia in 3 pathways** → [Wang&Li 2025 (arXiv:2509.18180v3), Fig.1, PDF p.2]  
2) **Closed-loop per automatic modeling** → [Wang&Li 2025 (arXiv:2509.18180v3), Fig.2, PDF p.3]  
3) **LLM-assisted optimization: approcci principali** → [Wang&Li 2025 (arXiv:2509.18180v3), Fig.3, PDF p.6]  
4) **Direct solving overview** → [Wang&Li 2025 (arXiv:2509.18180v3), Table 6, PDF p.10]  
5) **OR-LLM-Agent come pipeline agentica (NL→model→code→debug)** → [Zhang et al. 2025 (arXiv:2503.10009v3), Abstract, PDF p.1; Fig.2, PDF p.2]  
6) **Debugging loop formalizzato** → [Zhang et al. 2025 (arXiv:2503.10009v3), Alg.1, PDF p.3]  
7) **Jiang: framework unificato end-to-end** → [Jiang et al. 2024 (arXiv:2408.12214v2), Abstract, PDF p.1; Fig.1, PDF p.3]  

---

## Bibliografia

- Wang, Yang; Li, Kai. *Large Language Models in Operations Research: Methods, Applications, and Challenges*. arXiv:2509.18180v3 (2025).
- Zhang, Bowen; Luo, Pengcheng; Yang, Genke; Soong, Boon-Hee; Yuen, Chau. *OR-LLM-Agent: Automating Modeling and Solving of Operations Research Optimization Problems with Reasoning LLM*. arXiv:2503.10009v3 (2025).
- Jiang, Xia; Wu, Yaoxin; Wang, Yuan; Zhang, Yingqian. *Bridging Large Language Models and Optimization: A Unified Framework for Text-attributed Combinatorial Optimization*. arXiv:2408.12214v2 (2024).
