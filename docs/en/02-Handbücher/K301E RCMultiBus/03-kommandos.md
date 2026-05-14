# Commands

All commands start with 0xA1 or 0xA2, are encoded as Tag-Length-Value (TLV), and end with a XOR checksum.

| Start Byte | Tag (Command) | Length | Value (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 / 0xA2 | 0x6C | 0x03 | 0x01 0x01 0x01 | 0xCF |

The checksum is calculated as XOR over all bytes with 0xAA as the start value.

## SET\_FCT\_DIRECT – Direct Function Control

This function allows individual functions to be switched on or off directly.

| Start Byte | Tag (Command) | Length | Value (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x6C | 0x03 | 0x01 0x03 0x01 | 0xCD |

#### Data Format

| Byte 1 | Byte 2 | Byte 3 |
| --- | --- | --- |
| Data Object (e.g., basic functions) | Bit Offset (1–40, e.g., parking light, low beam) | On/Off (1 = On, 0 = Off) |

## SET\_PARAMETER – Parameter Change

This function allows script parameters for all outputs to be changed, e.g., "Set all high beam brightness values to 80%."

| Start Byte | Tag (Command) | Length | Value (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x76 | 0x02 | 0x04 0x50 | 0x81 |

## SET\_DATA – Periodic Data Transmission

This function is used to periodically set all values – both proportional and digital functions.

| Start Byte | Data Structure Tag | Length | Value (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA2 | corresponding tag | 0x05 | 0x87 0x80 0x00 0x00 0x00 | 0xCF |