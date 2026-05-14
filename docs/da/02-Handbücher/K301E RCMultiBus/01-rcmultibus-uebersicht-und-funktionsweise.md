# RCMultiBus – Oversigt og funktion

**RCMultiBus** fungerer som et overordnet protokol for alle 3-ledede databusser, der anvendes inden for RC-området. En slave-enhed, der understøtter RCMultiBus, skal kunne fortolke alle bustyper inklusive protokol, baudrate og polaritet. En master-enhed skal derimod kun kunne generere en af bustyperne.

## Understøttede bustyper

- IBUS
- SBUS
- EX-Bus
- CPPM

Afhængigt af bustypen kan proportionale og/eller digitale informationer modtages. Hver proportional kanal omdannes altid til digitale kontaktfunktioner (permanent og i hukommelsen).