# RCMultiBus – Visión general y funcionamiento

El **RCMultiBus** sirve como protocolo superior para todos los buses de datos basados en 3 hilos que se utilizan en el ámbito RC. Un dispositivo esclavo que soporte RCMultiBus debe ser capaz de interpretar todos los tipos de bus, incluyendo protocolo, velocidad en baudios y polaridad. Un dispositivo maestro, en cambio, solo debe ser capaz de generar uno de los tipos de bus.

## Tipos de bus soportados

- IBUS
- SBUS
- EX-Bus
- CPPM

Dependiendo del tipo de bus, se pueden recibir informaciones proporcionales y/o digitales. Cada canal proporcional se convierte siempre en funciones digitales de conmutación (permanentes y en memoria).