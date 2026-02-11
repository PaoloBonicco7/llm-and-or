---
kicker: "Chiusura"
---

## Sintesi + direzioni future

<CardGrid cols="2" style="margin:22px -5px;">
  <Card v-click>
    <div class="kicker">Takeaway</div>
    <h3><b>3 messaggi chiave</b></h3>
    <p><b>1)</b> <i>Closed-loop</i> obbligatorio: senza feedback (solver/compilatore) l’affidabilità crolla</p>
    <p><b>2)</b> Ibridi vincenti: creatività LLM + rigore <i>solver</i> (o rete neurale) batte i singoli metodi</p>
    <p><b>3)</b> Oltre il prompting: futuro = LLM come traduttore (<i>encoding</i>) o ingegnere (<i>code gen</i>), non <i>direct solving</i> puro</p>
  </Card>
  <Card v-click>
    <div class="kicker">Sfide</div>
    <h3><b>3 problemi aperti</b></h3>
    <p><b>1)</b> Instabilità semantica: piccole variazioni NL → modelli diversi o errati</p>
    <p><b>2)</b> <i>Benchmark</i> realistici: servono dataset industriali + metriche comparabili</p>
    <p><b>3)</b> Scalabilità &amp; generalizzazione: da TSP a VRP senza ripartire da zero</p>
  </Card>
</CardGrid>

<Callout v-click><b>Il filo conduttore:</b> da <i>Wang &amp; Li</i> (la mappa) a <i>OR-LLM-Agent</i> (l’agente che si corregge) fino a <i>LNCS</i> (l’architettura neurale unificata): l’IA sta diventando l’interfaccia naturale per l’ottimizzazione complessa</Callout>

<!--
- **Messaggio di chiusura** — “LLM + OR” regge quando c’è un modo serio di verificare ciò che l’LLM propone
- **Takeaway 1** — <i>closed-loop</i> e validazione riducono errori “silenziosi” e instabilità
- **Takeaway 2** — negli ibridi, l’LLM suggerisce mosse/euristiche ma il <i>solver</i> resta il giudice su feasibility e qualità
- **Takeaway 3** — <i>direct solving</i> “puro” è limitato: futuro = <i>encoding</i>/<i>code gen</i> e loop con verifica
- **Bridge ai case** — OR-LLM-Agent: <i>execution-guided repair</i> in <i>closed-loop</i> (feedback indispensabile); Jiang (LNCS): integrazione neurale più <i>end-to-end</i>
- **Fonti** — Wang & Li (2025) Fig.2/Fig.3/Sec.5 + Zhang & Luo (2025) Alg.1 + Jiang et al. (2024) Abstract/Fig.1
-->

---
kicker: "Bibliografia"
---

## References

- Wang &amp; Li (2025) — <i>Large Language Models in Operations Research: Methods, Applications, and Challenges</i> — [arXiv:2509.18180v3](https://arxiv.org/abs/2509.18180v3)
- Zhang et al. (2025) — <i>OR-LLM-Agent: Automating Modeling and Solving of Operations Research Optimization Problems with Reasoning LLM</i> — [arXiv:2503.10009v3](https://arxiv.org/abs/2503.10009v3)
- Jiang et al. (2024) — <i>Bridging Large Language Models and Optimization: A Unified Framework for Text-attributed Combinatorial Optimization</i> — [arXiv:2408.12214v2](https://arxiv.org/abs/2408.12214v2)

<!--
NOTE:
- **Solo riferimenti** — qui niente claim tecnici: è solo la lista dei paper citati.
-->
