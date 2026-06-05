# Datové struktury

## Základní funkce (Tag 0x01)

Základní funkce jsou kódovány v 5 bajtech:

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Výstražná světla | Levý blinkr | Pravý blinkr | Dálkové blikání | Mlhové světlo | Dálkové světlo | Potkávací světlo | Parkovací světlo |
| 1 | Zvedací nohy nahoru | Páté kolo | Motor běží | Startér | Klakson | Zadní mlhové světlo | Brzda | Zpátečka |
| 2 | Pravý blinkr impuls | Výstražné světlo | Denní svícení | Levý blinkr | Snižování | Zvedání | Zvedací nohy dolů |  |
| 3 | Interní/RFU | Signální klakson | Zařazení nižšího stupně | Zařazení vyššího stupně | Levé přisvěcování do zatáčky | Pravé přisvěcování do zatáčky | Interní/RFU | Levý blinkr impuls |
| 4 | Servo 2 | Servo 1 | Stupeň 2/2 | Stupeň 1/2 | Úroveň podložky | Sklápění rampy dolů | Sklápění rampy nahoru | Interní/RFU |

## Dodatečné funkce (Tag 0x05)

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | CH1 Paměť poloviční krátký pravý | CH1 Paměť poloviční krátký levý | CH1 Pravý plný | CH1 Levý plný | CH1 Paměť plný dlouhý pravý | CH1 Paměť plný dlouhý levý | CH1 Paměť plný krátký pravý | CH1 Paměť plný krátký levý |
| 1 | CH2 Paměť plný dlouhý pravý | CH2 Paměť plný dlouhý levý | CH2 Paměť plný krátký pravý | CH2 Paměť plný krátký levý | CH1 Pravý poloviční | CH1 Levý poloviční | CH1 Paměť poloviční dlouhý pravý | CH1 Paměť poloviční dlouhý levý |
| 2 | CH2 Pravý poloviční | CH2 Levý poloviční | CH2 Paměť poloviční dlouhý pravý | CH2 Paměť poloviční dlouhý levý | CH2 Paměť poloviční krátký pravý | CH2 Paměť poloviční krátký levý | CH2 Pravý plný | CH2 Levý plný |
| … |  |  |  |  |  |  |  |  |
| 45 | CH31 Paměť poloviční krátký pravý | CH31 Paměť poloviční krátký levý | CH31 Pravý plný | CH31 Levý plný | CH31 Paměť plný dlouhý pravý | CH31 Paměť plný dlouhý levý | CH31 Paměť plný krátký pravý | CH31 Paměť plný krátký levý |
| 46 | CH32 Paměť plný dlouhý pravý | CH32 Paměť plný dlouhý levý | CH32 Paměť plný krátký pravý | CH32 Paměť plný krátký levý | CH31 Pravý poloviční | CH31 Levý poloviční | CH31 Paměť poloviční dlouhý pravý | CH31 Paměť poloviční dlouhý levý |
| 47 | CH32 Pravý poloviční | CH32 Levý poloviční | CH32 Paměť poloviční dlouhý pravý | CH32 Paměť poloviční dlouhý levý | CH32 Paměť poloviční krátký pravý | CH32 Paměť poloviční krátký levý | CH32 Pravý plný | CH32 Levý plný |

## Proporcionální funkce (Tag 0x41)

Hodnoty jsou 16bitové podepsané hodnoty od -500 do +500, což odpovídá zobrazení od -100 % do +100 %. Data jsou uložena v little-endian formátu.

| CH1 (Plyn) | CH2 (Řízení) | CH3 | CH4 | … | CH31 | CH32 |
| --- | --- | --- | --- | --- | --- | --- |