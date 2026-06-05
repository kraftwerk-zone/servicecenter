# Zvukový modul

Zvukové moduly lze provozovat přímo na přijímači. Pro ovládání přes EasyBus musí být připojeny ke dvěma servo výstupům (přímo na KLM 4/16 nebo na KSB 2/4).

## Kompatibilní se Servonaut SMT

Jeden kanál pro informaci o plynu, druhý pro start/stop a houkání (ovládáno v opačných směrech).

![](images/image\_019.png)

image30.png

## Programovatelné zvukové moduly (např. BEIER USM-RC)

Založené na režimu Servonaut, ale rozšiřují možnost ovládat druhý klakson.

![](images/image\_020.png)

image31.png

Ve zvukovém modulu je třeba provést následující nastavení:

![](images/image\_021.png)

image32.png

## Ovládání zvukového modulu

S ovládacím panelem Světlo & Zvuk nejsou potřeba další nastavení. Tlačítko klaksonu ovládá klakson, tlačítko úrovně spouští nebo zastavuje motor.

Doplňkové kanály K1 a K2 (příp. až K10 při použití IBUS, SBUS, SUMD atd.) lze v systémových nastaveních uživatelsky přiřadit.

![](images/image\_022.png)

image33.png

Je také možná kombinace ovládacího panelu a uživatelsky definovaného přiřazení.

![](images/image\_023.png)

image34.png

## Důležitá nastavení

- **Motor běží okamžitě:** Podle toho, zda zvukový modul motor spouští okamžitě, musí být systémové nastavení „Motor běží okamžitě [aktivní]“ zapnuto nebo vypnuto.
- **Pozor:** Pohonný motor je v každém případě aktivní!
- **Světla blikají:** Každá světelná deska a rozšíření spínače (KLB) má systémová nastavení pro „Efekt startu“ (blikání při startu) a „Redukce světla při zastavení motoru“ (snížení při zastavení motoru). Používejte druhé pouze, pokud nejsou ovládány komponenty s integrovanou elektronikou.
- Doba blikání může být pomocí „Doba startu motoru“ přizpůsobena době startu zvukového modulu.