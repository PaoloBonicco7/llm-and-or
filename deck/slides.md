---
title: "LLM per Operations Research: metodi, applicazioni e sfide"
subtitle: "Survey (Wang & Li) + 2 case study (OR-LLM-Agent, Bridging LLMs & Optimization)"
theme: default
layout: cover
lineNumbers: false
---



<!-- ---- SLIDE 1 ---- -->
# LLM per Operations Research (OR)
## Metodi, applicazioni, sfide + esempi concreti

<small>Team research talk · Data · Nome presentatore</small>

<div class="mt-10 card-grid two">
  <div class="card">
    <div class="kicker">Paper principale (survey)</div>
    <h3>Wang &amp; Li (2025)</h3>
    <p><i>Large Language Models in Operations Research: Methods, Applications, and Challenges</i><br/>arXiv:2509.18180v3</p>
  </div>
  <div class="card">
    <div class="kicker">Approfondimenti (case study)</div>
    <p><b>Zhang et al. (2025)</b> — <i>OR-LLM-Agent</i> (arXiv:2503.10009v3)</p>
    <p class="mt-2"><b>Jiang et al. (2024)</b> — <i>Bridging LLMs &amp; Optimization</i> (arXiv:2408.12214v2)</p>
  </div>
</div>

<div class="so-what"><b>Flow (20 min):</b> perché OR+LLM → tassonomia (survey) → 2 casi studio → sfide aperte</div>

<!--
NOTE:
Obiettivo: presentazione ~20 min basata principalmente sul survey di Wang & Li, con 2 case study (Zhang et al., Jiang et al.).

Regole:
- Ogni claim non banale va attribuito ("gli autori propongono/riportano/mostrano...") + citazione.
- Evitare assoluti non supportati: usare formulazioni verificabili e contestualizzate (benchmark/setting).
-->

---



<!-- ---- SLIDE 2 ---- -->

<div class="kicker">Survey (Wang &amp; Li) — motivazione</div>

## Perché OR + LLM adesso

- **Limite dei metodi classici:** la pipeline OR è spesso *expert-driven* (modellazione + tuning manuale) → scala male con problemi **grandi**, **dinamici**, **multi-vincolo** e requisiti di **real-time**
- **Cosa abilitano gli LLM:** (1) **modellazione**: testo in linguaggio naturale → modello matematico e/o codice eseguibile; (2) **solving**: generano euristiche/strategie e si integrano con algoritmi/solver in loop di feedback
- **Obiettivo del survey:** risultati ancora “a silos” → unifica il panorama in 3 filoni (**automatic modeling**, **auxiliary/LLM-assisted optimization**, **direct solving**) e rivede benchmark, applicazioni e sfide

<div class="so-what"><b>Idea chiave:</b> collaborazione uomo–AI: l’LLM propone/struttura, il solver verifica (feasibility/qualità) → iterazioni “generate–validate–repair”.</div>

<!--
NOTE:
Script (≈30–40s):
- “La Ricerca Operativa è la cassetta degli attrezzi per decisioni con vincoli e trade-off: trasporti, supply chain, scheduling.”
- “Il workflow classico spesso dipende da esperti: tradurre requisiti in variabili/vincoli e poi fare tuning. Su problemi grandi o che cambiano, questo diventa difficile e poco ‘real-time’.”
- “Qui entrano gli LLM: possono trasformare testo in struttura (modello/codice) e possono collaborare col solver suggerendo euristiche o mosse da validare.”
- “Ma oggi la ricerca è frammentata: il valore del survey è mettere ordine in tre filoni e chiarire cosa funziona, come si valuta e quali sfide restano.”

Note per Q&A (una riga):
- Se chiedono “gli LLM risolvono da soli?”: il survey evidenzia anche instabilità e bisogno di validazione/controllo.

Evidence / Citations (paper principale):
- [Wang&Li 2025 (arXiv:2509.18180v3), Abstract, PDF p.1] — limiti OR classica; cosa abilitano gli LLM; obiettivo e tassonomia.
- [Wang&Li 2025 (arXiv:2509.18180v3), Sec.1, PDF p.1–2] — contesto (scala/dinamismo/real-time) + frammentazione e motivazione del survey.
-->

---

<div class="kicker">Survey (Wang &amp; Li) — fondamenti</div>

## Prima della tassonomia: perché OR e LLM “si incastrano”

- **Il cuore dell’OR:** **variabili** (decisioni) · **obiettivo** (min/max) · **vincoli** (regole) → un modello formale “risolvibile”
- **Trade-off classico:** metodi **esatti** (ottimo, ma costosi su larga scala) vs **euristiche/metaeuristiche** (scalano, ma senza garanzia di ottimo)
- **LLM come “ragionatori” + coders:** comprensione semantica → generazione strutturata (passi di ragionamento, pseudo-codice, Python/solver code)
- **Sinergia:** l’LLM rende “morbida” l’interfaccia uomo→modello (testo→struttura); l’OR/solver mantiene rigore e verifica (feasibility + qualità)

<div class="so-what"><b>Messaggio:</b> non è “LLM vs OR”, ma “LLM per portare problemi reali dentro modelli OR, con validazione automatica”.</div>

<!--
NOTE:
Script (≈40–50s):
- “Se devo riassumere l’ottimizzazione: scelgo variabili, definisco un obiettivo e rispetto vincoli.”
- “Poi arriva il compromesso: o garantisco l’ottimo ma rischio di non stare nei tempi, oppure uso euristiche che scalano ma non garantiscono l’ottimo.”
- “Gli autori sottolineano che gli LLM non sono solo ‘testo’: sono utili perché trasformano linguaggio naturale in strutture (modelli/codice) e supportano ragionamento controllato.”
- “La sinergia è qui: l’LLM traduce e propone; il solver verifica ed esegue. Quindi posso iterare e correggere.”

Evidence / Citations:
- [Wang&Li 2025 (arXiv:2509.18180v3), Sec.2.A, PDF p.2] — definizione OR (obiettivi/vincoli) e limiti al crescere della complessità.
- [Wang&Li 2025 (arXiv:2509.18180v3), Sec.2.B, PDF p.2–3] — LLM: mappare NL→struttura/codice; ragionamento e closed-loop (generate–validate–repair).

Nota:
- La frase “esatti vs euristiche” è background di corso; non è una specifica novità del survey.
-->

---

<div class="kicker">Survey (Wang &amp; Li) — tassonomia</div>

## Survey: 3 pathways (mappa mentale)

<div class="card-grid">
  <div class="card">
    <h3>1) Automatic modeling</h3>
    <p>Testo → formulazione/modello → codice/solver, con validazione e riparazione.</p>
  </div>
  <div class="card">
    <h3>2) LLM-assisted optimization</h3>
    <p>LLM genera euristiche/strategie; il solver valuta e guida il loop.</p>
  </div>
  <div class="card">
    <h3>3) Direct solving</h3>
    <p>LLM produce direttamente decisioni/soluzioni (testo) e/o input multimodali.</p>
  </div>
</div>

<div class="so-what"><b>Uso nel talk:</b> i due case study attaccano “pezzi” diversi di questa mappa.</div>

<!--
NOTE:
Key message:
- Gli autori propongono una tassonomia in 3 pathways per organizzare la letteratura.

Evidence / Citations:
- [Wang&Li 2025 (arXiv:2509.18180v3), Fig.1, PDF p.2] — overview/tassonomia (3 pathways).
-->

---
layout: two-cols
---

<div class="kicker">Survey (Wang &amp; Li) — Pathway 1</div>

## Pathway 1 — Automatic modeling (closed-loop)

- Obiettivo: trasformare una descrizione in un modello OR eseguibile
- **Closed-loop**: generazione → validazione (solver/esecuzione) → riparazione
- Output tipico: formulazione + implementazione + controlli di correttezza

<div class="so-what"><b>Perché conta:</b> riduce errori “silenziosi” (vincoli dimenticati, implementazione incoerente).</div>

::right::

![Closed-loop framework (placeholder)](/fig/wangli_fig_closed_loop.png)

<div class="small-source">Source: [Wang&Li 2025 (arXiv:2509.18180v3), Fig.2, PDF p.3]</div>

<!--
NOTE:
Key message:
- Nel pathway di automatic modeling, il survey enfatizza un ciclo chiuso generate–validate–repair per ridurre errori.

Evidence / Citations:
- [Wang&Li 2025 (arXiv:2509.18180v3), Fig.2, PDF p.3] — framework closed-loop per automatic modeling.
-->

---

<div class="kicker">Survey (Wang &amp; Li) — Pathway 1 (metodi)</div>

## Automatic modeling: famiglie di metodi (trade-off)

<div class="card-grid">
  <div class="card">
    <h3>Prompting</h3>
    <p>Rapido da applicare; sensibilità a vincoli complessi e formati.</p>
  </div>
  <div class="card">
    <h3>Fine-tuning / adattamento</h3>
    <p>Più aderenza in domini specifici; costo dati + computazione.</p>
  </div>
  <div class="card">
    <h3>Knowledge-guided</h3>
    <p>Più controllabile; dipende da copertura e qualità della conoscenza.</p>
  </div>
</div>

<div class="so-what"><b>Trade-off ricorrente:</b> rapidità vs robustezza/controllabilità (e costo di setup).</div>

<!--
NOTE:
Key message:
- Il survey raggruppa approcci per automatic modeling e discute pro/contro.

Evidence / Citations:
- [Wang&Li 2025 (arXiv:2509.18180v3), Table 1, PDF p.3] — overview metodi (automatic modeling).
- [Wang&Li 2025 (arXiv:2509.18180v3), Table 2, PDF p.4] — overview metodi (automatic modeling).
-->

---
layout: two-cols
---

<div class="kicker">Survey (Wang &amp; Li) — Pathway 2</div>

## Pathway 2 — LLM-assisted optimization (ibridi)

- LLM propone **euristiche/operatori/strategie** (azioni su soluzioni o parametri)
- Valutazione tramite **solver/scorer** → feedback per iterare
- Focus: migliorare qualità/efficienza senza sostituire completamente il solver

<div class="so-what"><b>Pragmatismo:</b> si “compra” affidabilità lasciando al solver il controllo della feasibility.</div>

::right::

![LLM-assisted optimization (placeholder)](/fig/wangli_fig_assisted_optimization.png)

<div class="small-source">Source: [Wang&Li 2025 (arXiv:2509.18180v3), Fig.3, PDF p.6]</div>

<!--
NOTE:
Key message:
- Nel pathway 2 l’LLM è un co-pilota: genera candidate mosse/strategie, mentre la valutazione resta ancorata al solver.

Evidence / Citations:
- [Wang&Li 2025 (arXiv:2509.18180v3), Fig.3, PDF p.6] — principali approcci in LLM-assisted optimization.
- [Wang&Li 2025 (arXiv:2509.18180v3), Table 3, PDF p.6] / [Table 4, PDF p.8] / [Table 5, PDF p.9] — tassonomie/categorie (seleziona le voci che citi).
-->

---

<div class="kicker">Survey (Wang &amp; Li) — Pathway 3</div>

## Direct solving: single-modal + technique-enhanced

<div class="card-grid two">
  <div class="card">
    <h3>Single-modal (testo)</h3>
    <p>L’LLM genera direttamente decisioni/soluzioni da descrizioni testuali.</p>
  </div>
  <div class="card">
    <h3>Technique-enhanced</h3>
    <p>Meta-prompt/iterazione, self-debugging, multi-sampling, multi-round optimization…</p>
  </div>
</div>

<div class="so-what"><b>Limite comune:</b> vincoli complessi e verificabilità → spesso serve un controllo esterno.</div>

<!--
NOTE:
Key message:
- Nel pathway 3 l’LLM tenta di risolvere direttamente; il survey discute setting e limiti.

Evidence / Citations:
- [Wang&Li 2025 (arXiv:2509.18180v3), Table 6, PDF p.10] — panoramica su direct solving (single-modal).
- [Wang&Li 2025 (arXiv:2509.18180v3), PDF p.10] — esempi di technique-enhanced (multi-*, meta-prompt, ecc.) nella tabella.
-->

---

<div class="kicker">Survey (Wang &amp; Li) — valutazione &amp; sfide</div>

## Valutazione + sfide aperte (dal survey)

<div class="card-grid two">
  <div class="card">
    <h3>Evaluation</h3>
    <p>Benchmark frammentati + metriche non uniformi → confronti difficili.</p>
  </div>
  <div class="card">
    <h3>Deployment</h3>
    <p>Integrazione con solver, logging e auditability: “ricerca → pratica”.</p>
  </div>
</div>

<div class="so-what"><b>Ponte verso i case study:</b> entrambi cercano di rendere il ciclo più controllabile (o più “end-to-end”).</div>

<!--
NOTE:
Key message:
- Il survey evidenzia che valutazione e deployment restano colli di bottiglia.

Evidence / Citations:
- [Wang&Li 2025 (arXiv:2509.18180v3), Sec.5, PDF p.13] — sfide e direzioni future.
-->

---
layout: two-cols
---

<div class="kicker">Case study — Zhang et al. (OR-LLM-Agent)</div>

## Case study 1 — OR-LLM-Agent (Zhang et al.)

- Pipeline agentica per **NL → modello → codice → debug**
- Agenti specializzati (es. modeling/math, code, debugging)
- Obiettivo: automatizzare e rendere più controllabile modeling + solving

<div class="so-what"><b>Fit (survey):</b> Pathway 1 (automatic modeling) con enfasi su closed-loop e riparazione.</div>

::right::

![OR-LLM-Agent architecture (placeholder)](/fig/zhang_fig_architecture.png)

<div class="small-source">Source: [Zhang et al. 2025 (arXiv:2503.10009v3), Fig.2, PDF p.2]</div>

<!--
NOTE:
Key message:
- Zhang et al. propongono un agente che integra generazione, esecuzione e correzione per problemi OR.

Evidence / Citations:
- [Zhang et al. 2025 (arXiv:2503.10009v3), Abstract, PDF p.1] — idea generale del framework.
- [Zhang et al. 2025 (arXiv:2503.10009v3), Fig.2, PDF p.2] — architettura/workflow (figure mostrata in slide).
-->

---
layout: two-cols
---

<div class="kicker">Case study — Zhang et al. (debug + experiments)</div>

## OR-LLM-Agent: debugging loop + benchmark

- Debugging agent: esecuzione + controllo errori/feasibility
- **Alg.1**: strategia di riparazione iterativa (code self-repair → model/math repair)
- Introducono **BWOR** (benchmark) e riportano confronti (reasoning vs non-reasoning) su più dataset

<div class="so-what"><b>Takeaway:</b> l’esecuzione diventa “oracle” per guidare repair e rendere l’automazione meno fragile.</div>

::right::

![Debug loop (placeholder)](/fig/zhang_alg1_debug_loop.png)

<div class="small-source">Source: [Zhang et al. 2025 (arXiv:2503.10009v3), Alg.1, PDF p.3]</div>

<!--
NOTE:
Key message:
- Il contributo chiave è l’ancoraggio all’esecuzione (run + debug) per ridurre errori di modellazione/codice.

Evidence / Citations:
- [Zhang et al. 2025 (arXiv:2503.10009v3), Alg.1, PDF p.3] — schema del loop di debugging/riparazione.
- [Zhang et al. 2025 (arXiv:2503.10009v3), PDF p.1] — link al benchmark BWOR (HuggingFace dataset) presente nel paper.
- [Zhang et al. 2025 (arXiv:2503.10009v3), PDF p.5] — esperimenti: confronti su benchmark e tra modelli reasoning/non-reasoning.

TODO (audit):
- Se aggiungi numeri/modelli: aggancia a tabella/figura specifica nel PDF.
-->

---
layout: two-cols
---

<div class="kicker">Case study — Jiang et al. (Bridging LLMs &amp; Optimization)</div>

## Case study 2 — Bridging LLMs & Optimization (Jiang et al.)

- Obiettivo: framework end-to-end per **COP descritti in testo** (“text-attributed”)
- **LNCS**: *Language-based Neural COP Solver* (encoding semantico + generator)
- Training: **conflict-free multi-task reinforcement learning** (come riportato dagli autori)

<div class="so-what"><b>Fit (survey):</b> spinge verso un approccio più “end-to-end” (bridge testo→ottimizzazione).</div>

::right::

![Framework (placeholder)](/fig/jiang_fig1_framework.png)

<div class="small-source">Source: [Jiang et al. 2024 (arXiv:2408.12214v2), Fig.1, PDF p.3]</div>

<!--
NOTE:
Key message:
- Jiang et al. propongono un bridge tra rappresentazioni testuali e componenti di ottimizzazione in un framework unificato.

Evidence / Citations:
- [Jiang et al. 2024 (arXiv:2408.12214v2), Abstract, PDF p.1] — definizione LNCS + semantic space + generator + conflict-free multi-task RL.
- [Jiang et al. 2024 (arXiv:2408.12214v2), Fig.1, PDF p.3] — overview architettura/framework.
-->

---
layout: two-cols
---

<div class="kicker">Case study — Jiang et al. (results)</div>

## Jiang: esperimenti + collegamento al survey

- Gli autori riportano risultati su COP diversi e discutono generalizzabilità
- Esempio (tabella): metriche tipo **Gap** su TSP / CVRP / KP
- Messaggio: end-to-end è promettente, ma evaluation/feasibility restano centrali

<div class="so-what"><b>Collegamento al survey:</b> riprende la sfida “valutazione robusta” e l’ancoraggio a vincoli/feasibility.</div>

::right::

![Results (placeholder)](/fig/jiang_tab_or_fig_results.png)

<div class="small-source">Source: [Jiang et al. 2024 (arXiv:2408.12214v2), Table 4, PDF p.7]</div>

<!--
NOTE:
Key message:
- Concludi con cosa aggiunge questo paper rispetto alla tassonomia del survey.

Evidence / Citations:
- [Jiang et al. 2024 (arXiv:2408.12214v2), Abstract, PDF p.1] — gli autori riportano SOTA + generalizability (claim attribuito).
- [Jiang et al. 2024 (arXiv:2408.12214v2), Table 4, PDF p.7] — tabella con colonne/metriche (es. Gap) su TSP/CVRP/KP.

Interpretazione (esplicita):
- Interpretazione: il framework può essere visto come un tentativo di "end-to-end" che tocca modeling e solving.
  Supporto indiretto: [Jiang et al. 2024 (arXiv:2408.12214v2), Abstract, PDF p.1] + [Wang&Li 2025 (arXiv:2509.18180v3), Fig.1, PDF p.2].
-->

---

<div class="kicker">Chiusura</div>

## Sintesi + direzioni future (ancorate al survey)

<div class="card-grid two">
  <div class="card">
    <h3>3 takeaway</h3>
    <p>1) Closed-loop + verifica è spesso il “fattore abilitante”.</p>
    <p>2) Ibridi LLM+solver massimizzano affidabilità mantenendo feasibility sotto controllo.</p>
    <p>3) Direct solving richiede evaluation rigorosa (metriche + setting comparabili).</p>
  </div>
  <div class="card">
    <h3>3 sfide aperte</h3>
    <p>1) Benchmark e metriche: confronti riproducibili e completi.</p>
    <p>2) Robustezza: vincoli complessi, edge case, stabilità.</p>
    <p>3) Deployment: integrazione, logging, auditability.</p>
  </div>
</div>

<div class="so-what"><b>Dove si collocano i case study:</b> OR-LLM-Agent (repair/exec loop) ↔ LNCS (end-to-end bridge testo→COP).</div>

<!--
NOTE:
Key message:
- Riassumi il survey e “chiudi il cerchio” collegando i due case study alle sfide.

Evidence / Citations:
- Takeaway closed-loop: [Wang&Li 2025 (arXiv:2509.18180v3), Fig.2, PDF p.3] + [Zhang et al. 2025 (arXiv:2503.10009v3), Alg.1, PDF p.3].
- Assisted optimization: [Wang&Li 2025 (arXiv:2509.18180v3), Fig.3, PDF p.6].
- Evaluation/deployment challenges: [Wang&Li 2025 (arXiv:2509.18180v3), Sec.5, PDF p.13].
- Case study LNCS end-to-end: [Jiang et al. 2024 (arXiv:2408.12214v2), Abstract, PDF p.1] + [Jiang et al. 2024 (arXiv:2408.12214v2), Fig.1, PDF p.3].
-->

---

<div class="kicker">Bibliografia</div>

## References

- Wang, Yang; Li, Kai. *Large Language Models in Operations Research: Methods, Applications, and Challenges*. arXiv:2509.18180v3 (2025).
- Zhang, Bowen; Luo, Pengcheng; Yang, Genke; Soong, Boon-Hee; Yuen, Chau. *OR-LLM-Agent: Automating Modeling and Solving of Operations Research Optimization Problems with Reasoning LLM*. arXiv:2503.10009v3 (2025).
- Jiang, Xia; Wu, Yaoxin; Wang, Yuan; Zhang, Yingqian. *Bridging Large Language Models and Optimization: A Unified Framework for Text-attributed Combinatorial Optimization*. arXiv:2408.12214v2 (2024).

<!--
NOTE:
Nessun claim tecnico: solo bibliografia.
-->
