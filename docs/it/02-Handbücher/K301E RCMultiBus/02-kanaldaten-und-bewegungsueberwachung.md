# Dati del canale e monitoraggio del movimento

Ogni valore del canale viene salvato e può essere assegnato individualmente a ogni uscita servo o motore. Inoltre, viene monitorato il movimento di ogni canale, dal quale viene generato un campo di bit. Questo campo di bit ha tre dimensioni:

- **Direzione:** alto (top) / basso (bottom)
- **Intensità del movimento:** pieno (full) / metà (half)
- **Stato:** permanente / in memoria (memory)

| CH | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH1 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| CH2 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| … |  |  |  |  |  |  |  |
| CHx | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |

## Esempi di monitoraggio del movimento

- **Esempio 1:** Il canale 4 viene spostato al +30% → viene impostato il flag *CH4 Permanent/Top/Half*.
- **Esempio 2:** Il canale 4 viene riportato indietro entro 0,5 secondi → il flag *CH4 Permanent/Top/Half* viene cancellato, viene impostato il flag *CH4 Memory/Top/Half*.
- **Esempio 3:** Il canale 1 viene spostato al -100% → viene impostato il flag *CH1 Permanent/Bottom/Full*.
- **Esempio 4:** Il canale 1 viene riportato indietro dopo un secondo → il flag *CH1 Permanent/Bottom/Full* viene cancellato, viene impostato il flag *CH1 Memory/Bottom/Full*.