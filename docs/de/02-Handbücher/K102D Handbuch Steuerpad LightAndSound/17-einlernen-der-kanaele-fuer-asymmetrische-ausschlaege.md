# Einlernen der Kanäle für asymmetrische Ausschläge

Dieser Abschnitt ist nur relevant, wenn alle vorherigen Schritte korrekt durchgeführt wurden und Fernlicht bzw. Nebelscheinwerfer zu kleine oder keine Ausschläge zeigen.

Mögliche Ursachen:

- Verstellte Mittelstellung (Trimmer, Subtrim)
- Elektronische Begrenzung des Kanals
- Günstiger Fernsteuersender mit nichtlinearem Steuerverlauf

![](images/image\_019.png)

image20.png

Setzen Sie nach Möglichkeit alle Einstellungen für den verwendeten Kanal zurück und starten Sie den normalen Einlernvorgang erneut.

Ist dies nicht möglich, muss die Aussteuerung für positive und negative Ausschläge getrennt eingestellt werden.

Öffnen Sie den LiveDaten-Assistenten und konzentrieren Sie sich auf den unten gekennzeichneten Wert (bei Verwendung von K2 auf den Wert links daneben). Dieser Wert ändert sich beim Tastendruck und sollte möglichst nahe an den folgenden Sollwerten liegen:

| Funktion | Wert (µs) |
| --- | --- |
| Mittelstellung | 1500 |
| Ebenentaste | 1000 \* |
| Standlicht | 1070 \*\* |
| Minus-Taste | 2000 \* |
| Sattelkupplung | 1930 \*\* |

\* Je nach Fernsteuersender können Ebenentaste und Minus-Taste vertauscht sein.

\*\* Gleiches gilt für Standlicht und Sattelkupplung.

Je größer die Aussteuerung, desto weiter entfernen sich die Werte von 1500 µs bei Tastendruck. Der Ausschlag der Ebenentaste sollte möglichst weit entfernt sein, der Ausschlag für Standlicht muss sich jedoch deutlich unterscheiden. Gleiches gilt für Minus-Taste und Sattelkupplung.

Stellen Sie die Aussteuerung für beide Ausschläge getrennt ein:

- Drücken Sie **Setup+** und **S4**, um die maximale Aussteuerung für den positiven Ausschlag einzustellen.
- Überprüfen Sie die Werte für Ebenentaste und Standlicht. Sind die Werte zu ähnlich (z. B. 1930 und 1925), reduzieren Sie die Aussteuerung mit **Setup+** und **S3** und prüfen Sie erneut. Der Unterschied sollte mindestens 50 µs betragen.
- Wiederholen Sie den Vorgang für den negativen Ausschlag mit **Setup-** und den entsprechenden S-Tasten. Prüfen Sie die Werte für Minus-Taste und Sattelkupplung.

![](images/image\_020.png)

image21.png
