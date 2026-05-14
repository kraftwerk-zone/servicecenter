# Aprendizaje de los canales para oscilaciones asimétricas

Esta sección solo es relevante si todos los pasos anteriores se han realizado correctamente y las luces largas o los faros antiniebla muestran oscilaciones demasiado pequeñas o ninguna.

Posibles causas:

- Posición central desajustada (trimmer, subtrim)
- Limitación electrónica del canal
- Emisor de radio económico con curva de control no lineal

![](images/image\_019.png)

image20.png

Si es posible, restablezca todos los ajustes para el canal utilizado y reinicie el proceso normal de aprendizaje.

Si esto no es posible, la modulación para oscilaciones positivas y negativas debe ajustarse por separado.

Abra el asistente de datos en vivo y concéntrese en el valor marcado a continuación (al usar K2, en el valor a la izquierda). Este valor cambia al presionar el botón y debe estar lo más cerca posible de los siguientes valores objetivo:

| Función | Valor (µs) |
| --- | --- |
| Posición central | 1500 |
| Botón plano | 1000 \* |
| Luz de posición | 1070 \*\* |
| Botón menos | 2000 \* |
| Acoplamiento de silla | 1930 \*\* |

\* Dependiendo del emisor de radio, el botón plano y el botón menos pueden estar intercambiados.

\*\* Lo mismo aplica para la luz de posición y el acoplamiento de silla.

Cuanto mayor sea la modulación, más se alejan los valores de 1500 µs al presionar el botón. La oscilación del botón plano debe estar lo más alejada posible, pero la oscilación para la luz de posición debe diferenciarse claramente. Lo mismo aplica para el botón menos y el acoplamiento de silla.

Ajuste la modulación para ambas oscilaciones por separado:

- Presione **Setup+** y **S4** para ajustar la modulación máxima para la oscilación positiva.
- Verifique los valores para el botón plano y la luz de posición. Si los valores son demasiado similares (por ejemplo, 1930 y 1925), reduzca la modulación con **Setup+** y **S3** y verifique nuevamente. La diferencia debe ser al menos de 50 µs.
- Repita el proceso para la oscilación negativa con **Setup-** y los botones S correspondientes. Verifique los valores para el botón menos y el acoplamiento de silla.

![](images/image\_020.png)

image21.png