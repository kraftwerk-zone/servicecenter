# ControlPanel

## General

Al iniciar el ControlPanel, el modelo debe estar listo para operar: batería cargada y conectada, modelo y control remoto encendidos y vinculados, servos móviles.

El sistema se detecta automáticamente y se muestran todos los módulos.

![](images/image\_023.png)

image72.png

 ![](images/image\_040.png)

image73.png

## Vista general de módulos

Al hacer clic en un módulo, se accede a la vista general de salidas. Allí puede asignar nombres, configurar velocidades de encendido y apagado y, según la función, configurar otros parámetros.

Guarde los cambios con el icono de disquete. Las ayudas están disponibles a través del signo de interrogación. Con el icono de ojo se pueden activar las salidas directamente en el modelo para facilitar la asignación.

![](images/image\_025.png)

image74.png

## Doble asignación

Cada salida puede tener doble asignación. Ejemplo:

- Primer nivel: luz de posición y luz de carretera
- Segundo nivel: intermitentes de emergencia

El cambio entre niveles es configurable.

![](images/image\_026.png)

image75.png

 hasta ![](images/image\_027.png)

image77.png

## Menú

|  |  |
| --- | --- |
| **Archivo** | Reconectar sistema, recargar módulos, descartar cambios temporales, guardar y abrir módulos. |
| **Módulos** | Mostrar y cargar todos los módulos. |
| **Configuración del sistema** | Configuración básica del sistema. |
| **Información del dispositivo** | Información sobre módulos, actualizaciones, ajustes de fábrica. |
| **Análisis del sistema** | Autodiagnóstico, prueba de comunicación, búsqueda de módulos dañados. |
| **Asistente para aprender canales** | Ayuda para aprender los canales. |
| **Registro** | Registro de comunicación para la búsqueda de errores. |
| **Asistente de datos en vivo** | Visualización en tiempo real de posiciones de palancas y estados de conmutación. |
| **Asistentes de efectos** | Configuración de efectos de luces giratorias y KnightRider. |
| **Configuración** | Opciones avanzadas, modo experto (advertencia sobre posibles daños). |
| **Información** | Información sobre el ControlPanel e informes de errores. |

## Barra de herramientas

![](images/image\_028.png)

image85.png

- Mostrar pantalla principal
- Reconectar sistema
- Recargar módulos
- Luz apagada / luz de posición / luz de cruce / luz de carretera / faros antiniebla / luz antiniebla trasera encendido/apagado
- Mostrar datos en vivo
- Información del dispositivo
- Configuración del sistema
- Mostrar salida en vivo
- Abrir actualización en vivo

## Datos en vivo

La vista de datos en vivo muestra las posiciones de las palancas y los estados de conmutación en tiempo real. Los canales pueden aprenderse y las funciones activarse o desactivarse.

![](images/image\_029.png)

image86.png

|  |  |
| --- | --- |
| [[IMAGE\_078]] | Cuando los canales están correctamente aprendidos, los puntos azules deben seguir los movimientos de su palanca. Si usa CPPM, IBUS o SBUS, los canales también deben asignarse correctamente. |
| 665544332211 [[IMAGE\_079]] | Aquí se muestran todos los canales tal como se miden realmente. La información de aprendizaje no se tiene en cuenta, es decir, las barras pueden moverse hacia abajo aunque la palanca se mueva hacia arriba.1: Solo se debe cambiar la asignación de canales si se usa CPPM, IBUS o SBUS.2-5: Estos valores se establecen durante el proceso de aprendizaje. 1000 – 2000 y 1500 como posición central son los valores estándar. Los valores pueden ajustarse y guardarse.6: Desplácese hacia la derecha para ver los valores de otros canales (solo relevante para CPPM, IBUS, SBUS) |
|  | El lado derecho de los datos en vivo muestra los estados de conmutación. Algunos pueden establecerse haciendo clic. Los tres grupos funcionales funciones básicas de luz, funciones adicionales y analógico pueden usarse como interruptores en las funciones, por ejemplo, en la función interruptor simple. [[IMAGE\_080]] [[IMAGE\_081]] |

![](images/image\_030.png)

image87.png

Con un aprendizaje correcto, los puntos azules siguen los movimientos de la palanca. Para CPPM, I-BUS o S-BUS, la asignación de canales debe ser correcta.

![](images/image\_031.png)

image88.png

El lado derecho muestra estados de conmutación que pueden cambiarse parcialmente haciendo clic.

![](images/image\_032.png)

image90.png

 ![](images/image\_033.png)

image91.png

## Actualizaciones

Después de conectar, el ControlPanel muestra actualizaciones disponibles para los módulos de bus.

![](images/image\_043.png)

image6.png

Consejos para una actualización segura:

- Actualice solo un módulo a la vez.
- Evite interrupciones de energía.
- Desconecte servos y motores durante la actualización.
- Reinicie el modelo y el ControlPanel en caso de problemas.

![](images/image\_035.png)

image92.png

 ![](images/image\_043.png)

image6.png

Las actualizaciones pueden restablecer los ajustes de fábrica. El ControlPanel guarda automáticamente todas las configuraciones en el disco duro.

![](images/image\_037.png)

image93.png

 ![](images/image\_038.png)

image94.png

 ![](images/image\_039.png)

image95.png

Después de las actualizaciones se muestran todos los módulos. El KLM 4/16 consta del módulo principal con cuatro salidas de servo y la extensión de interruptores integrada con 16 salidas de conmutación.

![](images/image\_040.png)

image73.png

## Información del dispositivo

Muestra información básica sobre los módulos. "Mostrar dispositivo" enciende las primeras tres salidas, útil cuando hay varias expansiones sin asignación de nombres.

Los módulos pueden reiniciarse, restablecerse a ajustes de fábrica o actualizarse.

![](images/image\_041.png)

image96.png

## Análisis del sistema

Ayuda en la búsqueda de errores leyendo información, buscando módulos dañados y realizando pruebas de comunicación.

![](images/image\_042.png)

image97.png

 ![](images/image\_043.png)

image6.png

## Aprender canales

El asistente ayuda a aprender los canales. Configure previamente la asignación correcta para K1 y K2, especialmente al usar pads de control.

![](images/image\_044.png)

image98.png