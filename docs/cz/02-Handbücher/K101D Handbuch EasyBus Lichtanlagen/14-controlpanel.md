# ControlPanel

## Obecné

Při spuštění ControlPanelu musí být model připraven k provozu: baterie nabitá a připojená, model a vysílač zapnuté a spárované, serva pohyblivá.

Systém je automaticky rozpoznán a všechny moduly jsou zobrazeny.

![](images/image\_023.png)

image72.png

 ![](images/image\_040.png)

image73.png

## Přehled modulů

Kliknutím na modul přejdete na přehled výstupů. Zde můžete přiřadit jména, nastavit rychlosti zapnutí a vypnutí a podle funkce konfigurovat další parametry.

Změny uložíte ikonou diskety. Nápovědy jsou dostupné přes otazník. Pomocí ikony oka lze výstupy na modelu přímo aktivovat, aby se usnadnilo přiřazení.

![](images/image\_025.png)

image74.png

## Dvojí přiřazení

Každý výstup může mít dvojí přiřazení. Příklad:

- První úroveň: poziční světlo & dálkové světlo
- Druhá úroveň: výstražná světla

Přepínání mezi úrovněmi je konfigurovatelné.

![](images/image\_026.png)

image75.png

 až ![](images/image\_027.png)

image77.png

## Menu

|  |  |
| --- | --- |
| **Soubor** | Znovu připojit systém, znovu načíst moduly, zahodit dočasné změny, uložit a otevřít moduly. |
| **Moduly** | Zobrazit a načíst všechny moduly. |
| **Nastavení systému** | Základní konfigurace systému. |
| **Informace o zařízeních** | Informace o modulech, aktualizace, tovární nastavení. |
| **Analýza systému** | Selftest, test komunikace, hledání poškozených modulů. |
| **Průvodce učením kanálů** | Podpora při učení kanálů. |
| **Logování** | Protokol komunikace pro hledání chyb. |
| **Průvodce živými daty** | Zobrazení polohy pák a stavů přepínačů v reálném čase. |
| **Průvodci efekty** | Konfigurace efektů majáků a KnightRider. |
| **Nastavení** | Rozšířené možnosti, režim experta (varování před možným poškozením). |
| **Info** | Informace o ControlPanelu a hlášení chyb. |

## Panel nástrojů

![](images/image\_028.png)

image85.png

- Zobrazit hlavní obrazovku
- Znovu připojit systém
- Znovu načíst moduly
- Světla vypnuta / poziční světlo / potkávací světlo / dálkové světlo / mlhovky / zadní mlhovka zapnuto/vypnuto
- Zobrazit živá data
- Informace o zařízeních
- Nastavení systému
- Zobrazit živý výstup
- Otevřít živou aktualizaci

## Živá data

Zobrazení živých dat ukazuje polohy pák a stavy přepínačů v reálném čase. Kanály lze naučit a funkce zapínat nebo vypínat.

![](images/image\_029.png)

image86.png

|  |  |
| --- | --- |
| [[IMAGE\_078]] | Pokud jsou kanály správně naučené, musí modré body sledovat pohyby vaší páky. Pokud používáte CPPM, IBUS nebo SBUS, musí být kanály také správně přiřazeny. |
| 665544332211 [[IMAGE\_079]] | Zde jsou zobrazeny všechny kanály tak, jak jsou skutečně měřeny. Informace o učení nejsou zohledněny, tj. pruhy se mohou pohybovat i dolů, i když páka jde nahoru.1: Změna přiřazení kanálu by měla být provedena pouze při použití CPPM, IBUS nebo SBUS.2-5: Tyto hodnoty jsou nastaveny během učení. 1000 – 2000 a 1500 střední poloha jsou standardní hodnoty. Hodnoty lze upravit a uložit.6: Posuňte doprava pro zobrazení hodnot dalších kanálů (platí jen pro CPPM, IBUS, SBUS) |
|  | Pravá strana živých dat zobrazuje stavy přepínačů. Některé lze nastavit kliknutím.Tři skupiny funkcí základní světelné funkce, doplňkové funkce a analogové lze použít jako přepínače u funkcí, například u funkce jednoduchý přepínač. [[IMAGE\_080]] [[IMAGE\_081]] |

![](images/image\_030.png)

image87.png

Při správném učení modré body sledují pohyby páky. Pro CPPM, I-BUS nebo S-BUS musí být přiřazení kanálů správné.

![](images/image\_031.png)

image88.png

Pravá strana zobrazuje stavy přepínačů, které lze částečně měnit kliknutím.

![](images/image\_032.png)

image90.png

 ![](images/image\_033.png)

image91.png

## Aktualizace

Po připojení ControlPanel zobrazí dostupné aktualizace pro sběrnicové moduly.

![](images/image\_043.png)

image6.png

Tipy pro bezpečnou aktualizaci:

- Aktualizujte vždy jen jeden modul najednou.
- Vyhněte se přerušení napájení.
- Odpojte serva a motory během aktualizace.
- Při problémech restartujte model i ControlPanel.

![](images/image\_035.png)

image92.png

 ![](images/image\_043.png)

image6.png

Aktualizace mohou resetovat tovární nastavení. ControlPanel automaticky zálohuje všechna nastavení na pevný disk.

![](images/image\_037.png)

image93.png

 ![](images/image\_038.png)

image94.png

 ![](images/image\_039.png)

image95.png

Po aktualizacích jsou zobrazeny všechny moduly. KLM 4/16 se skládá z hlavního modulu se čtyřmi servo výstupy a integrovaným rozšířením přepínačů se 16 spínacími výstupy.

![](images/image\_040.png)

image73.png

## Informace o zařízeních

Zobrazení základních informací o modulech. „Zobrazit zařízení“ zapne první tři výstupy, užitečné při více rozšířeních bez pojmenování.

Moduly lze restartovat, obnovit tovární nastavení nebo aktualizovat.

![](images/image\_041.png)

image96.png

## Analýza systému

Pomáhá při hledání chyb čtením informací, hledáním poškozených modulů a testy komunikace.

![](images/image\_042.png)

image97.png

 ![](images/image\_043.png)

image6.png

## Učení kanálů

Průvodce pomáhá při učení kanálů. Nejprve nastavte správné přiřazení pro K1 a K2, zejména při použití ovládacích panelů.

![](images/image\_044.png)

image98.png