# Estructuras de datos

## Funciones básicas (Etiqueta 0x01)

Las funciones básicas están codificadas en 5 bytes:

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Intermitente de emergencia | Intermitente izquierdo | Intermitente derecho | Luz de carretera intermitente | Faro antiniebla | Luz de carretera | Luz de cruce | Luz de posición |
| 1 | Patas de apoyo arriba | Rueda de repuesto | Motor en marcha | Arranque | Bocina | Luz antiniebla trasera | Luz de freno | Luz de marcha atrás |
| 2 | Impulso intermitente derecho | Luz rotativa | Luz diurna | Luz de giro izquierda | Luz de giro derecha | Volquete abajo | Volquete arriba | Patas de apoyo abajo |
| 3 | Interno/RFU | Bocina de señal | Marcha atrás | Marcha adelante | Luz de curva izquierda | Luz de curva derecha | Interno/RFU | Impulso intermitente izquierdo |
| 4 | Servo 2 | Servo 1 | Marcha 2/2 | Marcha 1/2 | Nivel de pad | Rampa abajo | Rampa arriba | Interno/RFU |

## Funciones adicionales (Etiqueta 0x05)

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | CH1 Memoria Medio Corto Derecho | CH1 Memoria Medio Corto Izquierdo | CH1 Derecho Completo | CH1 Izquierdo Completo | CH1 Memoria Completo Largo Derecho | CH1 Memoria Completo Largo Izquierdo | CH1 Memoria Completo Corto Derecho | CH1 Memoria Completo Corto Izquierdo |
| 1 | CH2 Memoria Completo Largo Derecho | CH2 Memoria Completo Largo Izquierdo | CH2 Memoria Completo Corto Derecho | CH2 Memoria Completo Corto Izquierdo | CH1 Derecho Medio | CH1 Izquierdo Medio | CH1 Memoria Medio Largo Derecho | CH1 Memoria Medio Largo Izquierdo |
| 2 | CH2 Derecho Medio | CH2 Izquierdo Medio | CH2 Memoria Medio Largo Derecho | CH2 Memoria Medio Largo Izquierdo | CH2 Memoria Medio Corto Derecho | CH2 Memoria Medio Corto Izquierdo | CH2 Derecho Completo | CH2 Izquierdo Completo |
| … | … | | | | | | | |
| 45 | CH31 Memoria Medio Corto Derecho | CH31 Memoria Medio Corto Izquierdo | CH31 Derecho Completo | CH31 Izquierdo Completo | CH31 Memoria Completo Largo Derecho | CH31 Memoria Completo Largo Izquierdo | CH31 Memoria Completo Corto Derecho | CH31 Memoria Completo Corto Izquierdo |
| 46 | CH32 Memoria Completo Largo Derecho | CH32 Memoria Completo Largo Izquierdo | CH32 Memoria Completo Corto Derecho | CH32 Memoria Completo Corto Izquierdo | CH31 Derecho Medio | CH31 Izquierdo Medio | CH31 Memoria Medio Largo Derecho | CH31 Memoria Medio Largo Izquierdo |
| 47 | CH32 Derecho Medio | CH32 Izquierdo Medio | CH32 Memoria Medio Largo Derecho | CH32 Memoria Medio Largo Izquierdo | CH32 Memoria Medio Corto Derecho | CH32 Memoria Medio Corto Izquierdo | CH32 Derecho Completo | CH32 Izquierdo Completo |

## Funciones proporcionales (Etiqueta 0x41)

Los valores son valores con signo de 16 bits en el rango de -500 a +500, lo que corresponde a una indicación de -100 % a +100 %. Los datos están en formato Little-Endian.

| CH1 (Acelerador) | CH2 (Dirección) | CH3 | CH4 | … | CH31 | CH32 |
| --- | --- | --- | --- | --- | --- | --- |