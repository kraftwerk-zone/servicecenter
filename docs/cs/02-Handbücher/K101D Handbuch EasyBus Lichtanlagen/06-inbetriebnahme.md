# Uvedení do provozu

Pro uvedení systémů KraftwerK EasyBus nejsou potřeba žádné speciální kroky. Přesto doporučujeme dodržet následující kontrolní seznam:

## Připojení k přijímači

![](images/image\_043.png)

image6.png

Před připojením KLM 4/16 k přijímači prosím zkontrolujte zapojení výstupů přijímače. Použijte servo a otestujte každý výstup na správnou funkci. Zaznamenejte zapojení.

**Poznámka:** Doporučuje se model zvednout, aby nedošlo k nechtěnému rozjetí.

Připojte servokabely pro řízení a plyn k odpovídajícím výstupům přijímače. Regulátor rychlosti a servo řízení se připojují k servo výstupům KLM. Kanály K1 a K2 lze volitelně použít.

**Tip:** Připojení kanálu plynu a/nebo řízení může být vynecháno, pokud jsou brzda, zpětné světlo a/nebo blinkry napájeny analogově (viz kapitola 11.5).

**Tip:** Alternativně lze regulátor rychlosti a/nebo servo řízení připojit přímo k přijímači pomocí Y-kabelu, aby se vyloučily rušení způsobená KLM.

## Připojení osvětlení

Všechny rozšiřující nebo osvětlující desky lze připojit přímo nebo přes rozbočovací desky k sběrnicovým výstupům světelného asistenta.

## Naučení kanálů

![](images/image\_043.png)

image6.png

Naučení kanálů je nezbytné pro správný provoz EasyBus systémů. Po každé změně na vysílači (např. zdvihy, směry otáčení, střední polohy) je nutné kanály znovu naučit.

Serva a motory ovládané systémem KraftwerK musí být nastaveny přes ControlPanel. Nepoužívejte menu vašeho vysílače!

1. Zapněte vysílač a model zvedněte tak, aby se poháněná kola nedotýkala země.
2. Zapněte model. Po dvojitém zablikání zelené LED posuňte plyn a řízení na pět sekund do koncové polohy, dokud červená LED nezaplavá asi jednu sekundu.
3. Vraťte kniply do střední polohy.

LED signály při učení:

- 1x bliknutí: knipl plynu – plný plyn, pak plná brzda
- 2x bliknutí: knipl řízení – plně vlevo, pak plně vpravo
- 3x bliknutí: přídavný kanál K1 – plně vlevo, pak plně vpravo
- 4x bliknutí: přídavný kanál K2 – plně nahoru, pak plně dolů

Po návratu všech kniplů do střední polohy svítí červená LED trvale, což signalizuje konec učení. Systém se automaticky restartuje a dvojité blikání zelené LED ukazuje připravenost k provozu.