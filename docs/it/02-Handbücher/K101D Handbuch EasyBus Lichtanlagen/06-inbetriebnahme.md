# Messa in servizio

Per la messa in servizio dei sistemi KraftwerK EasyBus non sono necessari passaggi speciali. Tuttavia, consigliamo di seguire la seguente lista di controllo.

## Collegamento al ricevitore

![](images/image\_065.png)

image6.png

Prima di collegare il KLM 4/16 al ricevitore, si prega di verificare la configurazione delle uscite del ricevitore. Utilizzare un servo e testare ogni uscita per verificarne il corretto funzionamento. Annotare la configurazione.

![](images/image\_002.jpg)

image7.jpeg

**Nota:** Per evitare una partenza involontaria, si consiglia di sollevare il modello.

Collegare i cavi del servo per lo sterzo e il gas alle corrispondenti uscite del ricevitore. Il regolatore di velocità e il servo dello sterzo vengono collegati alle uscite servo del KLM. I canali K1 e K2 possono essere utilizzati opzionalmente.

**Suggerimento:** Il collegamento del canale gas e/o sterzo può essere omesso se luci di frenata, retromarcia e/o indicatori di direzione sono alimentati in modo analogico (vedere capitolo 11.5 „Actros 3363 luci di frenata/retromarcia e indicatori dal regolatore di velocità“).

**Suggerimento:** Regolatore di velocità e/o servo dello sterzo possono anche essere collegati direttamente al ricevitore tramite cavo a Y per escludere interferenze causate dal KLM.

## Collegamento delle schede di illuminazione

Tutte le schede di espansione o di illuminazione possono essere collegate direttamente o tramite schede di distribuzione alle uscite bus dell’assistente luci.

## Apprendimento dei canali

![](images/image\_065.png)

image6.png

L’apprendimento dei canali è il passaggio più importante per il corretto funzionamento degli impianti KraftwerK EasyBus!

Dopo ogni modifica delle impostazioni del vostro sistema di radiocomando (escursioni, direzioni di rotazione, posizioni centrali) i canali devono essere riapprenduti.

I servi e i motori controllati dagli impianti KraftwerK devono essere regolati tramite il ControlPanel – non tramite il menu del radiocomando!

1. Accendere il radiocomando. Se il motore di trazione è collegato, sollevare il modello in modo che le ruote non tocchino il suolo.
2. Accendere il modello. Dopo il doppio lampeggio del LED verde, muovere il canale gas e sterzo ciascuno per cinque secondi al finecorsa, finché il LED rosso si accende per circa un secondo.
3. Riportare i comandi nella posizione centrale.

Il LED lampeggia in base ai canali:

- 1x breve: comando gas – finecorsa gas, poi finecorsa freno
- 2x breve: comando sterzo – finecorsa sinistra, poi destra
- 3x breve: canale aggiuntivo K1 – finecorsa sinistra, poi destra
- 4x breve: canale aggiuntivo K2 – finecorsa alto, poi basso

Quando tutti i comandi sono in posizione centrale, il LED rosso si accende a lungo e segnala la fine della procedura di apprendimento. Il sistema si riavvia e indica la prontezza operativa con un doppio lampeggio verde.