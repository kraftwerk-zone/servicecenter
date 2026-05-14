# Kommandoer

Alle kommandoer starter med `0xA1` eller `0xA2`, er kodet i Tag-Length-Value-format (TLV) og slutter med en XOR-checksum.

| Startbyte | Tag (Kommando) | Længde | Værdi (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 / 0xA2 | 0x6C | 0x03 | 0x01 0x01 0x01 | 0xCF |

Checksummen beregnes som XOR over alle bytes med startværdi `0xAA`.

## SET\_FCT\_DIRECT

Med funktionen *SetFunctionDirect* kan enkelte funktioner tændes eller slukkes direkte.

| Startbyte | Tag (Kommando) | Længde | Værdi (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x6C | 0x03 | 0x01 0x03 0x01 | 0xCD |

#### Dataformat

| Byte 1 | Byte 2 | Byte 3 |
| --- | --- | --- |
| Dataobjekt (f.eks. basisfunktioner) | Bitoffset 1–40 (f.eks. parkeringslys, nærlys) | Tænd/Sluk (1 = Tænd, 0 = Sluk) |

## SET\_PARAMETER

Med funktionen *SetParameter* kan scriptparametre ændres for alle udgange, f.eks. "Sæt alle fjernlysstyrker til 80 %".

| Startbyte | Tag (Kommando) | Længde | Værdi (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x76 | 0x02 | 0x04 0x50 | 0x81 |

## SET\_DATA

Denne funktion bruges til periodisk at sætte alle værdier – både proportionale og digitale funktioner.

| Startbyte | Tag for datastruktur | Længde | Værdi (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA2 | Tag for datastruktur | 0x05 | 0x87 0x80 0x00 0x00 0x00 | 0xCF |

![](images/image_001.png)

image1.png

 ![](images/image_002.png)

image2.png