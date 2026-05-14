# ControlPanel

## Generelt

Ved opstart af ControlPanel skal modellen være klar til drift: Batteri opladet og tilsluttet, model og fjernbetjening tændt og bundet, servomotorer bevægelige.

Systemet registreres automatisk, og alle moduler vises.

![](images/image\_023.png)

image72.png

 ![](images/image\_040.png)

image73.png

## Moduloversigt

Ved klik på et modul kommer du til udgangsoversigten. Her kan du tildele navne, indstille tænd- og slukhastigheder og afhængigt af funktion konfigurere yderligere parametre.

Ændringer gemmes med disketteikonet. Hjælp er tilgængelig via spørgsmålstegnet. Med øjeikonet kan udgange på modellen aktiveres direkte for at lette tildelingen.

![](images/image\_025.png)

image74.png

## Dobbeltbelægning

Hver udgang kan dobbeltbelægges. Eksempel:

- Første niveau: Positionslys & fjernlys
- Andet niveau: Nødblink

Skiftet mellem niveauer kan konfigureres.

![](images/image\_026.png)

image75.png

 til ![](images/image\_027.png)

image77.png

## Menu

|  |  |
| --- | --- |
| **Fil** | Genforbind systemet, genindlæs moduler, forkast midlertidige ændringer, gem og åbn moduler. |
| **Moduler** | Vis og indlæs alle moduler. |
| **Systemindstillinger** | Grundlæggende systemkonfiguration. |
| **Enhedsinformation** | Information om moduler, opdateringer, fabriksindstillinger. |
| **Systemanalyse** | Selvtest, kommunikationstest, søg efter beskadigede moduler. |
| **Kanallæringsassistent** | Hjælper med indlæring af kanaler. |
| **Logging** | Kommunikationslog til fejlfinding. |
| **Live-dataassistent** | Realtidsvisning af styrestænger og kontaktstatus. |
| **Effektassistenter** | Konfiguration af rundlys- og KnightRider-effekter. |
| **Indstillinger** | Avancerede muligheder, ekspertmode (advarsel om mulige skader). |
| **Info** | Information om ControlPanel og fejllogs. |

## Symbolbjælke

![](images/image\_028.png)

image85.png

- Vis hovedskærm
- Genforbind system
- Genindlæs moduler
- Lys Fra / Positionslys / Nærlys / Fjernlys / Tågeforlygter / Tågelygte bag Tænd/Sluk
- Vis live-data
- Enhedsinformation
- Systemindstillinger
- Vis live-udgang
- Åbn live-opdatering

## Live-data

Live-data-visningen viser styrestangpositioner og kontaktstatus i realtid. Kanaler kan indlæres, og funktioner kan tændes eller slukkes.

![](images/image\_029.png)

image86.png

|  |  |
| --- | --- |
| [[IMAGE\_078]] | Når kanalerne er korrekt indlært, skal de blå prikker følge dine styrestangsbevægelser. Hvis du bruger CPPM, IBUS eller SBUS, skal kanalerne også være korrekt tildelt. |
| 665544332211 [[IMAGE\_079]] | Her vises alle kanaler, som de faktisk måles. Indlæringsinformationer tages ikke i betragtning, dvs. søjlerne kan bevæge sig nedad, selvom styrestangen bevæges opad.1: Kanaltilordning bør kun ændres, hvis CPPM, IBUS eller SBUS anvendes.2-5: Disse værdier sættes under indlæringsprocessen. 1000 – 2000 og 1500 midterposition er standardværdier. Værdierne kan justeres og gemmes.6: Scroll til højre for at se værdier for andre kanaler (kun relevant for CPPM, IBUS, SBUS) |
|  | Højre side af live-data viser kontaktstatus. Nogle kan ændres ved klik. De tre funktionsgrupper Basislysfunktioner, Tilføjelsesfunktioner og Analog kan bruges som kontakter i funktionerne, f.eks. ved funktionen Enkelkontakt. [[IMAGE\_080]] [[IMAGE\_081]] |

![](images/image\_030.png)

image87.png

Ved korrekt indlæring følger de blå prikker styrestangsbevægelserne. For CPPM, I-BUS eller S-BUS skal kanaltilordningen være korrekt.

![](images/image\_031.png)

image88.png

Højre side viser kontaktstatus, som delvist kan ændres ved klik.

![](images/image\_032.png)

image90.png

 ![](images/image\_033.png)

image91.png

## Opdateringer

Efter tilslutning viser ControlPanel tilgængelige opdateringer til busmoduler.

![](images/image\_043.png)

image6.png

Tips til sikker opdatering:

- Opdater kun ét modul ad gangen.
- Undgå strømafbrydelser.
- Afbryd servomotorer og motorer under opdatering.
- Genstart model og ControlPanel ved problemer.

![](images/image\_035.png)

image92.png

 ![](images/image\_043.png)

image6.png

Opdateringer kan nulstille fabriksindstillinger. ControlPanel gemmer automatisk alle indstillinger på harddisken.

![](images/image\_037.png)

image93.png

 ![](images/image\_038.png)

image94.png

 ![](images/image\_039.png)

image95.png

Efter opdateringer vises alle moduler. KLM 4/16 består af hovedmodulet med fire servo-udgange og den integrerede kontaktudvidelse med 16 kontaktudgange.

![](images/image\_040.png)

image73.png

## Enhedsinformation

Viser grundlæggende information om moduler. "Vis enhed" tænder de første tre udgange, nyttigt ved flere udvidelser uden navngivning.

Moduler kan genstartes, nulstilles til fabriksindstillinger eller opdateres.

![](images/image\_041.png)

image96.png

## Systemanalyse

Hjælper med fejlfinding ved at læse informationer, søge efter beskadigede moduler og udføre kommunikationstest.

![](images/image\_042.png)

image97.png

 ![](images/image\_043.png)

image6.png

## Kanaler indlære

Assistenten hjælper med indlæring af kanaler. Indstil korrekt tildeling for K1 og K2 på forhånd, især ved brug af styrepads.

![](images/image\_044.png)

image98.png