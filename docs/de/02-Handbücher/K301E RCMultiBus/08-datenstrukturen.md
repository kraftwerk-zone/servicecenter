# Datenstrukturen

## Basisfunktionen (Tag 0x01)

Die Basisfunktionen sind in 5 Bytes codiert:

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Warnblinker | Blinker links | Blinker rechts | Fernlichtblitzer | Nebelscheinwerfer | Fernlicht | Abblendlicht | Standlicht |
| 1 | Stützbeine hoch | Fünfte Rad | Motor läuft | Anlasser | Hupe | Hecknebellicht | Bremse | Rückwärtsgang |
| 2 | Blinker rechts Impuls | Rundumleuchte | Tagfahrlicht | Blinker links | Senken | Heben | Stützbeine runter |  |
| 3 | Intern/RFU | Signalhupe | Gang runter | Gang rauf | Kurvenlicht links | Kurvenlicht rechts | Intern/RFU | Blinker links Impuls |
| 4 | Servo 2 | Servo 1 | Gang 2/2 | Gang 1/2 | Pad Level | Rampe runter | Rampe hoch | Intern/RFU |

## Zusatzfunktionen (Tag 0x05)

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | CH1 Memory Half Short Rechts | CH1 Memory Half Short Links | CH1 Rechts Voll | CH1 Links Voll | CH1 Memory Voll Lang Rechts | CH1 Memory Voll Lang Links | CH1 Memory Voll Kurz Rechts | CH1 Memory Voll Kurz Links |
| 1 | CH2 Memory Voll Lang Rechts | CH2 Memory Voll Lang Links | CH2 Memory Voll Kurz Rechts | CH2 Memory Voll Kurz Links | CH1 Rechts Halb | CH1 Links Halb | CH1 Memory Halb Lang Rechts | CH1 Memory Halb Lang Links |
| 2 | CH2 Rechts Halb | CH2 Links Halb | CH2 Memory Halb Lang Rechts | CH2 Memory Halb Lang Links | CH2 Memory Halb Kurz Rechts | CH2 Memory Halb Kurz Links | CH2 Rechts Voll | CH2 Links Voll |
| … |  |  |  |  |  |  |  |  |
| 45 | CH31 Memory Halb Kurz Rechts | CH31 Memory Halb Kurz Links | CH31 Rechts Voll | CH31 Links Voll | CH31 Memory Voll Lang Rechts | CH31 Memory Voll Lang Links | CH31 Memory Voll Kurz Rechts | CH31 Memory Voll Kurz Links |
| 46 | CH32 Memory Voll Lang Rechts | CH32 Memory Voll Lang Links | CH32 Memory Voll Kurz Rechts | CH32 Memory Voll Kurz Links | CH31 Rechts Halb | CH31 Links Halb | CH31 Memory Halb Lang Rechts | CH31 Memory Halb Lang Links |
| 47 | CH32 Rechts Halb | CH32 Links Halb | CH32 Memory Halb Lang Rechts | CH32 Memory Halb Lang Links | CH32 Memory Halb Kurz Rechts | CH32 Memory Halb Kurz Links | CH32 Rechts Voll | CH32 Links Voll |

## Proportionale Funktionen (Tag 0x41)

Die Werte sind 16-Bit signed Werte von -500 bis +500, was einer Anzeige von -100 % bis +100 % entspricht. Die Daten sind im Little-Endian-Format gespeichert.

| CH1 (Gas) | CH2 (Lenkung) | CH3 | CH4 | … | CH31 | CH32 |
| --- | --- | --- | --- | --- | --- | --- |
