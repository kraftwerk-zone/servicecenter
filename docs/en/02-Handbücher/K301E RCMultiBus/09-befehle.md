# Commands

All commands start with `0xA1` or `0xA2`, are encoded in Tag-Length-Value format (TLV), and end with an XOR checksum.

| Start byte | Tag (Command) | Length | Value (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 / 0xA2 | 0x6C | 0x03 | 0x01 0x01 0x01 | 0xCF |

The checksum is calculated as XOR over all bytes with a start value of `0xAA`.

## SET\_FCT\_DIRECT

The *SetFunctionDirect* function allows individual functions to be switched on or off directly.

| Start byte | Tag (Command) | Length | Value (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x6C | 0x03 | 0x01 0x03 0x01 | 0xCD |

#### Data format

| Byte 1 | Byte 2 | Byte 3 |
| --- | --- | --- |
| Data object (e.g., basic functions) | Bit offset 1–40 (e.g., parking light, dipped beam) | On/Off (1 = On, 0 = Off) |

## SET\_PARAMETER

The *SetParameter* function allows script parameters for all outputs to be changed, e.g., "Set all high beam brightness values to 80%".

| Start byte | Tag (Command) | Length | Value (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x76 | 0x02 | 0x04 0x50 | 0x81 |

## SET\_DATA

This function is used to periodically set all values – both proportional and digital functions.

| Start byte | Tag of data structure | Length | Value (Data) | Checksum |
| --- | --- | --- | --- | --- |
| 0xA2 | Tag of data structure | 0x05 | 0x87 0x80 0x00 0x00 0x00 | 0xCF |

![](images/image_001.png)

image1.png

 ![](images/image_002.png)

image2.png