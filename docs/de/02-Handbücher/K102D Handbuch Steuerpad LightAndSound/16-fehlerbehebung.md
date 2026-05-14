# Fehlerbehebung

## Das Pad schaltet Funktionen nicht zuverlässig oder falsch

- Prüfen Sie zuerst, ob der KLM korrekt konfiguriert ist. Öffnen Sie die Systemeinstellungen und kontrollieren Sie die Einträge „Belegung K1“ bzw. „Belegung K2“.
- Drücken Sie die Tasten in folgender Reihenfolge und prüfen Sie, ob die Werte jeweils um 14,5 % abnehmen, beginnend links oben mit 100, 85,5, 71, 56,5, 42, 27,5 % bzw. rechts oben mit -100, -85,5, -71, -56,5, -42, -27,5 %.

![](images/image\_018.png)

image18.png

Ist einer der zweiten Werte (85,5 % bzw. -85,5 %) größer als 90 % bzw. kleiner als -90 %, ist die Aussteuerung zu groß. Ist einer der Werte kleiner als 15 %, lesen Sie bitte Abschnitt 5.11.

Tragen Sie außerdem die Prozentwerte für Fernlicht und Nebelscheinwerfer in die Systemeinstellungen des KLM ein (siehe Kapitel 5.9).

## Das Pad ist angeschlossen, aber in den LiveDaten bewegt sich kein Wert

- Überprüfen Sie, ob das Pad korrekt angeschlossen ist und der richtige Empfängerausgang verwendet wird.
- Ein direkt angeschlossenes Servo sollte bei Tastendruck ausschlagen.
