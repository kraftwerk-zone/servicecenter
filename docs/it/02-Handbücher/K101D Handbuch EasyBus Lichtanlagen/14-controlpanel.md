# ControlPanel

## Generale

All'avvio del ControlPanel il modello deve essere operativo: batteria carica e collegata, modello e radiocomando accesi e associati, servi mobili.

Il sistema viene rilevato automaticamente e tutti i moduli vengono visualizzati.

![](images/image\_023.png)

image72.png

 ![](images/image\_040.png)

image73.png

## Panoramica moduli

Cliccando su un modulo si accede alla panoramica delle uscite. Qui è possibile assegnare nomi, impostare le velocità di accensione e spegnimento e, a seconda della funzione, configurare ulteriori parametri.

Le modifiche si salvano con l'icona del floppy disk. Aiuti sono disponibili tramite il punto interrogativo. Con l'icona dell'occhio è possibile attivare direttamente le uscite sul modello per facilitare l'assegnazione.

![](images/image\_025.png)

image74.png

## Doppia assegnazione

Ogni uscita può essere assegnata doppiamente. Esempio:

- Primo livello: luci di posizione & abbaglianti
- Secondo livello: lampeggiatori di emergenza

La commutazione tra i livelli è configurabile.

![](images/image\_026.png)

image75.png

 fino a ![](images/image\_027.png)

image77.png

## Menu

|  |  |
| --- | --- |
| **File** | Ricollegare il sistema, ricaricare i moduli, scartare modifiche temporanee, salvare e aprire moduli. |
| **Moduli** | Visualizzare e caricare tutti i moduli. |
| **Impostazioni di sistema** | Configurazione di base del sistema. |
| **Informazioni dispositivo** | Informazioni sui moduli, aggiornamenti, impostazioni di fabbrica. |
| **Analisi sistema** | Autotest, test di comunicazione, ricerca moduli danneggiati. |
| **Assistente apprendimento canali** | Supporto per l'apprendimento dei canali. |
| **Logging** | Registro di comunicazione per la risoluzione dei problemi. |
| **Assistente dati live** | Visualizzazione in tempo reale delle posizioni delle leve e degli stati di commutazione. |
| **Assistenti effetti** | Configurazione di effetti luci rotanti e KnightRider. |
| **Impostazioni** | Opzioni avanzate, modalità esperto (avviso di possibili danni). |
| **Info** | Informazioni sul ControlPanel e report errori. |

## Barra degli strumenti

![](images/image\_028.png)

image85.png

- Visualizza schermata principale
- Ricollega sistema
- Ricarica moduli
- Luci Spente / Luci di posizione / Anabbaglianti / Abbaglianti / Fendinebbia / Luce posteriore fendinebbia On/Off
- Visualizza dati live
- Informazioni dispositivo
- Impostazioni sistema
- Visualizza uscita live
- Apri aggiornamento live

## Dati live

La vista dati live mostra in tempo reale le posizioni delle leve e gli stati di commutazione. I canali possono essere appresi e le funzioni attivate o disattivate.

![](images/image\_029.png)

image86.png

|  |  |
| --- | --- |
| [[IMAGE\_078]] | Quando i canali sono correttamente appresi, i punti blu devono seguire i movimenti della leva. Se si utilizzano CPPM, IBUS o SBUS, i canali devono anche essere correttamente assegnati. |
| 665544332211 [[IMAGE\_079]] | Qui vengono mostrati tutti i canali come effettivamente misurati. Le informazioni di apprendimento non sono considerate, cioè le barre possono muoversi verso il basso anche se la leva viene spostata verso l'alto.1: La modifica dell'assegnazione canali dovrebbe essere fatta solo se si usa CPPM, IBUS o SBUS.2-5: Questi valori sono impostati durante l'apprendimento. 1000 – 2000 e 1500 posizione centrale sono i valori standard. I valori possono essere adattati e salvati.6: Scorrere a destra per visualizzare i valori degli altri canali (rilevante solo per CPPM, IBUS, SBUS) |
|  | La parte destra dei dati live mostra gli stati di commutazione. Alcuni possono essere impostati cliccando. I tre gruppi di funzioni base luci, funzioni aggiuntive e analogiche possono essere usati come interruttori nelle funzioni, ad es. nella funzione interruttore semplice. [[IMAGE\_080]] [[IMAGE\_081]] |

![](images/image\_030.png)

image87.png

Con apprendimento corretto i punti blu seguono i movimenti della leva. Per CPPM, I-BUS o S-BUS l'assegnazione canali deve essere corretta.

![](images/image\_031.png)

image88.png

La parte destra mostra gli stati di commutazione, modificabili in parte con un clic.

![](images/image\_032.png)

image90.png

 ![](images/image\_033.png)

image91.png

## Aggiornamenti

Dopo la connessione il ControlPanel mostra gli aggiornamenti disponibili per i moduli bus.

![](images/image\_043.png)

image6.png

Consigli per un aggiornamento sicuro:

- Aggiornare un modulo alla volta.
- Evitare interruzioni di corrente.
- Scollegare servi e motori durante l'aggiornamento.
- Riavviare modello e ControlPanel in caso di problemi.

![](images/image\_035.png)

image92.png

 ![](images/image\_043.png)

image6.png

Gli aggiornamenti possono resettare le impostazioni di fabbrica. Il ControlPanel salva automaticamente tutte le impostazioni sul disco fisso.

![](images/image\_037.png)

image93.png

 ![](images/image\_038.png)

image94.png

 ![](images/image\_039.png)

image95.png

Dopo gli aggiornamenti tutti i moduli vengono visualizzati. Il KLM 4/16 è composto dal modulo principale con quattro uscite servo e dall'espansione interruttori integrata con 16 uscite di commutazione.

![](images/image\_040.png)

image73.png

## Informazioni dispositivo

Visualizzazione delle informazioni di base sui moduli. "Mostra dispositivo" attiva le prime tre uscite, utile con più espansioni senza assegnazione nomi.

I moduli possono essere riavviati, resettati alle impostazioni di fabbrica o aggiornati.

![](images/image\_041.png)

image96.png

## Analisi sistema

Aiuta nella ricerca guasti leggendo informazioni, cercando moduli danneggiati e testando la comunicazione.

![](images/image\_042.png)

image97.png

 ![](images/image\_043.png)

image6.png

## Apprendimento canali

L'assistente supporta nell'apprendimento dei canali. Impostare prima la corretta assegnazione per K1 e K2, specialmente se si usano pad di controllo.

![](images/image\_044.png)

image98.png