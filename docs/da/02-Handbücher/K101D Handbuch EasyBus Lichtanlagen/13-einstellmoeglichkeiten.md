# Indstillinger

## Systemindstillinger

Systemindstillinger gælder for hele modulet eller systemet (f.eks. blinkinterval, modtager-type, bremselys-type). Du åbner disse via tandhjulsikonet eller menuen „System“ → „Systemindstillinger“.

![](images/image\_009.png)

image41.png

 ![](images/image\_010.png)

image42.png

| Navn | Beskrivelse |
| --- | --- |
| Startforsinkelse [s] | Forsinker systemstart for at tage højde for opstartstider på fjernbetjeningen. |
| Indlæringsfunktion [aktiv] | Aktiverer/deaktiverer manuel indlæringsfunktion (gas- og styrestik i endestilling). ControlPanel-indlæring forbliver aktiv. |
| Infrarød [til] | Skifter udgang 8 til infrarød drift. |
| Blinklys Til/Fra | Definerer tænd- og sluk-tid for blinklyset i 10 ms trin. |
| Modtagertype | Se afsnit 8 „Styreværksvarianter / Modtagertype“. |
| Fartregulatortype | Se afsnit 9.1 „Fartregulatortype“. |
| Nødblink ved bakning | Automatisk aktivering af nødblink ved bakning. |
| Bremselys følsomhed | Følsomhed for det intelligente bremselys. |
| Bremselys efterglød | Varighed af efterglød på bremselyset. |
| Styringstype | Se afsnit 9.3 „Styringstype“. |
| Blinklys tærskelværdi | Tærskelværdi for automatisk blinklysaktivering. |
| Kurvelystype | Se afsnit 0 „Kurvelystype“. |
| Motor starter straks [aktiv] | Se afsnit 10 „Soundmodul“. |
| Motor start varighed | Varighed af motorstart-flimren. |
| Pad Alt Til/Fra | Konfiguration af „Alt Til/Fra“-knap på styrepads. |
| Pad Lys & Lyd Fjernlys / Tågeforlygter | Se manual for styrepad Lys & Lyd. |
| Tildeling K1 – K12 | Se afsnit 13.6 „Brugerdefineret“. |

## Styring af funktioner Lys – Kørsel – Ekstra

Standardstyring sker via fire proportionale kanaler (gas til venstre, styring til højre). Kanal K2 skifter mellem funktionsgrupperne Lys, Kørsel og Ekstra.

![](images/image\_011.png)

image43.png

**Indlæring af kanaler:**

1. Gas – Bremse  
2. Venstre – Højre  
3. K1 venstre – højre  
4. K2 op – ned  

![](images/image\_012.png)

image44.png

## Skift lysfunktioner

- Positionslys, nærlys: K2 op + K1 kort tryk til venstre  
- Fjernlys: K2 op + K1 kort tryk til højre (kun hvis positionslys er tændt)  
- Tågeforlygter, tågebaglys: K2 op + K1 langt tryk til højre (kun hvis positionslys er tændt)  
- Blinklys venstre/højre: K2 midt + K1 kort tryk til venstre/højre  
- Nødblink: K2 midt + K1 langt tryk til højre  
- Lysblink: K2 midt + K1 langt tryk til venstre (efter første tænding kan K1 venstre styres direkte)  
- Ekstra funktioner: K2 ned + K1 i endestilling (venstre/højre) kort eller langt tryk  

![](images/image\_013.png)

image45.png

 til ![](images/image\_014.png)

image54.png

## Pad grund- eller ekstra funktioner

Pads koder tastetryk i op- og nedadgående bevægelser. KLM dekoder disse og styrer funktionerne. Pads tilsluttes fjernbetjeningen og tilsluttes K1 eller K2 på KLM.

For at indlære kanalerne skal pad’en sættes i opsætningsmode (samtidigt tryk på de to øverste højre opsætningsknapper). Alternativt kan du bruge „Indlær kanaler“-assistenten i ControlPanel.

![](images/image\_015.png)

image61.png

 ![](images/image\_016.png)

image63.png

## Pad Lys & Lyd

Styrer funktioner afhængigt af tastetryk med udsving fra +100 til -100%. Tilslutning og betjening svarer til grund- og ekstra funktioner.

![](images/image\_017.png)

image65.png

Funktioner er opdelt i korte, lange og ekstra niveauer. Lysblink, horn og andre funktioner aktiveres ved langt tryk og kan derefter styres med korte tryk.

Efter to sekunders inaktivitet gendannes den oprindelige tildeling.

![](images/image\_018.png)

image67.png

## Multiswitch Robbe/Graupner

Begge protokoller genkendes automatisk. Multiswitch-værdier kan tildeles kanalerne K3 til K12 i LiveData-assistenten og brugerdefineres.

![](images/image\_019.png)

image68.png

## Brugerdefineret

Hver kanal (undtagen gas og styring) kan tildeles individuelt. K1 og K2 understøtter fuld- og halvudsving, K3 til K12 kun fuldudsving.

![](images/image\_020.png)

image69.png

 ![](images/image\_021.png)

image70.png

Funktioner kan defineres som „Varighed“, „Memory kort“ eller „Memory lang“. Eksempler er lysfunktioner, horn, sædekobling, støtteben, lad, rampe, start, gearskift, servo1/2 osv.

![](images/image\_022.png)

image71.png