# Einstellmöglichkeiten

## Systemeinstellungen

Systemeinstellungen gelten für das gesamte Modul oder System (z. B. Blinkintervall, Empfängertyp, Bremslichttyp). Sie öffnen diese über das Zahnradsymbol oder das Menü „System“ → „Systemeinstellungen“.

![](images/image\_009.png)

image41.png

 ![](images/image\_010.png)

image42.png

| Name | Beschreibung |
| --- | --- |
| Startverzögerung [s] | Verzögert den Systemstart, um Anlaufzeiten der Fernsteuerung zu berücksichtigen. |
| Einlernmodus [aktiv] | Aktiviert/deaktiviert den manuellen Einlernmodus (Gas- und Lenkknüppel in Endausschlag). ControlPanel-Einlernen bleibt aktiv. |
| Infrarot [ein] | Schaltet Ausgang 8 auf Infrarotbetrieb um. |
| Blinker Ein/Aus | Definiert Ein- und Auszeit des Blinkers in 10 ms Schritten. |
| Empfängertyp | Siehe Abschnitt 8 „Ansteuerungsvarianten / Empfängertyp“. |
| Fahrtenreglertyp | Siehe Abschnitt 9.1 „Fahrtenreglertyp“. |
| Warnblinker beim Rückwärtsfahren | Automatische Aktivierung des Warnblinkers bei Rückwärtsfahrt. |
| Bremslicht Sensitivität | Empfindlichkeit des intelligenten Bremslichts. |
| Bremslicht Nachleuchten | Dauer des Nachleuchtens des Bremslichts. |
| Lenkungstyp | Siehe Abschnitt 9.3 „Lenkungstyp“. |
| Blinker Schwellwert | Schwellenwert für automatische Blinkeraktivierung. |
| Kurvenlichttyp | Siehe Abschnitt 0 „Kurvenlichttyp“. |
| Motor läuft sofort [aktiv] | Siehe Abschnitt 10 „Soundmodul“. |
| Motor Start Dauer | Dauer des Motorstart-Flackerns. |
| Pad Alles Ein/Aus | Konfiguration der „Alles Ein/Aus“-Taste der Steuerpads. |
| Pad Light&Sound Fernlicht / Nebelscheinwerfer | Siehe Handbuch Steuerpad Licht & Sound. |
| Belegung K1 – K12 | Siehe Abschnitt 13.6 „Benutzerdefiniert“. |

## Steuerung der Funktionen Licht – Fahren – Zusatz

Die Standardsteuerung erfolgt über vier Proportionalkanäle (Gas links, Lenkung rechts). Kanal K2 schaltet zwischen den Funktionsgruppen Licht, Fahren und Zusatz.

![](images/image\_011.png)

image43.png

**Einlernen der Kanäle:**

1. Gas – Bremse
2. Links – Rechts
3. K1 links – rechts
4. K2 hoch – runter

![](images/image\_012.png)

image44.png

## Lichtfunktionen schalten

- Standlicht, Abblendlicht: K2 hoch + K1 kurz links tippen
- Fernlicht: K2 hoch + K1 kurz rechts tippen (nur wenn Standlicht an)
- Nebelscheinwerfer, Nebelschlussleuchte: K2 hoch + K1 lang rechts tippen (nur wenn Standlicht an)
- Blinker links/rechts: K2 Mitte + K1 kurz links/rechts tippen
- Warnblinker: K2 Mitte + K1 lang rechts tippen
- Lichthupe: K2 Mitte + K1 lang links tippen (nach erstem Einschalten kann K1 links direkt gesteuert werden)
- Zusatzfunktionen: K2 runter + K1 in Endausschlag (links/rechts) kurz oder lang betätigen

![](images/image\_013.png)

image45.png

 bis ![](images/image\_014.png)

image54.png

## Pad Grund- oder Zusatzfunktionen

Pads codieren Tastendrücke in Auf- und Abwärtsbewegungen. Der KLM dekodiert diese und steuert die Funktionen. Pads werden am Fernsteuersender angeschlossen und an K1 oder K2 des KLM angeschlossen.

Für das Einlernen der Kanäle muss das Pad in den Setup-Modus versetzt werden (gleichzeitiges Drücken der beiden oberen rechten Setup-Tasten). Alternativ nutzen Sie den „Kanäle Einlernen“-Assistenten im ControlPanel.

![](images/image\_015.png)

image61.png

 ![](images/image\_016.png)

image63.png

## Pad Licht & Sound

Steuert Funktionen je nach Tastendruck mit Ausschlägen von +100 bis -100%. Anschluss und Bedienung analog zu Grund- und Zusatzfunktionen.

![](images/image\_017.png)

image65.png

Funktionen sind in kurze, lange und Zusatzebenen unterteilt. Lichthupe, Hupe und weitere Funktionen werden durch lange Betätigung aktiviert und können danach mit kurzen Betätigungen gesteuert werden.

Nach zwei Sekunden Inaktivität wird die ursprüngliche Belegung wiederhergestellt.

![](images/image\_018.png)

image67.png

## Multiswitch Robbe/Graupner

Beide Protokolle werden automatisch erkannt. Multiswitch-Werte können im LiveDaten-Assistenten den Kanälen K3 bis K12 zugewiesen und benutzerdefiniert belegt werden.

![](images/image\_019.png)

image68.png

## Benutzerdefiniert

Jeder Kanal (außer Gas und Lenkung) kann individuell belegt werden. K1 und K2 unterstützen Voll- und Halbausschläge, K3 bis K12 nur Vollausschläge.

![](images/image\_020.png)

image69.png

 ![](images/image\_021.png)

image70.png

Funktionen können als „Dauer“, „Memory kurz“ oder „Memory lang“ definiert werden. Beispiele sind Lichtfunktionen, Hupe, Sattelkupplung, Stützen, Mulde, Rampe, Starten, Schalten, Servo1/2 usw.

![](images/image\_022.png)

image71.png
