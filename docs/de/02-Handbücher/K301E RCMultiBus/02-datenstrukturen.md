# Datenstrukturen

## Basisfunktionen (Tag 0x01)

Basisfunktionen sind in 5 Bytes codiert:

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Warnblinker | Blinker links | Blinker rechts | Fernlichtblitzer | Nebelscheinwerfer | Fernlicht | Abblendlicht | Standlicht |
| 1 | Stützbeine hoch | Fünfte Rad | Motor läuft | Starten | Hupen | Hecknebellicht | Bremslicht | Rückfahrlicht |
| 2 | Blinker rechts Impuls | Rundumleuchte | Tagfahrlicht | Abbiegelicht links | Abbiegelicht rechts | Mulde runter | Mulde hoch | Stützbeine runter |
| 3 | Intern/RFU | Signalhorn | Gang runter | Gang hoch | Kurvenlicht links | Kurvenlicht rechts | Intern/RFU | Blinker links Impuls |
| 4 | Servo 2 | Servo 1 | Gang 2/2 | Gang 1/2 | Pad-Level | Rampe runter | Rampe hoch | Intern/RFU |

## Zusatzfunktionen (Tag 0x05)

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | CH1 Memory Half Short Rechts | CH1 Memory Half Short Links | CH1 Rechts Voll | CH1 Links Voll | CH1 Memory Voll Lang Rechts | CH1 Memory Voll Lang Links | CH1 Memory Voll Kurz Rechts | CH1 Memory Voll Kurz Links |
| 1 | CH2 Memory Voll Lang Rechts | CH2 Memory Voll Lang Links | CH2 Memory Voll Kurz Rechts | CH2 Memory Voll Kurz Links | CH1 Rechts Halb | CH1 Links Halb | CH1 Memory Half Lang Rechts | CH1 Memory Half Lang Links |
| 2 | CH2 Rechts Halb | CH2 Links Halb | CH2 Memory Half Lang Rechts | CH2 Memory Half Lang Links | CH2 Memory Half Kurz Rechts | CH2 Memory Half Kurz Links | CH2 Rechts Voll | CH2 Links Voll |
| … | … | | | | | | | |
| 45 | CH31 Memory Half Short Rechts | CH31 Memory Half Short Links | CH31 Rechts Voll | CH31 Links Voll | CH31 Memory Voll Lang Rechts | CH31 Memory Voll Lang Links | CH31 Memory Voll Kurz Rechts | CH31 Memory Voll Kurz Links |
| 46 | CH32 Memory Voll Lang Rechts | CH32 Memory Voll Lang Links | CH32 Memory Voll Kurz Rechts | CH32 Memory Voll Kurz Links | CH31 Rechts Halb | CH31 Links Halb | CH31 Memory Half Lang Rechts | CH31 Memory Half Lang Links |
| 47 | CH32 Rechts Halb | CH32 Links Halb | CH32 Memory Half Lang Rechts | CH32 Memory Half Lang Links | CH32 Memory Half Kurz Rechts | CH32 Memory Half Kurz Links | CH32 Rechts Voll | CH32 Links Voll |

## Proportionale Funktionen (Tag 0x41)

Die Werte sind 16-Bit vorzeichenbehaftete Werte im Bereich von -500 bis +500, was einer Anzeige von -100 % bis +100 % entspricht. Die Daten liegen im Little-Endian-Format vor.

| CH1 (Gas) | CH2 (Lenkung) | CH3 | CH4 | … | CH31 | CH32 |
| --- | --- | --- | --- | --- | --- | --- |
