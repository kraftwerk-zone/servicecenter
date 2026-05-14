# Estructuras de datos

## Funciones básicas (Etiqueta 0x01)

Las funciones básicas están codificadas en 5 bytes:

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Intermitente de emergencia | Intermitente izquierdo | Intermitente derecho | Luz alta intermitente | Faros antiniebla | Luz alta | Luz baja | Luz de posición |
| 1 | Patas de apoyo arriba | Rueda de repuesto | Motor en marcha | Motor de arranque | Bocina | Luz antiniebla trasera | Freno | Marcha atrás |
| 2 | Impulso intermitente derecho | Luz rotativa | Luz diurna | Intermitente izquierdo | Bajar | Subir | Patas de apoyo abajo |  |
| 3 | Interno/RFU | Bocina de señal | Marcha abajo | Marcha arriba | Luz de curva izquierda | Luz de curva derecha | Interno/RFU | Impulso intermitente izquierdo |
| 4 | Servo 2 | Servo 1 | Marcha 2/2 | Marcha 1/2 | Nivel de plataforma | Rampa abajo | Rampa arriba | Interno/RFU |

## Funciones adicionales (Etiqueta 0x05)

| Offset | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | CH1 Memoria Medio Corto Derecho | CH1 Memoria Medio Corto Izquierdo | CH1 Derecho Completo | CH1 Izquierdo Completo | CH1 Memoria Largo Completo Derecho | CH1 Memoria Largo Completo Izquierdo | CH1 Memoria Corto Completo Derecho | CH1 Memoria Corto Completo Izquierdo |
| 1 | CH2 Memoria Largo Completo Derecho | CH2 Memoria Largo Completo Izquierdo | CH2 Memoria Corto Completo Derecho | CH2 Memoria Corto Completo Izquierdo | CH1 Derecho Medio | CH1 Izquierdo Medio | CH1 Memoria Largo Medio Derecho | CH1 Memoria Largo Medio Izquierdo |
| 2 | CH2 Derecho Medio | CH2 Izquierdo Medio | CH2 Memoria Largo Medio Derecho | CH2 Memoria Largo Medio Izquierdo | CH2 Memoria Corto Medio Derecho | CH2 Memoria Corto Medio Izquierdo | CH2 Derecho Completo | CH2 Izquierdo Completo |
| … |  |  |  |  |  |  |  |  |
| 45 | CH31 Memoria Corto Medio Derecho | CH31 Memoria Corto Medio Izquierdo | CH31 Derecho Completo | CH31 Izquierdo Completo | CH31 Memoria Largo Completo Derecho | CH31 Memoria Largo Completo Izquierdo | CH31 Memoria Corto Completo Derecho | CH31 Memoria Corto Completo Izquierdo |
| 46 | CH32 Memoria Largo Completo Derecho | CH32 Memoria Largo Completo Izquierdo | CH32 Memoria Corto Completo Derecho | CH32 Memoria Corto Completo Izquierdo | CH31 Derecho Medio | CH31 Izquierdo Medio | CH31 Memoria Largo Medio Derecho | CH31 Memoria Largo Medio Izquierdo |
| 47 | CH32 Derecho Medio | CH32 Izquierdo Medio | CH32 Memoria Largo Medio Derecho | CH32 Memoria Largo Medio Izquierdo | CH32 Memoria Corto Medio Derecho | CH32 Memoria Corto Medio Izquierdo | CH32 Derecho Completo | CH32 Izquierdo Completo |

## Funciones proporcionales (Etiqueta 0x41)

Los valores son valores con signo de 16 bits de -500 a +500, lo que corresponde a una indicación de -100 % a +100 %. Los datos están almacenados en formato Little-Endian.

| CH1 (Acelerador) | CH2 (Dirección) | CH3 | CH4 | … | CH31 | CH32 |
| --- | --- | --- | --- | --- | --- | --- |