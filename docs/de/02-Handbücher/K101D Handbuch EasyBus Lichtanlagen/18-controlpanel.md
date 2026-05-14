# ControlPanel

## Allgemeines

Beim Start des ControlPanels muss das Modell betriebsbereit sein: Akku geladen und angeschlossen, Modell und Fernsteuerung eingeschaltet und gebunden. Servos müssen sich bewegen lassen.

Das System wird automatisch erkannt und alle Module werden geladen und angezeigt.

![](images/image\_044.png)

image72.png

 ![](images/image\_062.png)

image73.png

## Modulübersicht

Durch Klick auf ein Modul gelangt man zur Ausgangsübersicht. Dort können Namen vergeben und Ein-/Ausschaltgeschwindigkeiten eingestellt werden. Je nach Funktion variieren die Parameter (siehe Kapitel 7 „Funktionen“).

Änderungen werden mit dem Diskettensymbol gespeichert. Das Fragezeichen zeigt Hilfetexte, das Auge schaltet den Ausgang am Modell ein, um Zuordnungen zu erleichtern.

![](images/image\_046.png)

image74.png

## Doppelbelegung

Jeder Ausgang kann doppelt belegt werden. Beispiel:

- Erste Ebene: Standlicht & Fernlicht
- Zweite Ebene: Warnblinker

Die Umschaltung zwischen Ebenen kann konfiguriert werden.

![](images/image\_047.png)

image75.png

 bis ![](images/image\_048.png)

image77.png

## Menü

| Funktion | Beschreibung |
| --- | --- |
| Datei | System neu verbinden, Modul neu laden, temporäre Änderungen verwerfen, Module speichern und öffnen. |
| Module | Alle Module anzeigen und laden. |
| Systemeinstellungen | Grundlegendes Systemverhalten konfigurieren. |
| Geräteinformationen | Informationen zu Modulen, Softwareversionen, Updates, Werkseinstellungen. |
| Systemanalyse | Selbsttest, Kommunikationstest, beschädigte Module finden. |
| Kanäle Einlernen Assistent | Unterstützt beim Einlernen der Kanäle. |
| Logging | Kommunikation zwischen ControlPanel und System zur Fehlersuche. |
| Live-Daten Assistent | Zeigt Echtzeitdaten wie Knüppelausschläge und Schaltzustände. |
| Rundumlicht- und KnightRider-Effekt Assistent | Hilft bei Konfiguration über mehrere Ausgänge. |
| Einstellungen | Expertenoptionen für erweiterte Einstellungen (mit Vorsicht verwenden). |
| Info | Informationen über ControlPanel und Fehlerberichte. |

![](images/image\_049.png)

image78.png

## Symbolleiste

![](images/image\_050.png)

image85.png

- Hauptbildschirm anzeigen
- System neu verbinden
- Module neu laden
- Licht aus / Standlicht / Abblendlicht / Fernlicht / Nebelscheinwerfer / Nebelschlussleuchte Ein/Aus
- Live-Daten, Geräteinformationen, Systemeinstellungen
- Live-Ausgang anzeigen, Live-Update öffnen

## Live-Daten

Erlaubt Echtzeiteinblick in Knüppelpositionen und Schaltzustände. Kanäle können eingelernt und Funktionen ein-/ausgeschaltet werden.

![](images/image\_051.png)

image86.png

|  |  |
| --- | --- |
| [[IMAGE\_078]] | Wenn die Kanäle richtig eingelernt sind, müssen die blauen Punkte Ihren Knüppelbewegungen folgen.Sollten Sie CPPM, IBUS oder SBUS verwenden, müssen die Kanäle auch richtig zugeordnet werden. |
| 665544332211 [[IMAGE\_079]] | Hier werden alle Kanäle angezeigt, wie sie tatsächlich gemessen werden. Die Einlerninformationen werden hier nicht berücksichtigt, d.h. die Balken können sich auch nach unten bewegen, obwohl der Knüppel nach oben bewegt wird.1: Eine Änderung der Kanalzuordnung sollte nur erfolgen, wenn CPPM, IBUS oder SBUS verwendet wird.2-5: Diese Werte werden durch den Einlernvorgang gesetzt. 1000 – 2000 und 1500 Mittelstellung sind die Standardwerte. Die Werte können angepasst und gespeichert werden.6: Nach rechts scrollen, um die Werte für die anderen Kanäle anzuzeigen (nur relevant für CPPM, IBUS, SBUS) |
|  | Die rechte Seite der LiveDaten zeigt die Schaltzustände an. Teilweise können Sie durch Anklicken gesetzt werden.Die drei Funktionsgruppen Basislichtfunktionen, Zusatzfunktionen und Analog können als Schalter bei den Funktionen verwendet, wie z.B. bei der Funktion Einfachschalter. [[IMAGE\_080]] [[IMAGE\_081]] |

![](images/image\_052.png)

image87.png

Die blauen Punkte müssen den Knüppelbewegungen folgen. Bei CPPM, IBUS oder SBUS müssen Kanäle korrekt zugeordnet sein.

![](images/image\_053.png)

image88.png

Die rechte Seite zeigt Schaltzustände, die auch per Klick gesetzt werden können. Die drei Funktionsgruppen Basislicht, Zusatzfunktionen und Analog können als Schalter verwendet werden.

![](images/image\_054.png)

image90.png

 ![](images/image\_055.png)

image91.png
