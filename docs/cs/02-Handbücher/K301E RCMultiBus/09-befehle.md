# Příkazy

Všechny příkazy začínají `0xA1` nebo `0xA2`, jsou kódovány ve formátu Tag-Length-Value (TLV) a končí XOR kontrolním součtem.

| Startovní bajt | Tag (příkaz) | Délka | Hodnota (data) | Kontrolní součet |
| --- | --- | --- | --- | --- |
| 0xA1 / 0xA2 | 0x6C | 0x03 | 0x01 0x01 0x01 | 0xCF |

Kontrolní součet se počítá jako XOR přes všechny bajty s počáteční hodnotou `0xAA`.

## SET\_FCT\_DIRECT

Funkcí *SetFunctionDirect* lze jednotlivé funkce přímo zapínat nebo vypínat.

| Startovní bajt | Tag (příkaz) | Délka | Hodnota (data) | Kontrolní součet |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x6C | 0x03 | 0x01 0x03 0x01 | 0xCD |

#### Formát dat

| Bajt 1 | Bajt 2 | Bajt 3 |
| --- | --- | --- |
| Datový objekt (např. základní funkce) | Bitový offset 1–40 (např. parkovací světlo, potkávací světlo) | Zapnuto/Vypnuto (1 = zapnuto, 0 = vypnuto) |

## SET\_PARAMETER

Funkcí *SetParameter* lze měnit parametry skriptu pro všechny výstupy, např. „nastavit všechny hodnoty jasu dálkových světel na 80 %“.

| Startovní bajt | Tag (příkaz) | Délka | Hodnota (data) | Kontrolní součet |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x76 | 0x02 | 0x04 0x50 | 0x81 |

## SET\_DATA

Tato funkce slouží k periodickému nastavování všech hodnot – jak proporcionálních, tak digitálních funkcí.

| Startovní bajt | Tag datové struktury | Délka | Hodnota (data) | Kontrolní součet |
| --- | --- | --- | --- | --- |
| 0xA2 | Tag datové struktury | 0x05 | 0x87 0x80 0x00 0x00 0x00 | 0xCF |

![](images/image\_001.png)

image1.png

 ![](images/image\_002.png)

image2.png