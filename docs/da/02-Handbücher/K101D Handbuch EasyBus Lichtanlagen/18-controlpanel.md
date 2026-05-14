# ControlPanel

## Generelt

Ved opstart af ControlPanel skal modellen være klar til drift: Batteriet opladet og tilsluttet, model og fjernbetjening tændt og bundet. Servomotorer skal kunne bevæge sig.

Systemet registreres automatisk, og alle moduler indlæses og vises.

![](images/image\_044.png)

image72.png

 ![](images/image\_062.png)

image73.png

## Moduloversigt

Ved klik på et modul kommer man til udgangsoversigten. Her kan navne tildeles, og tænd-/sluk-hastigheder indstilles. Parametrene varierer afhængigt af funktionen (se kapitel 7 "Funktioner").

Ændringer gemmes med disketteikonet. Spørgsmålstegnet viser hjælpetekster, og øjet tænder udgangen på modellen for at lette tildelinger.

![](images/image\_046.png)

image74.png

## Dobbeltbelægning

Hver udgang kan have dobbeltbelægning. Eksempel:

- Første niveau: Positionslys & fjernlys
- Andet niveau: Nødblink

Skiftet mellem niveauer kan konfigureres.

![](images/image\_047.png)

image75.png

 til ![](images/image\_048.png)

image77.png

## Menu

| Funktion | Beskrivelse |
| --- | --- |
| Fil | Genforbind systemet, genindlæs modul, forkast midlertidige ændringer, gem og åbn moduler. |
| Moduler | Vis og indlæs alle moduler. |
| Systemindstillinger | Konfigurer grundlæggende systemadfærd. |
| Enhedsinformation | Information om moduler, softwareversioner, opdateringer, fabriksindstillinger. |
| Systemanalyse | Selvtest, kommunikationstest, find beskadigede moduler. |
| Kanalindlæringsassistent | Hjælper med indlæring af kanaler. |
| Logging | Kommunikation mellem ControlPanel og system til fejlfinding. |
| Live-dataassistent | Viser realtidsdata som styrestænger og kontaktstatus. |
| Rundumlys- og KnightRider-effektassistent | Hjælper med konfiguration over flere udgange. |
| Indstillinger | Ekspertindstillinger for avancerede konfigurationer (brug med forsigtighed). |
| Info | Information om ControlPanel og fejllogs. |

![](images/image\_049.png)

image78.png

## Symbolbjælke

![](images/image\_050.png)

image85.png

- Vis hovedskærm
- Genforbind systemet
- Genindlæs moduler
- Lys fra / Positionslys / Nærlys / Fjernlys / Tågeforlygter / Tågelygte bag tænd/sluk
- Live-data, enhedsinformation, systemindstillinger
- Vis live-udgang, åbn live-opdatering

## Live-data

Giver realtidsindsigt i styrestangpositioner og kontaktstatus. Kanaler kan indlæres, og funktioner kan tændes/slukkes.

![](images/image\_051.png)

image86.png

|  |  |
| --- | --- |
| [[IMAGE\_078]] | Når kanalerne er korrekt indlært, skal de blå prikker følge dine styrestangsbevægelser. Hvis du bruger CPPM, IBUS eller SBUS, skal kanalerne også være korrekt tildelt. |
| 665544332211 [[IMAGE\_079]] | Her vises alle kanaler, som de faktisk måles. Indlæringsinformationer tages ikke i betragtning, dvs. søjlerne kan bevæge sig nedad, selvom styrestangen bevæges opad.1: Kanaltilordning bør kun ændres, hvis CPPM, IBUS eller SBUS anvendes.2-5: Disse værdier sættes under indlæringsprocessen. 1000 – 2000 og 1500 midterstilling er standardværdier. Værdierne kan justeres og gemmes.6: Scroll til højre for at se værdier for andre kanaler (kun relevant for CPPM, IBUS, SBUS) |
|  | Den højre side af live-data viser kontaktstatus. Nogle kan sættes ved klik. De tre funktionsgrupper Basislysfunktioner, Tilføjelsesfunktioner og Analog kan bruges som kontakter i funktioner, f.eks. i funktionen Enkelkontakt. [[IMAGE\_080]] [[IMAGE\_081]] |

![](images/image\_052.png)

image87.png

De blå prikker skal følge styrestangsbevægelserne. Ved CPPM, IBUS eller SBUS skal kanaler være korrekt tildelt.

![](images/image\_053.png)

image88.png

Den højre side viser kontaktstatus, som også kan sættes ved klik. De tre funktionsgrupper Basislys, Tilføjelsesfunktioner og Analog kan bruges som kontakter.

![](images/image\_054.png)

image90.png

 ![](images/image\_055.png)

image91.png