# Solución de problemas

## El pad activa funciones de forma poco fiable o incorrecta

Primero, verifique que el KLM esté configurado correctamente. Abra la configuración del sistema y controle las entradas "Asignación K1" y "Asignación K2".

Presione las teclas en el siguiente orden y compruebe si los valores disminuyen en un 14,5 % cada vez, comenzando desde arriba a la izquierda con 100, 85,5, 71, 56,5, 42, 27,5 % o desde arriba a la derecha con -100, -85,5, -71, -56,5, -42, -27,5 %.

![](images/image\_018.png)

image18.png

Si alguno de los segundos valores (85,5 % / -85,5 %) es mayor que 90 % / -90 %, la señal está demasiado alta. Si alguno de los segundos valores (30 % / -30 %) es menor que 15 %, siga por favor la sección 5.11.

Además, introduzca los valores porcentuales para las luces largas y los faros antiniebla en la configuración del sistema del KLM (véase el capítulo 5.9).

## El pad está conectado, pero no se mueve ningún valor en los LiveData

Verifique que el pad esté conectado correctamente y que se esté utilizando la salida del receptor correcta. Un servo conectado directamente debería moverse al pulsar una tecla.