# Módulo de sonido

Los módulos de sonido pueden funcionar directamente en el receptor. Para el control a través de EasyBus, deben conectarse a dos salidas de servo (directamente en el KLM 4/16 o en el KSB 2/4).

## Compatible con Servonaut SMT

Un canal para la información del gas, el segundo para arrancar/detener y tocar la bocina (pulsado en direcciones opuestas).

![](images/image\_019.png)

image30.png

## Módulos de sonido programables (p. ej. BEIER USM-RC)

Se basan en el modo Servonaut, pero amplían la posibilidad de controlar una segunda bocina.

![](images/image\_020.png)

image31.png

En el módulo de sonido se deben realizar las siguientes configuraciones:

![](images/image\_021.png)

image32.png

## Control del módulo de sonido

Con el panel de control Luz y Sonido no se necesitan configuraciones adicionales. El botón de la bocina controla la bocina, el botón de nivel arranca o detiene el motor.

Los canales adicionales K1 y K2 (o hasta K10 al usar IBUS, SBUS, SUMD, etc.) pueden asignarse de forma personalizada en la configuración del sistema.

![](images/image\_022.png)

image33.png

También es posible una combinación entre el panel de control y la asignación personalizada.

![](images/image\_023.png)

image34.png

## Configuraciones importantes

- **Motor arranca inmediatamente:** Dependiendo de si el módulo de sonido arranca el motor inmediatamente, se debe activar o desactivar la configuración del sistema "Motor arranca inmediatamente [activo]".
- **Precaución:** ¡El motor de tracción está activo en todo caso!
- **Luces parpadeantes:** Cada placa de iluminación y extensión de interruptores (KLB) tiene configuraciones del sistema para "Efecto de arranque" (parpadeo al arrancar) y "Reducción de luz al parar motor" (reducción al detener el motor). Use esta última solo si no se controlan componentes con electrónica integrada.
- La duración del parpadeo puede ajustarse con "Duración de arranque del motor" para que coincida con la duración de arranque del módulo de sonido.