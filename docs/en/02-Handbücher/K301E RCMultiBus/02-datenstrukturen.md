# Data Structures

## Basic Functions (Tag 0x01)

Basic functions are encoded in 5 bytes:

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hazard Lights | Left Indicator | Right Indicator | High Beam Flasher | Fog Lights | High Beam | Low Beam | Parking Lights |
| 1 | Support Legs Up | Fifth Wheel | Engine Running | Starting | Horn | Rear Fog Light | Brake Light | Reverse Light |
| 2 | Right Indicator Pulse | Beacon Light | Daytime Running Light | Left Cornering Light | Right Cornering Light | Dump Down | Dump Up | Support Legs Down |
| 3 | Internal/RFU | Signal Horn | Gear Down | Gear Up | Left Cornering Light | Right Cornering Light | Internal/RFU | Left Indicator Pulse |
| 4 | Servo 2 | Servo 1 | Gear 2/2 | Gear 1/2 | Pad Level | Ramp Down | Ramp Up | Internal/RFU |

## Additional Functions (Tag 0x05)

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | CH1 Memory Half Short Right | CH1 Memory Half Short Left | CH1 Right Full | CH1 Left Full | CH1 Memory Full Long Right | CH1 Memory Full Long Left | CH1 Memory Full Short Right | CH1 Memory Full Short Left |
| 1 | CH2 Memory Full Long Right | CH2 Memory Full Long Left | CH2 Memory Full Short Right | CH2 Memory Full Short Left | CH1 Right Half | CH1 Left Half | CH1 Memory Half Long Right | CH1 Memory Half Long Left |
| 2 | CH2 Right Half | CH2 Left Half | CH2 Memory Half Long Right | CH2 Memory Half Long Left | CH2 Memory Half Short Right | CH2 Memory Half Short Left | CH2 Right Full | CH2 Left Full |
| … | … | | | | | | | |
| 45 | CH31 Memory Half Short Right | CH31 Memory Half Short Left | CH31 Right Full | CH31 Left Full | CH31 Memory Full Long Right | CH31 Memory Full Long Left | CH31 Memory Full Short Right | CH31 Memory Full Short Left |
| 46 | CH32 Memory Full Long Right | CH32 Memory Full Long Left | CH32 Memory Full Short Right | CH32 Memory Full Short Left | CH31 Right Half | CH31 Left Half | CH31 Memory Half Long Right | CH31 Memory Half Long Left |
| 47 | CH32 Right Half | CH32 Left Half | CH32 Memory Half Long Right | CH32 Memory Half Long Left | CH32 Memory Half Short Right | CH32 Memory Half Short Left | CH32 Right Full | CH32 Left Full |

## Proportional Functions (Tag 0x41)

The values are 16-bit signed values in the range of -500 to +500, corresponding to a display of -100% to +100%. The data is in little-endian format.

| CH1 (Throttle) | CH2 (Steering) | CH3 | CH4 | … | CH31 | CH32 |
| --- | --- | --- | --- | --- | --- | --- |