# Installazione generale – Determinazione della disposizione dei pin

## Teoria

La determinazione della posizione dei trasmettitori nella maggior parte dei radiocomandi avviene tramite potenziometri commerciali, che funzionano come classici partitori di tensione. Il principio è semplice:

- Tra i poli A e B si trova uno strato di carbone.
- Un contatto mobile (la cosiddetta "radice") si sposta lungo questo strato.
- La tensione misurata sulla radice è una parte della tensione applicata tra A e B.

Esempio: Se tra A e B ci sono 5 V e la leva è al centro, si misurano circa 2,5 V tra A e W e tra W e B. Muovendo la leva, le tensioni cambiano di conseguenza.

![](images/image\_010.png)

image11.png

## Pratica – Determinazione della disposizione dei pin

1. Accendere il radiocomando e prendere un multimetro.
2. Evitare cortocircuiti e contatti con altri poli durante la misurazione.
3. Controllare che i cavi del multimetro siano collegati correttamente (nero su COM, rosso su V).
4. In caso di dubbio, verificare la polarità con una batteria.
5. Misurare le tensioni tra i pin e annotare i valori:

- Pin 1 contro Pin 2
- Pin 1 contro Pin 3
- Pin 2 contro Pin 3

6. La tensione più alta misurata corrisponde alla tensione di alimentazione (tipicamente 3 V, 3,3 V o 5 V).
7. Il cavo marrone va collegato al polo negativo (massa), il rosso al polo positivo.
8. Il cavo arancione va collegato al pin rimanente (radice).

Premere ora il tasto in alto a sinistra sul pad. Un servo collegato all'uscita corrispondente del ricevitore dovrebbe muoversi. Se il movimento è troppo piccolo, la regolazione può essere modificata successivamente.

Per connessioni a 3 poli con passo 2,54 mm può essere utilizzato il connettore fornito. In caso contrario, il cavo a presa può essere saldato e il pad inserito.