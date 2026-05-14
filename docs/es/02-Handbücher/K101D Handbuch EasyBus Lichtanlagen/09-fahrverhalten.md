# Comportamiento de conducción

## Tipo de regulador de velocidad

En principio, cualquier regulador de velocidad es compatible con EasyBus. Para un control correcto de la luz de freno y la luz de marcha atrás, debe configurarse el tipo correcto de regulador de velocidad:

- **Simple:** La marcha atrás comienza inmediatamente al mover la palanca hacia atrás.
- **Freno separado:** Primero freno, luego marcha atrás tras tirar de nuevo.
- **Control de crucero estándar:** La desaceleración pasa directamente a la marcha atrás.
- **Control de crucero Servonaut:** Cambio de marcha mediante K1, salida del servo configurada en "Función proporcional K1".
- **Servonaut en punto muerto:** Como el control de crucero Servonaut, pero con posición de punto muerto entre adelante y atrás.
- **Servonaut K40:** Luz de freno y marcha atrás conmutadas al estilo K40.
- **Luz de freno/marcha atrás analógica:** Entradas analógicas de salida de conmutación de un regulador de velocidad (ver capítulo 11.4).

## Luz de freno inteligente

La luz de freno se enciende ya durante la desaceleración, no solo al ir marcha atrás. La sensibilidad y la duración del encendido posterior se pueden ajustar en la configuración del sistema.

## Tipo de dirección

Por defecto, el intermitente debe activarse manualmente y se desactiva automáticamente. Como alternativa, se puede elegir el "Intermitente automático", que se activa automáticamente en curvas. El "Umbral del intermitente" define el nivel de activación.

## Tipo de luz de curva

El comportamiento de la luz de curva se puede configurar mediante el parámetro "Tipo de luz de curva". Las opciones son autoexplicativas.