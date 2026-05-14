# Montáž obecně – určení rozložení pinů

## Teorie

Určení polohy ovladačů u většiny dálkových ovladačů probíhá pomocí běžných potenciometrů, které fungují jako klasické děliče napětí. Princip je jednoduchý:

- Mezi póly A a B je uhlíková vrstva.
- Pohyblivý kontakt (tzv. „kořen“) se posouvá podél této vrstvy.
- Naměřené napětí na kořeni je část napětí přiloženého mezi A a B.

Příklad: Pokud je mezi A a B 5 V a páčka je uprostřed, změříte mezi A a W a mezi W a B přibližně 2,5 V. Pohybem páčky se napětí odpovídajícím způsobem mění.

![](images/image\_010.png)

image11.png

## Praxe – určení rozložení pinů

1. Zapněte dálkový ovladač a vezměte si multimetr.
2. Vyhněte se zkratům a dotykům jiných kontaktů během měření.
3. Zkontrolujte, zda jsou měřicí vodiče multimetru správně připojeny (černý na COM, červený na V).
4. Pokud si nejste jisti, ověřte polaritu pomocí baterie.
5. Změřte napětí mezi piny a zaznamenejte hodnoty:

- Pin 1 proti Pin 2
- Pin 1 proti Pin 3
- Pin 2 proti Pin 3

6. Nejvyšší naměřené napětí odpovídá napájecímu napětí (typicky 3 V, 3,3 V nebo 5 V).
7. Hnědý kabel se připojuje na záporný pól (zem), červený na kladný pól.
8. Oranžový kabel se připojuje na zbývající pin (kořen).

Nyní stiskněte levé horní tlačítko na padu. Servo připojené na odpovídající výstup přijímače by mělo reagovat. Pokud je pohyb příliš malý, lze později upravit rozsah řízení.

Pro 3pinové konektory s roztečí 2,54 mm lze použít dodaný konektorový kryt. Jinak lze kabel s konektorem připájet a pad zasunout.