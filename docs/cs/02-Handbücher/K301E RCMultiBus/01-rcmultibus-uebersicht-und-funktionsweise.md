# RCMultiBus – Přehled a fungování

**RCMultiBus** slouží jako nadřazený protokol pro všechny 3drátové datové sběrnice používané v RC oblasti. Slave zařízení podporující RCMultiBus musí být schopno interpretovat všechny typy sběrnic včetně protokolu, přenosové rychlosti a polarity. Master zařízení naopak musí být schopno generovat pouze jeden z typů sběrnic.

## Podporované typy sběrnic

- IBUS
- SBUS
- EX-Bus
- CPPM

Podle typu sběrnice lze přijímat proporcionální a/nebo digitální informace. Každý proporcionální kanál je vždy převeden na digitální spínací funkce (trvalé a v paměti).