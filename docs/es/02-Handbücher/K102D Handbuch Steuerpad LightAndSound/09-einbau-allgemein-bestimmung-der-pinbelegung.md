# Instalación general – Determinación de la asignación de pines

## Teoría

La determinación de la posición de los controles en la mayoría de los transmisores remotos se realiza mediante potenciómetros comerciales que funcionan como divisores de tensión clásicos. El principio es sencillo:

- Entre los polos A y B hay una capa de carbono.
- Un contacto móvil (la llamada "raíz") se desplaza a lo largo de esta capa.
- El voltaje medido en la raíz es una parte del voltaje aplicado entre A y B.

Ejemplo: Si hay 5 V entre A y B y la palanca está en el centro, se miden aproximadamente 2,5 V entre A y W y entre W y B. Al mover la palanca, los voltajes cambian en consecuencia.

![](images/image\_010.png)

image11.png

## Práctica – Determinación de la asignación de pines

1. Encienda el transmisor remoto y tome un multímetro.
2. Evite cortocircuitos y tocar otros contactos durante la medición.
3. Verifique que las puntas del multímetro estén conectadas correctamente (negro en COM, rojo en V).
4. Si no está seguro, compruebe la polaridad con una batería.
5. Mida los voltajes entre los pines y anote los valores:

- Pin 1 contra Pin 2
- Pin 1 contra Pin 3
- Pin 2 contra Pin 3

6. El voltaje más alto medido corresponde a la tensión de alimentación (típicamente 3 V, 3,3 V o 5 V).
7. El cable marrón se conecta al polo negativo (masa), el rojo al polo positivo.
8. El cable naranja se conecta al pin restante (raíz).

Ahora pulse el botón superior izquierdo en el pad. Un servo conectado a la salida correspondiente del receptor debería moverse. Si el movimiento es demasiado pequeño, la calibración se puede ajustar más tarde.

Para conexiones de 3 pines con paso de 2,54 mm se puede usar la carcasa de conector suministrada. De lo contrario, el cable con conector hembra puede soldarse y el pad conectarse.