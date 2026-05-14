# Kanaldaten und Bewegungsüberwachung

Jeder Kanalwert wird gespeichert und kann für jeden Servo- oder Motor-Ausgang individuell zugeordnet werden. Zusätzlich wird die Bewegung jedes Kanals überwacht, woraus ein Bitfeld generiert wird. Dieses Bitfeld hat drei Dimensionen:

- **Richtung:** oben (top) / unten (bottom)
- **Bewegungsintensität:** voll (full) / halb (half)
- **Status:** permanent / im Speicher (memory)

| CH | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH1 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| CH2 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| … |  |  |  |  |  |  |  |
| CHx | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |

## Beispiele zur Bewegungsüberwachung

- **Beispiel 1:** Kanal 4 wird auf +30% bewegt → Flag *CH4 Permanent/Top/Half* wird gesetzt.
- **Beispiel 2:** Kanal 4 wird innerhalb von 0,5 Sekunden zurückbewegt → Flag *CH4 Permanent/Top/Half* wird gelöscht, Flag *CH4 Memory/Top/Half* wird gesetzt.
- **Beispiel 3:** Kanal 1 wird auf -100% bewegt → Flag *CH1 Permanent/Bottom/Full* wird gesetzt.
- **Beispiel 4:** Kanal 1 wird nach einer Sekunde zurückbewegt → Flag *CH1 Permanent/Bottom/Full* wird gelöscht, Flag *CH1 Memory/Bottom/Full* wird gesetzt.
