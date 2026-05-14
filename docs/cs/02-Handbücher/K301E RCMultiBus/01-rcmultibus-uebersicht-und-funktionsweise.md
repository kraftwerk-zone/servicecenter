# RCMultiBus – Přehled a fungování

**Verze:** 1.05  
**Datum:** 11.01.2021  
**Autor:** Wolfgang Haring e.U.  
**Firmenbuchnummer:** FN 312421 v (Landesgericht Wr. Neustadt)  
**Adresa:** Kammanngasse 7-9A/8, A-2700 Wiener Neustadt

![](images/image\_001.png)

image1.png

 ![](images/image\_002.png)

image2.png

## Obecné informace

**RCMultiBus** je nadřazený protokol pro všechny 3drátové datové sběrnice používané v oblasti RC. Slave zařízení podporující RCMultiBus musí být schopné interpretovat všechny typy sběrnic včetně protokolu, přenosové rychlosti a polarity. Master zařízení naopak musí být schopné pouze generovat jeden typ sběrnice.

Aktuálně podporované typy sběrnic jsou:

- IBUS
- SBUS
- EX-Bus
- CPPM

Podle typu sběrnice lze přijímat proporcionální a/nebo digitální informace. Každý proporcionální kanál je vždy převeden na digitální spínací funkce (trvalé a v paměti).

## Typy sběrnic a hodnoty kanálů

Každá hodnota kanálu je uložena a může být individuálně namapována na servo- nebo motorové výstupy. Navíc je sledován pohyb každého kanálu, ze kterého je generováno bitové pole. Toto bitové pole má tři dimenze:

- **Směr:** Top (nahoru) / Bottom (dolů)
- **Rozsah pohybu:** Full (plný) / Half (poloviční)
- **Stav paměti:** Memory (v paměti) / Permanent (trvalý)

| Kanál | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH1 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| CH2 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| … |  |  |  |  |  |  |  |
| CHx | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |

#### Příklady příznaků bitového pole

- **Příklad 1:** Kanál 4 je posunut o +30 % → příznak *CH4 Permanent/Top/Half* je nastaven.
- **Příklad 2:** Kanál 4 je během půl sekundy vrácen zpět → příznak *CH4 Permanent/Top/Half* je vymazán, příznak *CH4 Memory/Top/Half* je nastaven.
- **Příklad 3:** Kanál 1 je posunut o -100 % → příznak *CH1 Permanent/Bottom/Full* je nastaven.
- **Příklad 4:** Kanál 1 je po jedné sekundě vrácen zpět → příznak *CH1 Permanent/Bottom/Full* je vymazán, příznak *CH1 Memory/Bottom/Full* je nastaven.

## Multiswitch systémy (Futaba, Graupner)

Multiswitch systémy jsou pomalejší, protože signály jsou přenášeny multiplexně po sobě a používají převážně tlačítka nebo přepínače (žádné páčky). Proto zde nelze použít stavy *“short”* a *“half”*.

| Kanál | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH1 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| CH2 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| … |  |  |  |  |  |  |  |
| CHx | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |

## SUMD a SUMDV3

Použití SUMD nebo SUMDV3 závisí na verzi vysílače/přijímače a firmware přijímače.

- **SUMD:** Funguje analogicky jako IBUS, SBUS, EX-Bus a CPPM (viz výše).
- **SUMDV3:** Přenáší pole tzv. „digitálních spínačů“, které přijímají a ukládají moduly RCMultiBus. Zde lze použít jak kanálově závislé spínače jako u IBUS, SBUS, EX-Bus, CPPM, tak i digitální spínače vlastní SUMDV3.

## PWM standard

Funguje podobně jako IBUS, SBUS, EX-Bus a CPPM, ale pouze s jedním kanálem (CH1).

## Nastavení UART

- Standard: 38 400 baudů, 8 bytů, LSB první, žádná parita, 1 stop bit, timeout 100 µs
- V budoucnu: 100 000 baudů (v plánu)

## Centrální časově řízené funkce

Centrální časově řízené funkce jako blinkr jsou řízeny dvěma digitálními funkcemi:

- Informace, zda je funkce obecně zapnuta nebo vypnuta
- Impuls, který lampu zapíná a vypíná

Pro řízení blinkru stačí nastavit impuls. Obecná informace o zapnutí/vypnutí může být použita pro mixéry nebo jiné přepínače (např. přepnutí na druhou konfiguraci, pokud je blinkr aktivní).