# ControlPanel

## Allgemeines

Beim Start des ControlPanels muss das Modell betriebsbereit sein: Akku geladen und angeschlossen, Modell und Fernsteuerung eingeschaltet und gebunden, Servos beweglich.

Das System wird automatisch erkannt und alle Module werden angezeigt.

![](images/image\_023.png)

image72.png

 ![](images/image\_040.png)

image73.png

## Modulübersicht

Durch Klick auf ein Modul gelangen Sie zur Ausgangsübersicht. Dort können Sie Namen vergeben, Ein- und Ausschaltgeschwindigkeiten einstellen und je nach Funktion weitere Parameter konfigurieren.

Änderungen speichern Sie mit dem Diskettensymbol. Hilfen sind über das Fragezeichen verfügbar. Mit dem Augensymbol können Ausgänge am Modell direkt aktiviert werden, um die Zuordnung zu erleichtern.

![](images/image\_025.png)

image74.png

## Doppelbelegung

Jeder Ausgang kann doppelt belegt werden. Beispiel:

- Erste Ebene: Standlicht & Fernlicht
- Zweite Ebene: Warnblinker

Die Umschaltung zwischen Ebenen ist konfigurierbar.

![](images/image\_026.png)

image75.png

 bis ![](images/image\_027.png)

image77.png

## Menü

|  |  |
| --- | --- |
| **Datei** | System neu verbinden, Module neu laden, temporäre Änderungen verwerfen, Module speichern und öffnen. |
| **Module** | Alle Module anzeigen und laden. |
| **Systemeinstellungen** | Grundlegende Systemkonfiguration. |
| **Geräteinformationen** | Informationen zu Modulen, Updates, Werkseinstellungen. |
| **Systemanalyse** | Selbsttest, Kommunikationstest, Suche nach beschädigten Modulen. |
| **Kanäle Einlernen Assistent** | Unterstützt beim Einlernen der Kanäle. |
| **Logging** | Kommunikationsprotokoll zur Fehlersuche. |
| **Live-Daten Assistent** | Echtzeitanzeige von Knüppelstellungen und Schaltzuständen. |
| **Effekt-Assistenten** | Konfiguration von Rundumlicht- und KnightRider-Effekten. |
| **Einstellungen** | Erweiterte Optionen, Expertenmodus (Warnung vor möglichen Schäden). |
| **Info** | Informationen zum ControlPanel und Fehlerberichte. |

## Symbolleiste

![](images/image\_028.png)

image85.png

- Hauptbildschirm anzeigen
- System neu verbinden
- Module neu laden
- Licht Aus / Standlicht / Abblendlicht / Fernlicht / Nebelscheinwerfer / Nebelschlussleuchte Ein/Aus
- Live-Daten anzeigen
- Geräteinformationen
- Systemeinstellungen
- Live Ausgang anzeigen
- Live Update öffnen

## Live-Daten

Die Live-Daten-Ansicht zeigt Knüppelpositionen und Schaltzustände in Echtzeit. Kanäle können eingelernt und Funktionen ein- oder ausgeschaltet werden.

![](images/image\_029.png)

image86.png

|  |  |
| --- | --- |
| [[IMAGE\_078]] | Wenn die Kanäle richtig eingelernt sind, müssen die blauen Punkte Ihren Knüppelbewegungen folgen.Sollten Sie CPPM, IBUS oder SBUS verwenden, müssen die Kanäle auch richtig zugeordnet werden. |
| 665544332211 [[IMAGE\_079]] | Hier werden alle Kanäle angezeigt, wie sie tatsächlich gemessen werden. Die Einlerninformationen werden hier nicht berücksichtigt, d.h. die Balken können sich auch nach unten bewegen, obwohl der Knüppel nach oben bewegt wird.1: Eine Änderung der Kanalzuordnung sollte nur erfolgen, wenn CPPM, IBUS oder SBUS verwendet wird.2-5: Diese Werte werden durch den Einlernvorgang gesetzt. 1000 – 2000 und 1500 Mittelstellung sind die Standardwerte. Die Werte können angepasst und gespeichert werden.6: Nach rechts scrollen, um die Werte für die anderen Kanäle anzuzeigen (nur relevant für CPPM, IBUS, SBUS) |
|  | Die rechte Seite der LiveDaten zeigt die Schaltzustände an. Teilweise können Sie durch Anklicken gesetzt werden.Die drei Funktionsgruppen Basislichtfunktionen, Zusatzfunktionen und Analog können als Schalter bei den Funktionen verwendet, wie z.B. bei der Funktion Einfachschalter. [[IMAGE\_080]] [[IMAGE\_081]] |

![](images/image\_030.png)

image87.png

Bei korrektem Einlernen folgen die blauen Punkte den Knüppelbewegungen. Für CPPM, I-BUS oder S-BUS muss die Kanalzuordnung korrekt sein.

![](images/image\_031.png)

image88.png

Die rechte Seite zeigt Schaltzustände, die teilweise per Klick geändert werden können.

![](images/image\_032.png)

image90.png

 ![](images/image\_033.png)

image91.png

## Updates

Nach dem Verbinden zeigt das ControlPanel verfügbare Updates für Busmodule an.

![](images/image\_043.png)

image6.png

Tipps für ein sicheres Update:

- Nur ein Modul gleichzeitig updaten.
- Stromunterbrechungen vermeiden.
- Servos und Motoren während des Updates abklemmen.
- Modell und ControlPanel bei Problemen neu starten.

![](images/image\_035.png)

image92.png

 ![](images/image\_043.png)

image6.png

Updates können Werkseinstellungen zurücksetzen. Das ControlPanel sichert alle Einstellungen automatisch auf der Festplatte.

![](images/image\_037.png)

image93.png

 ![](images/image\_038.png)

image94.png

 ![](images/image\_039.png)

image95.png

Nach Updates werden alle Module angezeigt. Der KLM 4/16 besteht aus dem Hauptmodul mit vier Servoausgängen und der integrierten Schalterweiterung mit 16 Schaltausgängen.

![](images/image\_040.png)

image73.png

## Geräteinformationen

Anzeige grundlegender Informationen zu Modulen. „Zeige Gerät“ schaltet die ersten drei Ausgänge ein, hilfreich bei mehreren Erweiterungen ohne Namensvergabe.

Module können neu gestartet, auf Werkseinstellungen zurückgesetzt oder aktualisiert werden.

![](images/image\_041.png)

image96.png

## Systemanalyse

Hilft bei der Fehlersuche durch Auslesen von Informationen, Suche nach beschädigten Modulen und Kommunikationstests.

![](images/image\_042.png)

image97.png

 ![](images/image\_043.png)

image6.png

## Kanäle einlernen

Der Assistent unterstützt beim Einlernen der Kanäle. Stellen Sie zuvor die richtige Belegung für K1 und K2 ein, insbesondere bei Verwendung von Steuerpads.

![](images/image\_044.png)

image98.png
