# RCMultiBus – Übersicht und Funktionsweise

Der **RCMultiBus** dient als übergeordnetes Protokoll für alle 3-Draht-basierten Datenbusse, die im RC-Bereich verwendet werden. Ein Slave-Gerät, das RCMultiBus unterstützt, muss in der Lage sein, alle Bus-Typen inklusive Protokoll, Baudrate und Polarität zu interpretieren. Ein Master-Gerät hingegen muss nur einen der Bus-Typen erzeugen können.

## Unterstützte Bus-Typen

- IBUS
- SBUS
- EX-Bus
- CPPM

Je nach Bus-Typ können proportionale und/oder digitale Informationen empfangen werden. Jeder proportionale Kanal wird stets in digitale Schaltfunktionen (permanent und im Speicher) umgewandelt.
