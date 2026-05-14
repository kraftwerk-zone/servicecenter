# RCMultiBus – Panoramica e Funzionamento

Il **RCMultiBus** funge da protocollo superiore per tutti i bus dati a 3 fili utilizzati nel settore RC. Un dispositivo slave che supporta RCMultiBus deve essere in grado di interpretare tutti i tipi di bus, inclusi protocollo, baud rate e polarità. Un dispositivo master, invece, deve essere in grado di generare solo uno dei tipi di bus.

## Tipi di bus supportati

- IBUS
- SBUS
- EX-Bus
- CPPM

A seconda del tipo di bus, possono essere ricevute informazioni proporzionali e/o digitali. Ogni canale proporzionale viene sempre convertito in funzioni di commutazione digitali (permanenti e in memoria).