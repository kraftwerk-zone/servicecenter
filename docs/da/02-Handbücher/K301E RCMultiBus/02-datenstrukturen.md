# Datastrukturer

## Basisfunktioner (Tag 0x01)

Basisfunktioner er kodet i 5 bytes:

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Nødblink | Venstre blinklys | Højre blinklys | Fjernlysblink | Tågeforlygte | Fjernlys | Nærlys | Positionslys |
| 1 | Støtteben op | Femte hjul | Motor kører | Start | Horn | Baglygter tåge | Bremselys | Baklys |
| 2 | Højre blink impuls | Rundtlys | Kørelys | Svinglys venstre | Svinglys højre | Kasse ned | Kasse op | Støtteben ned |
| 3 | Intern/RFU | Signalhorn | Gear ned | Gear op | Kurvelys venstre | Kurvelys højre | Intern/RFU | Venstre blink impuls |
| 4 | Servo 2 | Servo 1 | Gear 2/2 | Gear 1/2 | Pad-niveau | Rampe ned | Rampe op | Intern/RFU |

## Ekstra funktioner (Tag 0x05)

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | CH1 Memory Half Short Højre | CH1 Memory Half Short Venstre | CH1 Højre Fuld | CH1 Venstre Fuld | CH1 Memory Fuld Lang Højre | CH1 Memory Fuld Lang Venstre | CH1 Memory Fuld Kort Højre | CH1 Memory Fuld Kort Venstre |
| 1 | CH2 Memory Fuld Lang Højre | CH2 Memory Fuld Lang Venstre | CH2 Memory Fuld Kort Højre | CH2 Memory Fuld Kort Venstre | CH1 Højre Halv | CH1 Venstre Halv | CH1 Memory Half Lang Højre | CH1 Memory Half Lang Venstre |
| 2 | CH2 Højre Halv | CH2 Venstre Halv | CH2 Memory Half Lang Højre | CH2 Memory Half Lang Venstre | CH2 Memory Half Kort Højre | CH2 Memory Half Kort Venstre | CH2 Højre Fuld | CH2 Venstre Fuld |
| … | … | | | | | | | |
| 45 | CH31 Memory Half Short Højre | CH31 Memory Half Short Venstre | CH31 Højre Fuld | CH31 Venstre Fuld | CH31 Memory Fuld Lang Højre | CH31 Memory Fuld Lang Venstre | CH31 Memory Fuld Kort Højre | CH31 Memory Fuld Kort Venstre |
| 46 | CH32 Memory Fuld Lang Højre | CH32 Memory Fuld Lang Venstre | CH32 Memory Fuld Kort Højre | CH32 Memory Fuld Kort Venstre | CH31 Højre Halv | CH31 Venstre Halv | CH31 Memory Half Lang Højre | CH31 Memory Half Lang Venstre |
| 47 | CH32 Højre Halv | CH32 Venstre Halv | CH32 Memory Half Lang Højre | CH32 Memory Half Lang Venstre | CH32 Memory Half Kort Højre | CH32 Memory Half Kort Venstre | CH32 Højre Fuld | CH32 Venstre Fuld |

## Proportionale funktioner (Tag 0x41)

Værdierne er 16-bit signed værdier i området fra -500 til +500, hvilket svarer til en visning fra -100 % til +100 %. Dataene er i little-endian format.

| CH1 (Gas) | CH2 (Styring) | CH3 | CH4 | … | CH31 | CH32 |
| --- | --- | --- | --- | --- | --- | --- |