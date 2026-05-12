# ControlPanel

## Allgemeines

Beim Start des ControlPanels muss das Modell betriebsbereit sein: Akku geladen und angeschlossen, Modell eingeschaltet, Fernsteuerung eingeschaltet und gebunden. Servos sollten sich bewegen lassen. Das System wird automatisch erkannt und alle Module werden angezeigt.

![](images/image\_030.png)

image72.png

 ![](images/image\_049.png)

image73.png

## Modulübersicht und Ausgangsübersicht

Durch Klicken auf ein Modul gelangen Sie zur Ausgangsübersicht. Diese variiert je nach Modultyp (Schalt-, Servo- oder Motorerweiterung) und Anzahl der Ausgänge. Für jeden Ausgang können Name, Ein- und Ausschaltgeschwindigkeit sowie weitere Parameter eingestellt werden.

Änderungen werden mit dem Diskettensymbol gespeichert. Das Fragezeichen zeigt Hilfetexte, das Augensymbol schaltet den Ausgang am Modell ein, um die Zuordnung zu erleichtern.

![](images/image\_032.png)

image74.png

## Doppelbelegung

Jeder Ausgang kann doppelt belegt werden, z.B. Grundfunktion „Standlicht & Fernlicht“ und zweite Ebene „Warnblinker“ oder „Stroboskop“.

|  |  |
| --- | --- |
| Jeder Ausgang kann über die Auswahlliste auf der rechten Seite doppelt belegt werden.Bsp: Erste Ebene: Funktion Standlicht & Fernlicht | [[IMAGE\_072]] |
| Mit dem Eintrag Erste -> Zweite kann konfiguriert werden, wie auf die zweite Ebene geschaltet werden soll, z.B. Grundfunktionen Warnblinker | [[IMAGE\_073]] |
| Unter Zweite Ebene kann wie gewohnt eine Funktion eingestellt werden, z.B.: Stroboskop auf Grundfunktionen Warnblinker.Erste Ebene: Stand- & Fernlicht |
| Erste Zweite Warnblinker |
| Zweite Ebene: Strobokskop |
| Das Resultat ist ein Blitzer über das Fahrlicht, wenn der Warnblinker eingeschaltet wird. | [[IMAGE\_074]] |

![](images/image\_033.png)

image75.png

 ![](images/image\_034.png)

image76.png

 ![](images/image\_035.png)

image77.png

## Menü

| Menüpunkt | Funktion |
| --- | --- |
| Datei | System neu verbinden, Modul neu laden, temporäre Änderungen verwerfen, Module speichern und laden. |
| Module | Anzeige und Auswahl aller Module. |
| Systemeinstellungen | Konfiguration des Systemverhaltens. |
| Geräteinformationen | Anzeige von Softwareversionen, Updates, Werkseinstellungen und Reset. |
| Systemanalyse | Selbsttest, Kommunikationstest, Suche beschädigter Module. |
| Assistenten | Kanäle einlernen, Live-Daten, Rundumlicht- und KnightRider-Effekt Assistent. |
| Logging | Kommunikationsprotokoll zur Fehlersuche. |
| Hilfe | Informationen zum ControlPanel und Fehler melden. |

![](images/image\_036.png)

image78.png

## Symbolleiste

![](images/image\_037.png)

image85.png

Symbole von links nach rechts: Hauptbildschirm, Verbinden, Neu laden, Licht Aus, Standlicht, Abblendlicht, Fernlicht, Nebelscheinwerfer, Nebelschlussleuchte, Ein/Aus, Live Daten, Geräteinformationen, Systemeinstellungen, Live Zeige Ausgang, Live Update öffnen.

## Live Daten

Die Live-Daten-Ansicht zeigt Knüppelpositionen und Schaltzustände in Echtzeit. Kanäle können eingelernt und Funktionen direkt ein- oder ausgeschaltet werden.

![](images/image\_038.png)

image86.png

|  |  |
| --- | --- |
| [[IMAGE\_078]] | Wenn die Kanäle richtig eingelernt sind, müssen die blauen Punkte Ihren Knüppelbewegungen folgen.Sollten Sie CPPM, IBUS oder SBUS verwenden, müssen die Kanäle auch richtig zugeordnet werden. |
| 665544332211 [[IMAGE\_079]] | Hier werden alle Kanäle angezeigt, wie sie tatsächlich gemessen werden. Die Einlerninformationen werden hier nicht berücksichtigt, d.h. die Balken können sich auch nach unten bewegen, obwohl der Knüppel nach oben bewegt wird.1: Eine Änderung der Kanalzuordnung sollte nur erfolgen, wenn CPPM, IBUS oder SBUS verwendet wird.2-5: Diese Werte werden durch den Einlernvorgang gesetzt. 1000 – 2000 und 1500 Mittelstellung sind die Standardwerte. Die Werte können angepasst und gespeichert werden.6: Nach rechts scrollen, um die Werte für die anderen Kanäle anzuzeigen (nur relevant für CPPM, IBUS, SBUS) |
|  | Die rechte Seite der LiveDaten zeigt die Schaltzustände an. Teilweise können Sie durch Anklicken gesetzt werden.Die drei Funktionsgruppen Basislichtfunktionen, Zusatzfunktionen und Analog können als Schalter bei den Funktionen verwendet, wie z.B. bei der Funktion Einfachschalter. [[IMAGE\_080]] [[IMAGE\_081]] |

![](images/image\_039.png)

image87.png

Wenn Kanäle korrekt eingelernt sind, folgen die blauen Punkte den Knüppelbewegungen. Bei CPPM, IBUS oder SBUS müssen die Kanäle zusätzlich zugeordnet werden.

![](images/image\_040.png)

image88.png

Die rechte Seite zeigt Schaltzustände, die teilweise per Klick gesetzt werden können. Die drei Funktionsgruppen Basislicht, Zusatzfunktionen und Analog können als Schalter verwendet werden.

![](images/image\_041.png)

image90.png

 ![](images/image\_042.png)

image91.png
