# Uvedení do provozu

## Instalace do vysílače Carson

Řídicí panel musí být připojen k analogovému kanálu; spínací kanály nejsou vhodné. Pokud je panel připojen, jak je znázorněno níže, pravý knipl vertikálně obsadí řídicí signály panelu a nelze jej použít k jiným účelům.

**Poznámka:** Nastavte trimr na jeden krajní úhel a nechte jej tam. Pokud bude později úhel pohybu příliš malý, lze trimr přepnout na druhý krajní úhel a panel znovu naučit.

![](images/image\_005.jpg)

image5.jpeg

Protože vysílače Carson nemají lineární průběh řízení, musí být úhly panelu nastaveny asymetricky (viz kapitola 5.11 „Naučení kanálů pro asymetrické úhly“).

Jsou nutná následující nastavení:

- Stiskněte tlačítko 7 a poté tlačítko 10.
- Stiskněte tlačítko 6 a poté tlačítko 2.

![](images/image\_006.jpg)

image6.jpeg

Tím se optimálně nastaví rozsah řízení. Poté naučte kanály odpovídajícím způsobem.

Protože vysílače Carson se výrazně liší, mohou být v některých případech nutná jiná nastavení.

## Instalace do Graupner MC20

![](images/image\_007.png)

image7.png

Lepší variantou než výše uvedené je pájení přímo na desku plošných spojů, protože zde nemohou vznikat mechanické pohyby.

![](images/image\_008.jpg)

image9.jpeg

 ![](images/image\_009.jpg)

image10.jpeg

## Obecná instalace

#### Určení rozložení pinů – teorie

Určení polohy ovladačů v dálkových vysílačích se většinou provádí pomocí běžných potenciometrů, které fungují jako dělič napětí. Mezi póly A a B je uhlíková vrstva, po které se pohybuje jezdec (tzv. „kořen“). Napětí na jezdci je část celkového napětí mezi A a B.

![](images/image\_010.png)

image11.png

**Příklad:** Pokud je mezi A a B 5 V a knipl je uprostřed, měří se mezi A a W 2,5 V a mezi W a B také 2,5 V. Při pohybu kniplu lze například naměřit 2 V mezi A a W a 3 V mezi W a B.

Je třeba zjistit, který pin je napájecí napětí a který je jezdec. **Tip:** Střední pin je často jezdec. Nespoléhejte se na barvy kabelů, ale pečlivě změřte zapojení.

#### Určení rozložení pinů – praxe

Použijte multimetr a zapněte dálkový vysílač. Vyhněte se zkratům a dotykům jiných kontaktů, abyste zabránili poškození.

Zkontrolujte, zda jsou měřicí vodiče multimetru správně připojeny (černý obvykle COM, červený obvykle V). Pokud si nejste jisti, otestujte polaritu pomocí baterie.

Proveďte následující měření a zaznamenejte hodnoty (u záporných hodnot prohoďte měřicí hroty a změřte znovu):

- Pin 1 proti pinu 2
- Pin 1 proti pinu 3
- Pin 2 proti pinu 3

Největší naměřené napětí odpovídá napájecímu napětí (typicky 3 V, 3,3 V nebo 5 V). Součet dvou menších hodnot dává největší napětí.

Hnědý kabel se připojí na záporný pól (zem), červený na kladný pól. Oranžový kabel se připojí na zbývající pin (jezdec).

Nyní stiskněte levé horní tlačítko. Servo připojené na výstup přijímače by mělo vykonat pohyb. Pokud je pohyb příliš malý, lze později nastavit rozsah řízení.

U 3pinového připojení s roztečí 2,54 mm lze použít přiložený konektor. Jinak lze kabel s konektorem připájet a panel zasunout.

## Nastavení rozsahu řízení

Protože je panel univerzální pro všechny dálkové vysílače, musí být rozsah řízení (maximální úhel pohybu) nastaven jednou. Některé vysílače interně generují pouze ±20 % na ovladači, jiné vyžadují plný rozsah.

Rozsah řízení by měl být co největší, protože jinak nebudou všechny funkce spolehlivě spínat nebo se zesílí rušení.

![](images/image\_011.png)

image12.png

Pokud panel učíte poprvé a neznáte potřebný rozsah řízení, nastavte rozsah na maximum tak, že současně stisknete tlačítko Setup a S4 (nejdříve Setup).

Spusťte Kraftwerk-ControlPanel a otevřete LiveData. Pokud kanály ještě nejsou naučené, měl by být při stisknutí tlačítka Ebenentaste viditelný pohyb přes 70 %. Tlačítko Ebenentaste generuje maximální pohyb jedním směrem, tlačítko Minustaste maximální pohyb opačným směrem.

![](images/image\_014.png)

image14.png

Zkontrolujte, zda tlačítko Ebenentaste (největší pohyb) a tlačítko Standlichttaste (druhý největší pohyb) zobrazují různé procentuální hodnoty (rozdíl alespoň 5 %). Totéž platí pro tlačítko Minustaste a Sattelkupplung.

Pokud tomu tak není, panel kanál přetěžuje a rozsah řízení musí být zmenšen.

Pro úpravu klikněte na tlačítko Naučit, potvrďte střední polohu dalším kliknutím, stiskněte tlačítko Ebenentaste, klikněte znovu, stiskněte tlačítko Minustaste, klikněte na Uložit a máte hotovo. (Text na tlačítku se při každém kliknutí mění.)

**Shrnutí:**

- Tlačítka Ebenentaste a Minustaste by měla generovat hodnoty přes 70 % (značka nehraje roli).
- Rozdíl mezi Ebenentaste a Standlicht a mezi Minustaste a Sattelkupplung by měl být alespoň 5 %.
- Volitelně: Fernlicht a Nebelscheinwerfer (nejmenší pohyby) by měly stále vykazovat viditelné pohyby přes 10 %.