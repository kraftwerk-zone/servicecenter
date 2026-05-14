# Comportamento di guida

## Tipo di regolatore di marcia

Fondamentalmente, ogni regolatore di marcia è compatibile con EasyBus. Per un corretto controllo della luce di frenata e retromarcia, deve essere impostato il tipo di regolatore di marcia corretto:

- **Semplice:** la retromarcia parte immediatamente quando la leva viene spostata indietro.
- **Freno separato:** prima il freno, poi la retromarcia dopo un nuovo tiro.
- **Tempomat standard:** il rallentamento passa direttamente alla retromarcia.
- **Tempomat Servonaut:** cambio marcia tramite K1, uscita servo impostata su „Funzione proporzionale K1“.
- **Servonaut folle:** come Tempomat Servonaut, ma con posizione folle tra avanti e indietro.
- **Servonaut K40:** luce di frenata e retromarcia commutate nello stile K40.
- **Freno/luce retromarcia analogica:** ingressi di commutazione di un regolatore di marcia alimentati in modo analogico (vedi capitolo 11.4).

## Luce di frenata intelligente

La luce di frenata si accende già durante il rallentamento, non solo in retromarcia. Sensibilità e durata della luce residua sono regolabili nelle impostazioni di sistema.

## Tipo di sterzo

Di default, l’indicatore di direzione deve essere acceso manualmente e si spegne automaticamente. In alternativa, si può scegliere l’„Indicatore automatico“, che si attiva automaticamente in curva. La „Soglia indicatore“ definisce la soglia di attivazione.

## Tipo di luce curva

Il comportamento della luce curva è regolabile tramite il parametro „Tipo di luce curva“. Le opzioni sono autoesplicative.