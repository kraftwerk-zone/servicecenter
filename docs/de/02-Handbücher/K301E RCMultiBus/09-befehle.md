# Befehle

Alle Befehle beginnen mit `0xA1` oder `0xA2`, sind im Tag-Length-Value-Format (TLV) kodiert und enden mit einer XOR-Prüfsumme.

| Startbyte | Tag (Befehl) | Länge | Wert (Daten) | Prüfsumme |
| --- | --- | --- | --- | --- |
| 0xA1 / 0xA2 | 0x6C | 0x03 | 0x01 0x01 0x01 | 0xCF |

Die Prüfsumme wird als XOR über alle Bytes mit Startwert `0xAA` berechnet.

## SET\_FCT\_DIRECT

Mit der Funktion *SetFunctionDirect* können einzelne Funktionen direkt ein- oder ausgeschaltet werden.

| Startbyte | Tag (Befehl) | Länge | Wert (Daten) | Prüfsumme |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x6C | 0x03 | 0x01 0x03 0x01 | 0xCD |

#### Datenformat

| Byte 1 | Byte 2 | Byte 3 |
| --- | --- | --- |
| Datenobjekt (z. B. Basisfunktionen) | Bitoffset 1–40 (z. B. Parklicht, Abblendlicht) | Ein/Aus (1 = Ein, 0 = Aus) |

## SET\_PARAMETER

Mit der Funktion *SetParameter* können Skriptparameter für alle Ausgänge geändert werden, z. B. „Alle Fernlicht-Helligkeitswerte auf 80 % setzen“.

| Startbyte | Tag (Befehl) | Länge | Wert (Daten) | Prüfsumme |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x76 | 0x02 | 0x04 0x50 | 0x81 |

## SET\_DATA

Diese Funktion dient dazu, periodisch alle Werte – sowohl proportionale als auch digitale Funktionen – zu setzen.

| Startbyte | Tag der Datenstruktur | Länge | Wert (Daten) | Prüfsumme |
| --- | --- | --- | --- | --- |
| 0xA2 | Tag der Datenstruktur | 0x05 | 0x87 0x80 0x00 0x00 0x00 | 0xCF |

![](images/image\_001.png)

image1.png

 ![](images/image\_002.png)

image2.png
