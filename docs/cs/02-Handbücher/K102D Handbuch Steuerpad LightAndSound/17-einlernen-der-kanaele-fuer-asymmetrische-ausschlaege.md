# Naučení kanálů pro asymetrické výchylky

Tato část je relevantní pouze v případě, že všechny předchozí kroky byly správně provedeny a dálkové světlo nebo mlhové světlomety vykazují příliš malé nebo žádné výchylky.

Možné příčiny:

- Posunutá střední poloha (trimer, subtrim)
- Elektronické omezení kanálu
- Levný vysílač s nelineárním průběhem řízení

![](images/image\_019.png)

image20.png

Pokud je to možné, nastavte všechny parametry pro použitý kanál zpět na výchozí a spusťte normální proces učení znovu.

Pokud to není možné, musí být řízení pro kladné a záporné výchylky nastaveno odděleně.

Otevřete asistenta živých dat a zaměřte se na níže označenou hodnotu (při použití K2 na hodnotu vlevo od ní). Tato hodnota se mění při stisku tlačítka a měla by být co nejblíže následujícím cílovým hodnotám:

| Funkce | Hodnota (µs) |
| --- | --- |
| Střední poloha | 1500 |
| Tlačítko roviny | 1000 \* |
| Stálé světlo | 1070 \*\* |
| Tlačítko mínus | 2000 \* |
| Sedlová spojka | 1930 \*\* |

\* V závislosti na vysílači mohou být tlačítko roviny a tlačítko mínus prohozeny.

\*\* Totéž platí pro stálé světlo a sedlovou spojku.

Čím větší je řízení, tím více se hodnoty při stisku tlačítka vzdaluji od 1500 µs. Výchylka tlačítka roviny by měla být co největší, výchylka stálého světla se však musí výrazně lišit. Totéž platí pro tlačítko mínus a sedlovou spojku.

Nastavte řízení pro obě výchylky odděleně:

- Stiskněte **Setup+** a **S4** pro nastavení maximálního řízení pro kladnou výchylku.
- Zkontrolujte hodnoty tlačítka roviny a stálého světla. Pokud jsou hodnoty příliš podobné (např. 1930 a 1925), snižte řízení pomocí **Setup+** a **S3** a zkontrolujte znovu. Rozdíl by měl být alespoň 50 µs.
- Opakujte postup pro zápornou výchylku pomocí **Setup-** a příslušných tlačítek S. Zkontrolujte hodnoty tlačítka mínus a sedlové spojky.

![](images/image\_020.png)

image21.png