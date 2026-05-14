# Installation generelt – Bestemmelse af pin-konfiguration

## Teori

Positionsbestemmelsen af styresenderne i de fleste fjernbetjeninger sker via almindelige potentiometre, som fungerer som klassiske spændingsdelere. Princippet er enkelt:

- Mellem polerne A og B findes et kulstoflag.
- En bevægelig kontakt (den såkaldte "wiper") bevæger sig langs dette lag.
- Den målte spænding ved wiperen er en del af den spænding, der påføres mellem A og B.

Eksempel: Hvis der er 5 V mellem A og B, og styrestokken står i midten, måler du ca. 2,5 V mellem A og W samt mellem W og B. Når styrestokken bevæges, ændres spændingerne tilsvarende.

![](images/image\_010.png)

image11.png

## Praksis – Bestemmelse af pin-konfiguration

1. Tænd for fjernbetjeningen og tag et multimeter frem.
2. Undgå kortslutninger og berøring af andre kontakter under målingen.
3. Kontroller, at multimeterets måleledninger er korrekt tilsluttet (sort til COM, rød til V).
4. Hvis du er usikker, kan du kontrollere polariteten med et batteri.
5. Mål spændingerne mellem pinnene og noter værdierne:

- Pin 1 mod Pin 2
- Pin 1 mod Pin 3
- Pin 2 mod Pin 3

6. Den største målte spænding svarer til forsyningsspændingen (typisk 3 V, 3,3 V eller 5 V).
7. Den brune ledning forbindes til minuspolen (masse), den røde til pluspolen.
8. Den orange ledning forbindes til den resterende pin (wiperen).

Tryk nu på den øverste venstre knap på pad’en. Et servo tilsluttet den tilsvarende modtagerudgang bør bevæge sig. Hvis bevægelsen er for lille, kan udslaget justeres senere.

Til 3-polet tilslutning med 2,54 mm rastermål kan det medfølgende stikhus anvendes. Ellers kan hunstikkablet loddes, og pad’en kan sættes i.