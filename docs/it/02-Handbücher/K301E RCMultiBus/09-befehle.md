# Comandi

Tutti i comandi iniziano con `0xA1` o `0xA2`, sono codificati nel formato Tag-Length-Value (TLV) e terminano con un checksum XOR.

| Byte di inizio | Tag (Comando) | Lunghezza | Valore (Dati) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 / 0xA2 | 0x6C | 0x03 | 0x01 0x01 0x01 | 0xCF |

Il checksum viene calcolato come XOR su tutti i byte con valore iniziale `0xAA`.

## SET\_FCT\_DIRECT

Con la funzione *SetFunctionDirect* è possibile attivare o disattivare direttamente singole funzioni.

| Byte di inizio | Tag (Comando) | Lunghezza | Valore (Dati) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x6C | 0x03 | 0x01 0x03 0x01 | 0xCD |

#### Formato dati

| Byte 1 | Byte 2 | Byte 3 |
| --- | --- | --- |
| Oggetto dati (es. funzioni base) | Offset bit 1–40 (es. luci di parcheggio, abbaglianti) | On/Off (1 = acceso, 0 = spento) |

## SET\_PARAMETER

Con la funzione *SetParameter* è possibile modificare i parametri dello script per tutte le uscite, ad esempio "Impostare tutti i valori di luminosità degli abbaglianti all'80%".

| Byte di inizio | Tag (Comando) | Lunghezza | Valore (Dati) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x76 | 0x02 | 0x04 0x50 | 0x81 |

## SET\_DATA

Questa funzione serve per impostare periodicamente tutti i valori – sia funzioni proporzionali che digitali.

| Byte di inizio | Tag della struttura dati | Lunghezza | Valore (Dati) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA2 | Tag della struttura dati | 0x05 | 0x87 0x80 0x00 0x00 0x00 | 0xCF |

![](images/image\_001.png)

image1.png

 ![](images/image\_002.png)

image2.png