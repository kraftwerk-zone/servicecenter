# Strutture dati

## Funzioni di base (Tag 0x01)

Le funzioni di base sono codificate in 5 byte:

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Quattro frecce | Freccia sinistra | Freccia destra | Abbagliante lampeggiante | Fendinebbia | Abbagliante | Anabbagliante | Luci di posizione |
| 1 | Piedini di supporto su | Ruota di scorta | Motore acceso | Avvio | Clacson | Luce posteriore nebbia | Luce freno | Luce retromarcia |
| 2 | Freccia destra impulso | Luce rotante | Luci diurne | Luce curva sinistra | Luce curva destra | Cassone giù | Cassone su | Piedini di supporto giù |
| 3 | Interno/RFU | Clacson segnale | Marcia giù | Marcia su | Luce curva sinistra | Luce curva destra | Interno/RFU | Freccia sinistra impulso |
| 4 | Servo 2 | Servo 1 | Marcia 2/2 | Marcia 1/2 | Livello pad | Rampa giù | Rampa su | Interno/RFU |

## Funzioni aggiuntive (Tag 0x05)

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | CH1 Memoria Half Short Destra | CH1 Memoria Half Short Sinistra | CH1 Destra Pieno | CH1 Sinistra Pieno | CH1 Memoria Pieno Lungo Destra | CH1 Memoria Pieno Lungo Sinistra | CH1 Memoria Pieno Corto Destra | CH1 Memoria Pieno Corto Sinistra |
| 1 | CH2 Memoria Pieno Lungo Destra | CH2 Memoria Pieno Lungo Sinistra | CH2 Memoria Pieno Corto Destra | CH2 Memoria Pieno Corto Sinistra | CH1 Destra Mezzo | CH1 Sinistra Mezzo | CH1 Memoria Half Lungo Destra | CH1 Memoria Half Lungo Sinistra |
| 2 | CH2 Destra Mezzo | CH2 Sinistra Mezzo | CH2 Memoria Half Lungo Destra | CH2 Memoria Half Lungo Sinistra | CH2 Memoria Half Corto Destra | CH2 Memoria Half Corto Sinistra | CH2 Destra Pieno | CH2 Sinistra Pieno |
| … | … | | | | | | | |
| 45 | CH31 Memoria Half Short Destra | CH31 Memoria Half Short Sinistra | CH31 Destra Pieno | CH31 Sinistra Pieno | CH31 Memoria Pieno Lungo Destra | CH31 Memoria Pieno Lungo Sinistra | CH31 Memoria Pieno Corto Destra | CH31 Memoria Pieno Corto Sinistra |
| 46 | CH32 Memoria Pieno Lungo Destra | CH32 Memoria Pieno Lungo Sinistra | CH32 Memoria Pieno Corto Destra | CH32 Memoria Pieno Corto Sinistra | CH31 Destra Mezzo | CH31 Sinistra Mezzo | CH31 Memoria Half Lungo Destra | CH31 Memoria Half Lungo Sinistra |
| 47 | CH32 Destra Mezzo | CH32 Sinistra Mezzo | CH32 Memoria Half Lungo Destra | CH32 Memoria Half Lungo Sinistra | CH32 Memoria Half Corto Destra | CH32 Memoria Half Corto Sinistra | CH32 Destra Pieno | CH32 Sinistra Pieno |

## Funzioni proporzionali (Tag 0x41)

I valori sono numeri interi con segno a 16 bit nell’intervallo da -500 a +500, che corrispondono a una visualizzazione da -100% a +100%. I dati sono in formato Little-Endian.

| CH1 (Gas) | CH2 (Sterzo) | CH3 | CH4 | … | CH31 | CH32 |
| --- | --- | --- | --- | --- | --- | --- |