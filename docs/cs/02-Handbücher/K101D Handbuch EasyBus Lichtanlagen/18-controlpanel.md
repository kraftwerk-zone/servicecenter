# ControlPanel

## Obecné

Při spuštění ControlPanelu musí být model připraven k provozu: baterie nabitá a připojená, model a vysílač zapnuté a spárované. Serva musí být pohyblivá.

Systém je automaticky rozpoznán a všechny moduly jsou načteny a zobrazeny.

![](images/image\_044.png)

image72.png

 ![](images/image\_062.png)

image73.png

## Přehled modulů

Kliknutím na modul se dostanete do přehledu výstupů. Zde lze přiřadit názvy a nastavit rychlosti zapnutí/vypnutí. Parametry se liší podle funkce (viz kapitola 7 „Funkce“).

Změny se ukládají pomocí ikony diskety. Otazník zobrazuje nápovědu, oko zapíná výstup na modelu pro usnadnění přiřazení.

![](images/image\_046.png)

image74.png

## Dvojí přiřazení

Každý výstup může být přiřazen dvakrát. Příklad:

- První úroveň: poziční světlo & dálkové světlo
- Druhá úroveň: výstražná světla

Přepínání mezi úrovněmi lze konfigurovat.

![](images/image\_047.png)

image75.png

 až ![](images/image\_048.png)

image77.png

## Menu

| Funkce | Popis |
| --- | --- |
| Soubor | Znovu připojit systém, znovu načíst modul, zahodit dočasné změny, uložit a otevřít moduly. |
| Moduly | Zobrazit a načíst všechny moduly. |
| Nastavení systému | Konfigurace základního chování systému. |
| Informace o zařízeních | Informace o modulech, verzích softwaru, aktualizacích, továrním nastavení. |
| Analýza systému | Selftest, test komunikace, nalezení poškozených modulů. |
| Asistent učení kanálů | Pomáhá při učení kanálů. |
| Logging | Komunikace mezi ControlPanel a systémem pro hledání chyb. |
| Asistent živých dat | Zobrazuje data v reálném čase jako pohyby pák a stav přepínačů. |
| Asistent efektů Rundumlicht a KnightRider | Pomáhá s konfigurací přes více výstupů. |
| Nastavení | Pokročilé možnosti pro experty (používat opatrně). |
| Info | Informace o ControlPanelu a hlášení chyb. |

![](images/image\_049.png)

image78.png

## Panel nástrojů

![](images/image\_050.png)

image85.png

- Zobrazit hlavní obrazovku
- Znovu připojit systém
- Znovu načíst moduly
- Světla vypnuta / poziční světlo / potkávací světlo / dálkové světlo / mlhovky / zadní mlhové světlo zapnuto/vypnuto
- Živá data, informace o zařízeních, nastavení systému
- Zobrazit živý výstup, otevřít živou aktualizaci

## Živá data

Umožňuje pohled v reálném čase na polohy pák a stavy přepínačů. Kanály lze naučit a funkce zapínat/vypínat.

![](images/image\_051.png)

image86.png

|  |  |
| --- | --- |
| [[IMAGE\_078]] | Pokud jsou kanály správně naučené, musí modré body sledovat pohyby vaší páky. Pokud používáte CPPM, IBUS nebo SBUS, musí být kanály také správně přiřazeny. |
| 665544332211 [[IMAGE\_079]] | Zde jsou zobrazeny všechny kanály tak, jak jsou skutečně měřeny. Informace o učení zde nejsou zohledněny, tj. pruhy se mohou pohybovat i dolů, i když je páka posunuta nahoru.1: Změna přiřazení kanálů by měla být provedena pouze při použití CPPM, IBUS nebo SBUS.2-5: Tyto hodnoty jsou nastaveny během učení. 1000 – 2000 a 1500 střední poloha jsou standardní hodnoty. Hodnoty lze upravit a uložit.6: Posuňte doprava pro zobrazení hodnot ostatních kanálů (platí jen pro CPPM, IBUS, SBUS) |
|  | Pravá strana živých dat zobrazuje stavy přepínačů. Některé lze nastavit kliknutím.Tři skupiny funkcí Základní světelné funkce, Doplňkové funkce a Analogové lze použít jako přepínače u funkcí, např. u funkce Jednoduchý přepínač. [[IMAGE\_080]] [[IMAGE\_081]] |

![](images/image\_052.png)

image87.png

Modré body musí sledovat pohyby páky. U CPPM, IBUS nebo SBUS musí být kanály správně přiřazeny.

![](images/image\_053.png)

image88.png

Pravá strana zobrazuje stavy přepínačů, které lze také nastavit kliknutím. Tři skupiny funkcí Základní světla, Doplňkové funkce a Analogové lze použít jako přepínače.

![](images/image\_054.png)

image90.png

 ![](images/image\_055.png)

image91.png