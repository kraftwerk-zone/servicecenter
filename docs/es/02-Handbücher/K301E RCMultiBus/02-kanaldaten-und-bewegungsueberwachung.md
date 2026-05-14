# Datos del canal y monitoreo de movimiento

Cada valor de canal se guarda y puede asignarse individualmente a cada salida de servo o motor. Además, se monitorea el movimiento de cada canal, a partir del cual se genera un campo de bits. Este campo de bits tiene tres dimensiones:

- **Dirección:** arriba (top) / abajo (bottom)
- **Intensidad del movimiento:** completo (full) / medio (half)
- **Estado:** permanente / en memoria (memory)

| CH | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH1 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| CH2 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| … |  |  |  |  |  |  |  |
| CHx | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |

## Ejemplos de monitoreo de movimiento

- **Ejemplo 1:** El canal 4 se mueve a +30% → se activa la bandera *CH4 Permanent/Top/Half*.
- **Ejemplo 2:** El canal 4 se mueve hacia atrás dentro de 0,5 segundos → se desactiva la bandera *CH4 Permanent/Top/Half*, se activa la bandera *CH4 Memory/Top/Half*.
- **Ejemplo 3:** El canal 1 se mueve a -100% → se activa la bandera *CH1 Permanent/Bottom/Full*.
- **Ejemplo 4:** El canal 1 se mueve hacia atrás después de un segundo → se desactiva la bandera *CH1 Permanent/Bottom/Full*, se activa la bandera *CH1 Memory/Bottom/Full*.