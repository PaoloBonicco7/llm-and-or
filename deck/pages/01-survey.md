---
layout: section
hideFooter: true
---

# Survey
## Wang &amp; Li (2025)

---
kicker: "Survey (Wang & Li) — motivazione"
---

## Perché OR + LLM adesso

<CardGrid class="deck-grid">
  <Card v-click>
    <div class="kicker">Problema</div>
    <h3><b>OR “expert-driven”</b></h3>
    <p><b>Bottleneck</b>: modellazione + tuning manuale, forte dipendenza da esperti</p>
    <p><b>Dove fatica</b>: problemi grandi e dinamici, vincoli complessi, requisiti di <i>real-time</i></p>
  </Card>
  <Card v-click>
    <div class="kicker">Opportunità</div>
    <h3><b>LLM come “traduttore”</b></h3>
    <p><b><i>Modeling</i></b>: testo → variabili/vincoli → modello o codice per <i>solver</i></p>
    <p><b><i>Solving</i></b>: propone euristiche/strategie e migliora con <i>feedback</i> (loop)</p>
  </Card>
  <Card v-click>
    <div class="kicker">Survey</div>
    <h3><b>Mettere ordine</b></h3>
    <p>Tassonomia in 3 filoni:</p>
    <p>
      - <b>Automatic modeling</b>
      <br />
      - <b>LLM-assisted optimization</b>
      <br />
      - <b>Direct solving</b>
    </p>
  </Card>
</CardGrid>

<Callout v-click><b>Idea chiave:</b> Il modello di linguaggio <b>propone/struttura</b>, il <i>solver</i> verifica (<b><i>feasibility</i> / qualità</b>) → iterazioni <b><i>generate – validate – repair</i></b> per limitare errori e allucinazioni </Callout>

<!--
NOTE:
- **OR in una frase** — “decisioni con vincoli”: trasporti, supply chain, scheduling.
- **Perché oggi fa fatica** — pipeline spesso *expert-driven* (modellazione + tuning manuale) → poca scalabilità quando i problemi crescono/diventano dinamici e serve real-time.
- **Cosa portano gli LLM** — mappano linguaggio naturale → struttura (variabili/vincoli/obiettivi) fino a modello e/o codice eseguibile.
- **Non solo modeling** — possono anche generare euristiche/strategie e iterare con <i>feedback</i> (sempre con validazione)
- **Perché il survey è utile** — letteratura frammentata: qui gli autori propongono una tassonomia in 3 filoni e discutono benchmark/applicazioni/sfide.
- **Takeaway** — “LLM propone, <i>solver</i> verifica”: non ci fidiamo dell’output a occhi chiusi, lo chiudiamo in un loop <i>generate–validate–repair</i>
- **Fonte** — Wang & Li (2025), arXiv:2509.18180v3, Abstract + Sec.1.
-->

---
kicker: "Survey (Wang & Li) — fondamenti"
---

## Prima della tassonomia: perché OR e LLM "si incastrano"

<CardGrid cols="2" class="deck-grid">
  <Card v-click>
    <div class="kicker">OR</div>
    <h3><b>Rigore + verifica</b></h3>
    <p><b>Formalizza</b>: obiettivo e vincoli diventano regole precise</p>
    <p><b>Controlla</b>: il <i>solver</i> verifica feasibility e misura la qualità</p>
  </Card>
  <Card v-click>
    <div class="kicker">LLM</div>
    <h3><b>Interfaccia + proposta</b></h3>
    <p><b>Abbassa la barriera</b>: parti da requisiti in linguaggio naturale</p>
    <p><b>Accelera l’iterazione</b>: propone bozze (modello / codice) e si rifinisce con <i>feedback</i></p>
  </Card>
</CardGrid>

<Callout v-click><b>Messaggio:</b> l’LLM rende più facile passare dal <b>problema descritto a parole al modello</b>; il <i>solver</i> fa da verifica automatica</Callout>

<!--
- **Perché “si incastrano”** — OR dà rigore e un modo oggettivo di controllare; l’LLM dà flessibilità sul linguaggio.
- **OR = verifica** — se un vincolo manca o un’ipotesi è sbagliata, il <i>solver</i> te lo segnala (feasibility + qualità)
- **LLM = acceleratore** — ti fa partire da una descrizione, propone una bozza, e poi la aggiusti con errori/<i>feedback</i>
- **Ottimo vs tempo** — metodi esatti con garanzie vs euristiche / meta-euristiche più scalabili.
- **Fonte** — Wang & Li (2025), arXiv:2509.18180v3, Sec.2.A–B. (Trade-off esatti/euristiche = background di OR.)
-->

---
layout: center
hideFooter: true
---

<Figure
  src="/fig/wangli_fig1_literature_classification_map.png"
  alt="Literature classification map of LLM-driven OR research pathways and representative works (Wang & Li, 2025)"
  caption="Mappa della letteratura: come gli autori raggruppano i lavori su OR+LLM e quali esempi ricadono in ciascun filone"
  maxHeight="470px"
  source="[Wang & Li 2025 (arXiv:2509.18180v3), Fig.1]"
/>

<!--
Le **3 tipologie di approccio** ricorrenti nella letteratura su **OR+LLM**, con esempi rappresentativi
-->

---
kicker: "Survey (Wang & Li) — tassonomia"
---

## Survey: 3 pathways

<CardGrid class="deck-grid">
  <Card v-click>
    <div class="kicker"><i>Pathway 1</i></div>
    <h3><b>Automatic modeling</b></h3>
    <p><b>Obiettivo</b>: <br> testo → modello/formulazione</p>
    <p><b>Output</b>: <br> codice per <i>solver</i> + validazione/<i>repair</i> in loop</p>
  </Card>
  <Card v-click>
    <div class="kicker"><i>Pathway 2</i></div>
    <h3><b>LLM-assisted optimization</b></h3>
    <p><b>Ruolo</b>: l’LLM propone mosse / euristiche / parametri</p>
    <p><b>Controllo</b>: il <i>solver</i> / <i>scorer</i> valuta e guida l’iterazione</p>
  </Card>
  <Card v-click>
    <div class="kicker"><i>Pathway 3</i></div>
    <h3><b>Direct solving</b></h3>
    <p><b>Idea</b>: l’LLM genera direttamente una soluzione</p>
    <p><b>Nota</b>: spesso serve una validazione esterna (vincoli/feasibility)</p>
  </Card>
</CardGrid>

<Callout v-click><b>Esempi:</b> i due case study riportano due esempi per due pathway</Callout>

<!--
- **La mappa** — 3 modi ricorrenti di usare LLM in OR: 
  1. **costruire modelli**
  2. **assistere il solving**
  3. **generare direttamente soluzioni.**
- **Come leggerla** — da sinistra a destra aumenta “quanto” deleghi all’LLM; di solito aumenta anche il bisogno di <i>checker</i>/validazione.
- **Ponte ai case study** — ogni paper lo posiziono qui: *quale parte automatizza* e *quale parte resta al solver*.
- **Fonte** — Wang & Li (2025), arXiv:2509.18180v3, Fig.1.
-->

---
layout: two-cols
kicker: "Survey (Wang & Li) — Pathway 1"
layoutClass: pathway1-split
---

## Pathway 1 — Automatic modeling

<v-clicks style="margin: 0 20px 0 -20px">

- **Obiettivo**: trasformare una descrizione in un modello OR eseguibile (formulazione + codice)

- **Pipeline** (Fig.2): **comprensione** → **identificazione elementi** → **struttura del modello** → **codice <i>solver</i>** → **verifica + <i>feedback</i>**

- **<i>Closed-loop</i>**: esecuzione → errori / incoerenze → riparazione iterativa (<i>retry</i> / <i>repair</i>)

</v-clicks>

<Callout v-click style="margin: 0 20px 0 -20px"><b>Perché conta:</b> riduce errori “silenziosi” (vincoli dimenticati, implementazione incoerente)</Callout>

::right::

<Figure
  src="/fig/wangli_fig_closed_loop.png"
  alt="Closed-loop framework of automatic modeling from natural language input to model execution"
  caption="Il ciclo di automatic modeling individuato dagli autori"
  source="[Wang & Li 2025 (arXiv:2509.18180v3), Fig.2, PDF p.3]"
/>

<!--
- **Di cosa parliamo** — “automatic modeling” = automatizzare la parte più noiosa: scrivere un modello coerente partendo dal testo.
- **Le fasi chiave** — comprendere il problema → estrarre variabili/vincoli → assemblare la formulazione → generare codice → farlo girare e controllare.
- **Loop = sicurezza** — il *solver* fa da *checker*: se non è feasible o c’è un bug, si torna indietro e si ripara.
- **Perché è importante** — molti errori sono “silenziosi” (vincolo dimenticato = soluzione apparentemente ottima ma sbagliata).
- **Fonte** — Wang & Li (2025), arXiv:2509.18180v3, Fig.2 + Sec.3.A.
-->

---
kicker: "Survey (Wang & Li) — Pathway 1 (metodi)"
---

## Automatic modeling: famiglie di metodi

<CardGrid class="deck-grid">
  <Card v-click>
    <div class="kicker">Setup basso</div>
    <h3><i><b>Prompting</b></i></h3>
    <p><b>Pro</b>: parti subito, ottimo per prototipi</p>
    <p><b>Contro</b>: fragile su vincoli complessi e formati “sporchi”</p>
  </Card>
  <Card v-click>
    <div class="kicker">Stabilità ↑</div>
    <h3><i><b>Fine-tuning</b></i> / adattamento</h3>
    <p><b>Pro</b>: più aderenza su dominio e stile di input</p>
    <p><b>Contro</b>: costo dati + compute + manutenzione</p>
  </Card>
  <Card v-click>
    <div class="kicker">Controllo ↑</div>
    <h3><i><b>Knowledge-guided</b></i></h3>
    <p><b>Pro</b>: più controllabile con KB/regole/<i>retrieval</i></p>
    <p><b>Contro</b>: dipende da copertura e qualità della conoscenza</p>
  </Card>
</CardGrid>

<Callout v-click><b>Trade-off ricorrente:</b> rapidità vs robustezza/controllabilità (e costo di setup)</Callout>

<!--
- **Messaggio della slide** — Trade-off stabilità/costo
- **Prompting** — “parto subito”: prototipo veloce, ma su vincoli brutti serve struttura e validazione
- **Fine-tuning** — paghi in dati/compute, ma riduci variabilità e migliori aderenza su un dominio
- **Knowledge-guided** — aggiungi KB: aumenta controllo, ma se la conoscenza è incompleta porta + danni che benefici
- **Regola pratica** — output strutturati + validazione automatica (<i>solver-in-the-loop</i>), altrimenti è facile “perdersi” un vincolo
- **Fonte** — Wang & Li (2025), arXiv:2509.18180v3, Table 1–2 (panoramica metodi).
-->

---
layout: two-cols-header
kicker: "Survey (Wang & Li) — Pathway 2"
layoutClass: pathway2-split
---

## Pathway 2 — Hybrid Optimization

::left::

<v-clicks style="margin-top: 30px">

- <b>Ruolo dell’LLM</b> — progetta il metodo, non la soluzione
- <b>Generatore di euristiche</b><br>
  - crea operatori di ricerca
  - progetta euristiche costruttive da zero per nuovi problemi
- <b>Guida intelligente</b><br>
  - suggerisce mosse promettenti durante la ricerca
  - seleziona dinamicamente la strategia migliore
- <b>Vantaggio</b> — creatività dell’LLM + efficienza e validità garantita dai solver classici

</v-clicks>

<Callout v-click><b>Idea chiave:</b> l’LLM progetta l’algoritmo, il solver classico lo esegue e trova l’ottimo</Callout>

::right::

<div class="pathway2-figs">
  <Figure
    src="/fig/wangli_fig_assisted_optimization-a.png"
    alt="LLM-driven Heuristic Evolution & Strategy Optimization"
    caption="<i>LLM-driven Heuristic Evolution &amp; Strategy Optimization</i>"
    maxHeight="500px"
  />

  <div class="small-source">
    Source: [Wang &amp; Li 2025 (arXiv:2509.18180v3), Fig.3, PDF p.6]
  </div>
</div>

<!--
- **Come leggerla** — l’LLM resta “dentro” un algoritmo classico: propone euristiche/strategie, il solver le esegue
- **Messaggio** — creatività (LLM) + rigore/validazione (solver classico)
- **Fonte** — Wang & Li (2025), arXiv:2509.18180v3, Fig.3 + Table 3–5
-->

---
kicker: "Survey (Wang & Li) — Pathway 3"
layout: two-cols-header
layoutClass: pathway3-split
---

## Pathway 3 — Direct Generative Optimization

::left::

<v-clicks style="margin-top: 30px">

- <b>Ruolo dell’LLM</b> — <i>solver black-box</i>: descrizione $\to$ soluzione (senza modellazione/codice)
- <b>Approccio <i>zero-code</i></b> — input in linguaggio naturale, output come soluzione finale
- <b>Tecniche di potenziamento</b><br>
  - <b>Reasoning</b>: passo-passo per ridurre errori logici
  - <b>Iterazione &amp; feedback</b>: <i>self-refinement</i>/<i>self-debugging</i> (spesso con un <i>checker</i> esterno)
- <b>Limiti</b> — efficace per prototipi/istanze piccole; su vincoli o istanze grandi serve validazione rigorosa

</v-clicks>

<Callout v-click><b>Idea chiave:</b> prova --> verifica --> correzione (loop) finché la soluzione è <i>feasible</i></Callout>

::right::

<div class="pathway2-figs">
  <Figure
    src="/fig/wangli_fig_assisted_optimization-b.png"
    alt="LLM-dominated Optimization Solving"
    caption="<i>LLM-dominated Optimization Solving</i>"
    maxHeight="500px"
  />

  <div class="small-source">
    Source: [Wang &amp; Li 2025 (arXiv:2509.18180v3), Fig.3, PDF p.6]
  </div>
</div>

<!--
- **Cos’è “direct solving”** — invece di costruire un modello, chiedi all’LLM di produrre direttamente una soluzione (o una decisione).
- **Potenziamento** — per farlo reggere: iterazioni, <i>self-debugging</i>, <i>multi-sampling</i>/<i>self-ensemble</i> e validazione esterna.
- **Occhio ai vincoli** — senza un controllo (<i>solver</i>/<i>checker</i>/<i>scorer</i>) è facile ottenere output plausibili ma non feasible.
- **Fonte** — Wang & Li (2025), arXiv:2509.18180v3, Table 6 + Sec.3.B.2 (direct solving).
-->

---
kicker: "Survey (Wang & Li) — benchmark"
---

## Benchmark

<CardGrid cols="2" class="deck-grid deck-grid--benchmark">

 <Card v-click>
 <div class="kicker">Graph reasoning</div>
 <h3><b>Struttura & Topologia</b> (<b>NLGraph</b> · <b>GraphArena</b>)</h3>
 <p>L'LLM "vede" il grafo? Test su cicli, connettività e rilevamento di <b>allucinazioni</b> (archi inesistenti).</p>
 </Card>

 <Card v-click>
 <div class="kicker">Spatial planning</div>
 <h3><b>Navigazione</b> (<b>PPNL</b>)</h3>
 <p>Ragionamento spaziale multi-step: pianificare sequenze coerenti in ambienti grid-world.</p>
 </Card>

 <Card v-click>
 <div class="kicker">Combinatorial optimization</div>
 <h3><b>Performance</b> (<b>CO-Bench</b> · <b>FrontierCO</b>)</h3>
 <p>End-to-end: dal testo alla soluzione. Si misura il <b>gap di ottimalità</b> su problemi NP-hard (TSP, Scheduling).</p>
 </Card>

 <Card v-click>
 <div class="kicker">Explainability</div>
 <h3><b>Trasparenza</b> (<b>EOR</b>)</h3>
 <p>Giustificare le scelte all'utente: <i>“Perché hai cambiato questo turno?”</i> vs Black-box.</p>
 </Card>

</CardGrid>

<div class="benchmark-callout" style="margin-top: 20px">
  <Callout v-click><b>Messaggio chiave:</b> La valutazione moderna richiede tre metriche: <b>correttezza strutturale</b> (codice valido), <b>qualità della soluzione</b> (funzione obiettivo) e <b>interpretabilità</b> del ragionamento.</Callout>
</div>

<!--
- **Concetto chiave** — “non basta che giri”: serve misurare *qualità* (costo/ottimo) e *ragionamento strutturato* (grafi, percorsi).
- **Grafi** — NLGraph (29k problemi, testo→grafi: cicli/cammini minimi/connettività); GraphArena valuta anche processo e allucinazioni (archi inesistenti).
- **Spaziale** — PPNL: pianificazione su griglia, coerenza delle azioni lungo il percorso.
- **CO classica** — CO-Bench: end-to-end (lettura dati → algoritmo → soluzione) su problemi reali; FrontierCO: problemi “hard”, spesso buono vs NN ma fatica a scegliere l’algoritmo giusto.
- **Interpretabilità** — EOR: spiegare *perché* una decisione è cambiata (contesto industriale).
- **Takeaway** — benchmark rigorosi = modo concreto per capire dove l’LLM eccelle (problemi piccoli / generazione di codice) e dove crolla (grafi complessi / ottimalità garantita) → serve validazione (<i>checker</i>/<i>solver</i>).
- **Fonte** — Wang & Li (2025), arXiv:2509.18180v3, sezione benchmark (PDF p.11).
-->

---
kicker: "Survey (Wang & Li) — valutazione & sfide"
---

## Valutazione + sfide aperte (dal survey)

<CardGrid class="deck-grid">
  <Card v-click>
    <div class="kicker">Safety</div>
    <h3>Affidabilità</h3>
    <p><b>Instabilità</b>: Testo → struttura non sempre consistente</p>
    <p><b>Opacità</b>: interpretabilità limitata del “perché”</p>
  </Card>
  <Card v-click>
    <div class="kicker">Misura</div>
    <h3><i>Evaluation</i></h3>
    <p><b>Benchmark</b>: frammentati, coverage parziale</p>
    <p><b>Metriche</b>: non uniformi → confronti difficili</p>
  </Card>
  <Card v-click>
    <div class="kicker">Pratica</div>
    <h3><i>Deployment</i></h3>
    <p><b>Integrazione</b>: <i>solver</i>, pipeline, toolchain</p>
    <p><b>Operatività</b>: logging, auditability, costi</p>
  </Card>
</CardGrid>

<Callout v-click><b>Ponte verso i case study:</b> due strade per ridurre rischio e instabilità: <i>closed-loop</i> con validazione vs approcci più <i>end-to-end</i> con <i>evaluation</i> forte</Callout>

<!--
- **Affidabilità** — anche quando “sembra giusto”, Testo→struttura può essere instabile e la spiegazione non è sempre affidabile
- **Evaluation** — senza benchmark + metriche comparabili rischi di non capire se hai davvero migliorato qualcosa
- **Deployment** — il mondo reale chiede integrazione (tool/solver), logging, audit, e costi sostenibili
- **Ponte ai case** — OR-LLM-Agent = <i>closed-loop</i> e <i>repair</i>, Jiang = più <i>end-to-end</i> ma con training + metriche (claim attribuito)
- **Fonte** — Wang & Li (2025), arXiv:2509.18180v3, Sec.5 (sfide e direzioni future).
-->
