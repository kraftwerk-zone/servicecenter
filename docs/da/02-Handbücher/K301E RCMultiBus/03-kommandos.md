# Kommandoer

Alle kommandoer starter med 0xA1 eller 0xA2, er kodet som Tag-Length-Value (TLV) og slutter med en XOR-checksum.

| Startbyte | Tag (Kommando) | Længde | Værdi (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 / 0xA2 | 0x6C | 0x03 | 0x01 0x01 0x01 | 0xCF |

Checksummen beregnes som XOR over alle bytes med 0xAA som startværdi.

## SET\_FCT\_DIRECT – Direkte funktionsstyring

Med denne funktion kan enkelte funktioner tændes eller slukkes direkte.

| Startbyte | Tag (Kommando) | Længde | Værdi (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x6C | 0x03 | 0x01 0x03 0x01 | 0xCD |

#### Dataformat

| Byte 1 | Byte 2 | Byte 3 |
| --- | --- | --- |
| Dataobjekt (f.eks. basisfunktioner) | Bit-offset (1–40, f.eks. parkeringslys, nærlys) | Tænd/Sluk (1 = Tænd, 0 = Sluk) |

## SET\_PARAMETER – Parameterændring

Med denne funktion kan scriptparametre ændres for alle udgange, f.eks. "Sæt alle fjernlysstyrker til 80 %".

| Startbyte | Tag (Kommando) | Længde | Værdi (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x76 | 0x02 | 0x04 0x50 | 0x81 |

## SET\_DATA – Periodisk dataoverførsel

Denne funktion bruges til at sætte alle værdier – både proportionale og digitale funktioner – periodisk.

| Startbyte | Tag for datastruktur | Længde | Værdi (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA2 | tilsvarende tag | 0x05 | 0x87 0x80 0x00 0x00 0x00 | 0xCF |