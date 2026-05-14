# Datové struktury

## Základní funkce (Tag 0x01)

Základní funkce jsou kódovány v 5 bajtech:

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Výstražná světla | Levý blinkr | Pravý blinkr | Dálkové blikání | Mlhové světlo | Dálkové světlo | Potkávací světlo | Parkovací světlo |
| 1 | Zvedací nohy nahoru | Páté kolo | Motor běží | Startování | Houkačka | Zadní mlhové světlo | Brzdové světlo | Zpětné světlo |
| 2 | Pravý blinkr impuls | Výstražné světlo | Denní svícení | Levé přisvěcování do zatáčky | Pravé přisvěcování do zatáčky | Sklápění korby dolů | Sklápění korby nahoru | Zvedací nohy dolů |
| 3 | Interní/RFU | Signální klakson | Zařazení nižšího stupně | Zařazení vyššího stupně | Levé světlo do zatáčky | Pravé světlo do zatáčky | Interní/RFU | Levý blinkr impuls |
| 4 | Servo 2 | Servo 1 | Převod 2/2 | Převod 1/2 | Úroveň podložky | Sklápění rampy dolů | Sklápění rampy nahoru | Interní/RFU |

## Dodatečné funkce (Tag 0x05)

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | CH1 Paměť Poloviční Krátká Pravá | CH1 Paměť Poloviční Krátká Levá | CH1 Pravá Plná | CH1 Levá Plná | CH1 Paměť Plná Dlouhá Pravá | CH1 Paměť Plná Dlouhá Levá | CH1 Paměť Plná Krátká Pravá | CH1 Paměť Plná Krátká Levá |
| 1 | CH2 Paměť Plná Dlouhá Pravá | CH2 Paměť Plná Dlouhá Levá | CH2 Paměť Plná Krátká Pravá | CH2 Paměť Plná Krátká Levá | CH1 Pravá Poloviční | CH1 Levá Poloviční | CH1 Paměť Poloviční Dlouhá Pravá | CH1 Paměť Poloviční Dlouhá Levá |
| 2 | CH2 Pravá Poloviční | CH2 Levá Poloviční | CH2 Paměť Poloviční Dlouhá Pravá | CH2 Paměť Poloviční Dlouhá Levá | CH2 Paměť Poloviční Krátká Pravá | CH2 Paměť Poloviční Krátká Levá | CH2 Pravá Plná | CH2 Levá Plná |
| … | … | | | | | | | |
| 45 | CH31 Paměť Poloviční Krátká Pravá | CH31 Paměť Poloviční Krátká Levá | CH31 Pravá Plná | CH31 Levá Plná | CH31 Paměť Plná Dlouhá Pravá | CH31 Paměť Plná Dlouhá Levá | CH31 Paměť Plná Krátká Pravá | CH31 Paměť Plná Krátká Levá |
| 46 | CH32 Paměť Plná Dlouhá Pravá | CH32 Paměť Plná Dlouhá Levá | CH32 Paměť Plná Krátká Pravá | CH32 Paměť Plná Krátká Levá | CH31 Pravá Poloviční | CH31 Levá Poloviční | CH31 Paměť Poloviční Dlouhá Pravá | CH31 Paměť Poloviční Dlouhá Levá |
| 47 | CH32 Pravá Poloviční | CH32 Levá Poloviční | CH32 Paměť Poloviční Dlouhá Pravá | CH32 Paměť Poloviční Dlouhá Levá | CH32 Paměť Poloviční Krátká Pravá | CH32 Paměť Poloviční Krátká Levá | CH32 Pravá Plná | CH32 Levá Plná |

## Proporcionální funkce (Tag 0x41)

Hodnoty jsou 16bitová znaménková čísla v rozsahu od -500 do +500, což odpovídá zobrazení od -100 % do +100 %. Data jsou uložena v little-endian formátu.

| CH1 (Plyn) | CH2 (Řízení) | CH3 | CH4 | … | CH31 | CH32 |
| --- | --- | --- | --- | --- | --- | --- |