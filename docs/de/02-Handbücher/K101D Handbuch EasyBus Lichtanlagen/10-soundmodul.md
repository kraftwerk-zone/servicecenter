# Soundmodul

Soundmodule können direkt am Empfänger betrieben werden. Für die Steuerung über EasyBus müssen sie an zwei Servoausgänge angeschlossen werden (direkt am KLM 4/16 oder an KSB 2/4).

## Servonaut SMT kompatibel

Ein Kanal für Gasinformation, der zweite zum Starten/Stoppen und Hupen (in entgegengesetzte Richtungen getastet).

![](images/image\_019.png)

image30.png

## Programmierbare Soundmodule (z.B. BEIER USM-RC)

Basieren auf Servonaut-Modus, erweitern aber die Möglichkeit, eine zweite Hupe anzusteuern.

![](images/image\_020.png)

image31.png

Im Soundmodul sind folgende Einstellungen vorzunehmen:

![](images/image\_021.png)

image32.png

## Steuerung des Soundmoduls

Mit dem Steuerpad Licht & Sound sind keine weiteren Einstellungen nötig. Die Hupentaste steuert die Hupe, die Ebenentaste startet bzw. stoppt den Motor.

Die Zusatzkanäle K1 und K2 (bzw. bis K10 bei Verwendung von IBUS, SBUS, SUMD etc.) können in den Systemeinstellungen benutzerdefiniert belegt werden.

![](images/image\_022.png)

image33.png

Eine Mischung aus Steuerpad und benutzerdefinierter Belegung ist ebenfalls möglich.

![](images/image\_023.png)

image34.png

## Wichtige Einstellungen

- **Motor läuft sofort:** Je nachdem, ob das Soundmodul den Motor sofort startet, muss die Systemeinstellung „Motor läuft sofort [aktiv]“ gesetzt oder entfernt werden.
- **Vorsicht:** Der Fahrmotor ist in jedem Fall aktiv!
- **Lichter flackern:** Jede Beleuchtungsplatine und Schalterweiterung (KLB) hat Systemeinstellungen für „Starteffekt“ (Flackern beim Start) und „Motor Stop Lichtreduktion“ (Absenkung bei Motorstopp). Verwenden Sie letztere nur, wenn keine Komponenten mit integrierter Elektronik angesteuert werden.
- Die Dauer des Flackerns kann mit „Motor Start Dauer“ an die Soundmodul-Startdauer angepasst werden.
