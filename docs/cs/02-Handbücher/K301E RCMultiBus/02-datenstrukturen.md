# Datové struktury

## Základní funkce (Tag 0x01)

Základní funkce jsou kódovány v 5 bajtech:

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Výstražná světla | Levý blinkr | Pravý blinkr | Dálkové blikání | Mlhové světlo | Dálkové světlo | Potkávací světlo | Parkovací světlo |
| 1 | Zvedací nohy nahoru | Páté kolo | Motor běží | Startování | Houkačka | Zadní mlhové světlo | Brzdové světlo | Zpětné světlo |
| 2 | Impuls pravého blinkru | Maják | Denní svícení | Levé přídavné světlo | Pravé přídavné světlo | Sklápění korby dolů | Sklápění korby nahoru | Zvedací nohy dolů |
| 3 | Interní/RFU | Signální klakson | Zařazení nižšího stupně | Zařazení vyššího stupně | Levé zatáčkové světlo | Pravé zatáčkové světlo | Interní/RFU | Impuls levého blinkru |
| 4 | Servo 2 | Servo 1 | Stupeň 2/2 | Stupeň 1/2 | Úroveň podložky | Sklápění rampy dolů | Sklápění rampy nahoru | Interní/RFU |

## Přídavné funkce (Tag 0x05)

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | CH1 Paměť Poloviční Krátký Pravý | CH1 Paměť Poloviční Krátký Levý | CH1 Pravý Plný | CH1 Levý Plný | CH1 Paměť Plný Dlouhý Pravý | CH1 Paměť Plný Dlouhý Levý | CH1 Paměť Plný Krátký Pravý | CH1 Paměť Plný Krátký Levý |
| 1 | CH2 Paměť Plný Dlouhý Pravý | CH2 Paměť Plný Dlouhý Levý | CH2 Paměť Plný Krátký Pravý | CH2 Paměť Plný Krátký Levý | CH1 Pravý Poloviční | CH1 Levý Poloviční | CH1 Paměť Poloviční Dlouhý Pravý | CH1 Paměť Poloviční Dlouhý Levý |
| 2 | CH2 Pravý Poloviční | CH2 Levý Poloviční | CH2 Paměť Poloviční Dlouhý Pravý | CH2 Paměť Poloviční Dlouhý Levý | CH2 Paměť Poloviční Krátký Pravý | CH2 Paměť Poloviční Krátký Levý | CH2 Pravý Plný | CH2 Levý Plný |
| … | … | | | | | | | |
| 45 | CH31 Paměť Poloviční Krátký Pravý | CH31 Paměť Poloviční Krátký Levý | CH31 Pravý Plný | CH31 Levý Plný | CH31 Paměť Plný Dlouhý Pravý | CH31 Paměť Plný Dlouhý Levý | CH31 Paměť Plný Krátký Pravý | CH31 Paměť Plný Krátký Levý |
| 46 | CH32 Paměť Plný Dlouhý Pravý | CH32 Paměť Plný Dlouhý Levý | CH32 Paměť Plný Krátký Pravý | CH32 Paměť Plný Krátký Levý | CH31 Pravý Poloviční | CH31 Levý Poloviční | CH31 Paměť Poloviční Dlouhý Pravý | CH31 Paměť Poloviční Dlouhý Levý |
| 47 | CH32 Pravý Poloviční | CH32 Levý Poloviční | CH32 Paměť Poloviční Dlouhý Pravý | CH32 Paměť Poloviční Dlouhý Levý | CH32 Paměť Poloviční Krátký Pravý | CH32 Paměť Poloviční Krátký Levý | CH32 Pravý Plný | CH32 Levý Plný |

## Proporcionální funkce (Tag 0x41)

Hodnoty jsou 16bitová znaménková čísla v rozsahu od -500 do +500, což odpovídá zobrazení od -100 % do +100 %. Data jsou uložena v little-endian formátu.

| CH1 (Plyn) | CH2 (Řízení) | CH3 | CH4 | … | CH31 | CH32 |
| --- | --- | --- | --- | --- | --- | --- |