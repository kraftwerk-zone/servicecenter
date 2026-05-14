# RCMultiBus – Overview and Functionality

The **RCMultiBus** serves as a universal protocol for all 3-wire based data buses used in the RC domain. A slave device that supports RCMultiBus must be capable of interpreting all bus types including protocol, baud rate, and polarity. A master device, on the other hand, only needs to be able to generate one of the bus types.

## Supported Bus Types

- IBUS
- SBUS
- EX-Bus
- CPPM

Depending on the bus type, proportional and/or digital information can be received. Each proportional channel is always converted into digital switch functions (permanent and stored).