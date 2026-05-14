# Kommandos

Alle Kommandos beginnen mit 0xA1 oder 0xA2, sind als Tag-Length-Value (TLV) kodiert und enden mit einer XOR-Prüfsumme.

| Startbyte | Tag (Kommando) | Länge | Wert (Daten) | Prüfsumme |
| --- | --- | --- | --- | --- |
| 0xA1 / 0xA2 | 0x6C | 0x03 | 0x01 0x01 0x01 | 0xCF |

Die Prüfsumme wird als XOR über alle Bytes mit 0xAA als Startwert berechnet.

## SET\_FCT\_DIRECT – Direkte Funktionssteuerung

Mit dieser Funktion können einzelne Funktionen direkt ein- oder ausgeschaltet werden.

| Startbyte | Tag (Kommando) | Länge | Wert (Daten) | Prüfsumme |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x6C | 0x03 | 0x01 0x03 0x01 | 0xCD |

#### Datenformat

| Byte 1 | Byte 2 | Byte 3 |
| --- | --- | --- |
| Datenobjekt (z. B. Basisfunktionen) | Bit-Offset (1–40, z. B. Parklicht, Abblendlicht) | Ein/Aus (1 = Ein, 0 = Aus) |

## SET\_PARAMETER – Parameteränderung

Mit dieser Funktion können Skriptparameter für alle Ausgänge geändert werden, z. B. „Alle Fernlicht-Helligkeitswerte auf 80 % setzen“.

| Startbyte | Tag (Kommando) | Länge | Wert (Daten) | Prüfsumme |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x76 | 0x02 | 0x04 0x50 | 0x81 |

## SET\_DATA – Periodische Datenübertragung

Diese Funktion dient dazu, alle Werte – sowohl proportionale als auch digitale Funktionen – periodisch zu setzen.

| Startbyte | Tag der Datenstruktur | Länge | Wert (Daten) | Prüfsumme |
| --- | --- | --- | --- | --- |
| 0xA2 | entsprechender Tag | 0x05 | 0x87 0x80 0x00 0x00 0x00 | 0xCF |
