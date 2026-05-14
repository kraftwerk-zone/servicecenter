# Puesta en marcha

Para la puesta en marcha de los sistemas KraftwerK EasyBus no se requieren pasos especiales. Sin embargo, recomendamos tener en cuenta la siguiente lista de verificación.

## Conexión al receptor

![](images/image\_065.png)

image6.png

Antes de conectar el KLM 4/16 al receptor, por favor verifique la asignación de las salidas del receptor. Para ello, utilice un servo y pruebe cada salida para comprobar su correcto funcionamiento. Anote la asignación.

![](images/image\_002.jpg)

image7.jpeg

**Nota:** Para evitar un arranque no deseado, se recomienda elevar el modelo.

Conecte los cables del servo para la dirección y el acelerador a las salidas correspondientes del receptor. El regulador de velocidad y el servo de dirección se conectan a las salidas de servo del KLM. Los canales K1 y K2 pueden usarse opcionalmente.

**Consejo:** La conexión del canal de acelerador y/o dirección puede omitirse si las luces de freno, marcha atrás y/o intermitentes se alimentan de forma analógica (véase el capítulo 11.5 «Actros 3363 luces de freno/marcha atrás e intermitentes desde el regulador de velocidad»).

**Consejo:** El regulador de velocidad y/o el servo de dirección también pueden conectarse directamente al receptor mediante un cable en Y para evitar interferencias causadas por el KLM.

## Conexión de las placas de iluminación

Todas las placas de expansión o de iluminación pueden conectarse directamente o a través de placas distribuidoras a las salidas de bus del asistente de luces.

## Programación de los canales

![](images/image\_065.png)

image6.png

¡La programación de los canales es el paso más importante para el correcto funcionamiento de los sistemas KraftwerK EasyBus!

Después de cada cambio en la configuración de su sistema de radio control (desplazamientos, direcciones de giro, posiciones centrales), los canales deben programarse de nuevo.

Los servos y motores controlados por los sistemas KraftwerK deben ajustarse mediante el ControlPanel, no a través del menú del sistema de radio control.

1. Encienda el sistema de radio control. Si el motor de tracción está conectado, eleve el modelo para que las ruedas no toquen el suelo.
2. Encienda el modelo. Tras el doble parpadeo del LED verde, mueva el canal de acelerador y el de dirección durante cinco segundos hasta el extremo, hasta que el LED rojo se encienda durante aproximadamente un segundo.
3. Vuelva a colocar las palancas en posición central.

El LED parpadea según los canales:

- 1x corto: Palanca de acelerador – extremo máximo de aceleración, luego extremo máximo de freno
- 2x corto: Palanca de dirección – extremo máximo a la izquierda, luego a la derecha
- 3x corto: Canal adicional K1 – extremo máximo a la izquierda, luego a la derecha
- 4x corto: Canal adicional K2 – extremo máximo arriba, luego abajo

Cuando todas las palancas estén en posición central, el LED rojo se enciende de forma continua y señala el fin del proceso de programación. El sistema se reinicia y muestra con un doble parpadeo verde que está listo para funcionar.