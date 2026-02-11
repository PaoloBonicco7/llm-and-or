---
layout: section
hideFooter: true
---

# Case study 2
## Bridging Large Language Models and Optimization
#
### Language-based Neural COP Solver (LNCS) (Jiang et al., 2024)

<!--
NOTE:
- **Dal survey ai case study:** adesso passiamo dalla “mappa mentale” a un esempio concreto.
- **Qui il focus:** non “promptare meglio”, ma costruire un <i>solver</i> <i>end-to-end</i> che parte da testo e arriva a una soluzione.
-->

---
kicker: "Case study — Jiang et al. (Bridging LLMs & Optimization)"
---

## Jiang et al. (2024): bridge testo → ottimizzazione

<CardGrid cols="2" class="deck-grid jiang-framework-grid">
  <Card v-click>
    <div class="kicker">Problema</div>
    <h3><b>Prompting non basta</b></h3>
    <p>Su COP non banali la qualità può degradare: contesti lunghi + struttura tipo grafo</p>
  </Card>
  <Card v-click>
    <div class="kicker">Input</div>
    <h3><b>Text-attributed COP</b></h3>
    <p>Task + instance description: il problema arriva come <b>testo</b> (non solo feature numeriche)</p>
  </Card>
  <Card v-click>
    <div class="kicker">Bridge</div>
    <h3><b>LLM frozen → embedding</b></h3>
    <p>L’LLM (congelato) fa da <b><i>encoder</i></b> e allinea le istanze in uno spazio vettoriale comune</p>
  </Card>
  <Card v-click>
    <div class="kicker">Solving</div>
    <h3><b>Transformer + RL</b></h3>
    <p>Un <b><i>solution generator</i></b> costruisce la soluzione, allenato in multi-task con RL</p>
  </Card>
</CardGrid>

<Callout v-click><b>Direct solving</b>: con input <i>testuale</i> invece che solo numerico + basato su reti neurali</Callout>

<!--
- **Pain point:** **prompting** da solo fatica quando il problema cresce (contesto lungo, vincoli, struttura a grafo).
- **Text-attributed COPs:** l’input non è solo numeri: è **testo** (descrizione del task + dettagli dell’istanza).
- **LLM frozen:** l’LLM qui fa da **<i>encoder</i> semantico** (non è quello che “risolve” davvero).
- **Transformer solver:** un modello più leggero impara a costruire la soluzione (stile <i>neural combinatorial optimization</i>).
- **Multi-task RL (CGERL - Conflict Gradients Erasing Reinforcement Learning):** allenano su COP diversi e gestiscono i **conflitti di gradiente** per non peggiorare un task mentre migliori un altro.
- **Takeaway:** è un bridge pratico: sfrutti semantica dell’LLM, ma tieni il solving in un modello addestrabile/controllabile.
- **Riferimenti (paper):** Abstract p.1 + Fig.1 p.3 (arXiv:2408.12214v2).
-->

---
layout: center
hideFooter: true
kicker: "Case study — Jiang et al. (framework)"
---

<Figure
  src="/fig/jiang_fig1_framework.png"
  alt="The illustration of the proposed framework (LNCS)"
  caption="The illustration of the proposed framework. [Blue part]: The LLM is frozen and takes as input the TAI for different COPs, producing task embedding and initial node embedding. [Orange part]: The encoder of the trainable solution generator processes the embedding through the attention blocks and produces instance embeddings, which is further used to construct solutions by a decoder."
  maxHeight="500px"
  source="[Jiang et al. 2024 (arXiv:2408.12214v2), Fig.1, PDF p.3]"
/>

<!--
*   **Input Testuale (TAI):** Il problema viene diviso in due parti testuali: *Task Description* (regole generali del problema) e *Instance Description* (dati specifici come città o oggetti). 

*   **LLM come Encoder (Frozen):** Un LLM pre-addestrato (con parametri congelati) legge il testo e lo converte in vettori numerici (*embeddings*), creando una rappresentazione matematica unificata per problemi diversi. 

*   **Solution Generator (Trainable):** Una rete Transformer più piccola riceve gli embeddings dall'LLM e li elabora per capire le relazioni tra gli elementi (es. distanze tra città).

*   **Decoder Dinamico:** Il decoder costruisce la soluzione passo dopo passo, tenendo conto del contesto attuale (es. "dove sono ora?") e dei vincoli rimanenti (es. "quanto spazio ho nel camion?"). 

*   **Training Multi-Task (CGERL - Conflict Gradients Erasing Reinforcement Learning):** Il modello viene addestrato con Reinforcement Learning su più problemi contemporaneamente, usando una tecnica speciale per evitare che imparare un compito peggiori le prestazioni su un altro.
-->

---
kicker: "Case study — Jiang et al. (results)"
---

## Risultati

<CardGrid cols="2" class="deck-grid">
  <Card v-click>
    <div class="kicker">Performance</div>
    <h3><b>Qualità > prompting</b></h3>
    <p>Con LNCS, riportano <b>soluzioni più competitive</b> rispetto a approcci LLM “solo prompt” e altre baseline LLM-based.</p>
  </Card>
  <Card v-click>
    <div class="kicker">Generalità</div>
    <h3><b>Un modello, più COP</b></h3>
    <p>Stesso schema “testo → embedding → soluzione” su più problemi (es. TSP/CVRP/KP), senza un solver ad-hoc per ogni task.</p>
  </Card>
  <Card v-click>
    <div class="kicker">Training</div>
    <h3><b>Multi-task più stabile</b></h3>
    <p>La parte “conflict-free” (CGERL) serve a <b>ridurre conflitti</b> tra task durante l’addestramento multi-problema.</p>
  </Card>
  <Card v-click>
    <div class="kicker">Valutazione</div>
    <h3><b>Metriche “ancora”</b></h3>
    <p>Quando possibile usano metriche tipo <i>optimality gap</i> (o confronti con solver/euristiche) per ancorare i risultati.</p>
  </Card>
</CardGrid>

<Callout v-click><b>Collegamento al survey:</b> è direct solving che “regge” perché ha <b>training</b> + <b>metriche</b>, non solo testo in input.</Callout>

<style>
.jiang-framework-grid {
  margin-top: 14px;
  margin-bottom: 14px;
}
.jiang-framework-grid .card {
  min-height: 180px;
}
</style>

<!--
- **Come la racconto** — “non vi sto vendendo un numero: vi sto vendendo l’idea che *allenare* un generatore + usare metriche serie cambia la qualità.”
- **Performance** — gli autori mostrano gap migliori rispetto a baseline LLM-based e risultati competitivi su più COP (claim attribuito al paper).
- **Perché è credibile** — usano metriche tipo <i>optimality gap</i> e confronti con solver/euristiche: non è solo ‘sembra giusto’.
- **CGERL** — la parte ‘conflict-free’ è proprio per non far litigare i task durante il multi-task.
- **Takeaway** — direct solving sì, ma con <b>addestramento</b> e <b>valutazione</b> agganciata a vincoli/metriche.
- **Riferimenti (paper)** — Table II p.7 + Abstract p.1 (arXiv:2408.12214v2).
-->