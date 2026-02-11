---
layout: section
hideFooter: true
---

# Case study 1
## OR-LLM-Agent (Zhang et al., 2025)

---
layout: default
kicker: "Case study — Zhang et al. (OR-LLM-Agent)"
---

## Case study 1 — OR-LLM-Agent (Zhang et al.)

<v-clicks style="margin: 5px 0;">

- **Task decomposition**: 3 sub-agenti (Math → Code → Debug)
- **Reasoning LLM**: niente <i>fine-tuning</i> / <i>retraining</i> dichiarato
- **Closed-loop**: esecuzione/<i>solver</i> come <i>feedback</i> per <i>repair</i> e robustezza

</v-clicks>

<Callout v-click><b><i>Pathway</i> 1</b>: Si colloca nel (<i>automatic modeling</i>) con enfasi su <i>closed-loop</i> e riparazione</Callout>

<Figure
  src="/fig/zhang_fig_architecture.png"
  alt="OR-LLM-Agent workflow: modeling → code → debugging"
  caption="Workflow OR-LLM-Agent: Math Agent → Code Agent → Debugging Agent"
  maxHeight="200px"
  source="[Zhang et al. 2025 (arXiv:2503.10009v3), Fig.2, PDF p.2]"
  style="margin-top: 1rem;"
/>

<!--
- **Aggancio al survey**
- **Idea base** — **testo → modello → codice**, poi esecuzione/<i>solver</i> come “reality check”.
- **Perché 3 agenti** — separano i compiti (modellazione, codice, debug) e rendono il loop più controllabile.
- **Da non sbagliare** — 3 stadi in sequenza (modeling → code → debugging) e sub-agent dichiarati <i>off-the-shelf</i> (senza fine-tuning/retraining).
- **Fonte (paper)** — [Zhang et al. 2025 (arXiv:2503.10009v3), Abstract, PDF p.1] + [Zhang et al. 2025 (arXiv:2503.10009v3), Fig.2, PDF p.2]
-->

---
layout: default
kicker: "Case study — Zhang et al. (sub-agents)"
---

## OR-LLM-Agent: cosa fanno i sub-agent

<CardGrid style="margin:22px -5px;">
  <Card v-click>
    <div class="kicker">1) Modeling</div>
    <h3><b>Math Agent</b></h3>
    <p><b>Input</b>: descrizione in linguaggio naturale</p>
    <p><b>Output</b>: <b>variabili</b>, <b>vincoli</b>, <b>obiettivo</b> → modello/formulazione</p>
    <p><b>Perché aiuta</b>: mette ordine, riduce omissioni e ambiguità</p>
  </Card>
  <Card v-click>
    <div class="kicker">2) Coding</div>
    <h3><b>Code Agent</b></h3>
    <p><b>Input</b>: modello matematico</p>
    <p><b>Output</b>: <b>codice eseguibile</b> per il <i>solver</i> (setup, variabili, vincoli, obiettivo)</p>
    <p><b>Perché aiuta</b>: separa “capire” da “implementare”, e rende più facile validare</p>
  </Card>
  <Card v-click>
    <div class="kicker">3) Execution</div>
    <h3><b>Debugging Agent</b></h3>
    <p><b>Input</b>: codice eseguibile</p>
    <p><b>Strategia</b>: prima <b>code repair</b>, poi (se serve) <b>model repair</b></p>
    <p><b>Perché aiuta</b>: l’esecuzione diventa un “test di realtà”, non solo testo plausibile</p>
  </Card>
</CardGrid>

<Callout v-click><b>Idea chiave:</b> spezzare il workflow in ruoli chiari + mettere l’<i>execution</i> nel loop rende la pipeline più controllabile e meno fragile.</Callout>

<!--
- **Come raccontarla** — “hanno preso il workflow umano e l’hanno spezzato in tre ruoli chiari.”
- **Math Agent** — mette ordine: **variabili / vincoli / obiettivo** → formulazione più coerente.
- **Code Agent** — traduce la formulazione in **codice per solver** (parte più “meccanica”).
- **Debugging Agent** — **esegue** e ripara: prima sistema il codice, poi (se serve) rimette mano al modello.
- **Takeaway** — l’esecuzione ti evita errori “plausibili ma sbagliati”.
- **Fonte (paper)** — [Zhang et al. 2025 (arXiv:2503.10009v3), Abstract, PDF p.1] + [Zhang et al. 2025 (arXiv:2503.10009v3), Alg.1, PDF p.3]
-->

---
layout: center
hideFooter: true
kicker: "Case study — Zhang et al. (workflow)"
---

<Figure
	src="/fig/zhang_fig_architecture_2.png"
  alt="Workflow OR-LLM-Agent: Math Agent → Code Agent → Debugging Agent"
  caption="Workflow OR-LLM-Agent: Math Agent → Code Agent → Debugging Agent"
  maxHeight="450px"
  source="[Zhang et al. 2025 (arXiv:2503.10009v3), Fig.2, PDF p.2]"
/>

<!--
NOTE:
- **Slide solo figura:** qui non leggo tutto, la uso come “mappa”.
- **Come guidare l’occhio:** “seguite la riga: testo → modello → codice → esecuzione/repair.”
- **Messaggio:** il punto è il loop: trasformi testo in struttura, generi codice, lo esegui e ripari finché “sta in piedi”.
- **Fonte (paper)** — [Zhang et al. 2025 (arXiv:2503.10009v3), Fig.2, PDF p.2]
-->
