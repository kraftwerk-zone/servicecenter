# Comandos

Todos los comandos comienzan con `0xA1` o `0xA2`, están codificados en formato Tag-Length-Value (TLV) y terminan con una suma de verificación XOR.

| Byte de inicio | Etiqueta (Comando) | Longitud | Valor (Datos) | Suma de verificación |
| --- | --- | --- | --- | --- |
| 0xA1 / 0xA2 | 0x6C | 0x03 | 0x01 0x01 0x01 | 0xCF |

La suma de verificación se calcula como XOR sobre todos los bytes con valor inicial `0xAA`.

## SET\_FCT\_DIRECT

Con la función *SetFunctionDirect* se pueden activar o desactivar funciones individuales directamente.

| Byte de inicio | Etiqueta (Comando) | Longitud | Valor (Datos) | Suma de verificación |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x6C | 0x03 | 0x01 0x03 0x01 | 0xCD |

#### Formato de datos

| Byte 1 | Byte 2 | Byte 3 |
| --- | --- | --- |
| Objeto de datos (p. ej. funciones básicas) | Desplazamiento de bit 1–40 (p. ej. luz de estacionamiento, luz de cruce) | Encendido/Apagado (1 = Encendido, 0 = Apagado) |

## SET\_PARAMETER

Con la función *SetParameter* se pueden cambiar parámetros de script para todas las salidas, por ejemplo, "Establecer todos los valores de brillo de luz de carretera al 80 %".

| Byte de inicio | Etiqueta (Comando) | Longitud | Valor (Datos) | Suma de verificación |
| --- | --- | --- | --- | --- |
| 0xA1 | 0x76 | 0x02 | 0x04 0x50 | 0x81 |

## SET\_DATA

Esta función sirve para establecer periódicamente todos los valores, tanto funciones proporcionales como digitales.

| Byte de inicio | Etiqueta de la estructura de datos | Longitud | Valor (Datos) | Suma de verificación |
| --- | --- | --- | --- | --- |
| 0xA2 | Etiqueta de la estructura de datos | 0x05 | 0x87 0x80 0x00 0x00 0x00 | 0xCF |

![](images/image_001.png)

image1.png

 ![](images/image_002.png)

image2.png