# Apprendimento dei canali per escursioni asimmetriche

Questa sezione è rilevante solo se tutti i passaggi precedenti sono stati eseguiti correttamente e gli abbaglianti o i fendinebbia mostrano escursioni troppo piccole o assenti.

Cause possibili:

- Posizione centrale regolata in modo errato (trimmer, subtrim)
- Limitazione elettronica del canale
- Radiocomando economico con curva di controllo non lineare

![](images/image\_019.png)

image20.png

Se possibile, azzerare tutte le impostazioni per il canale utilizzato e avviare nuovamente la procedura di apprendimento normale.

Se ciò non è possibile, la regolazione deve essere effettuata separatamente per le escursioni positive e negative.

Aprire l'assistente dati in tempo reale e concentrarsi sul valore evidenziato in basso (se si usa K2, sul valore immediatamente a sinistra). Questo valore cambia premendo il tasto e dovrebbe essere il più vicino possibile ai seguenti valori target:

| Funzione | Valore (µs) |
| --- | --- |
| Posizione centrale | 1500 |
| Tasto piano | 1000 \* |
| Luce di posizione | 1070 \*\* |
| Tasto meno | 2000 \* |
| Accoppiamento sella | 1930 \*\* |

\* A seconda del radiocomando, il tasto piano e il tasto meno possono essere invertiti.

\*\* Lo stesso vale per luce di posizione e accoppiamento sella.

Più grande è l’escursione, più i valori si allontanano da 1500 µs alla pressione del tasto. L’escursione del tasto piano dovrebbe essere il più distante possibile, mentre quella per la luce di posizione deve essere chiaramente differente. Lo stesso vale per il tasto meno e l’accoppiamento sella.

Regolare separatamente l’escursione per entrambe le direzioni:

- Premere **Setup+** e **S4** per impostare l’escursione massima per l’escursione positiva.
- Verificare i valori per il tasto piano e la luce di posizione. Se i valori sono troppo simili (ad esempio 1930 e 1925), ridurre l’escursione con **Setup+** e **S3** e controllare di nuovo. La differenza dovrebbe essere almeno di 50 µs.
- Ripetere la procedura per l’escursione negativa con **Setup-** e i tasti S corrispondenti. Controllare i valori per il tasto meno e l’accoppiamento sella.

![](images/image\_020.png)

image21.png