# Einbau allgemein – Bestimmung der Pinbelegung

## Theorie

Die Positionsbestimmung der Steuergeber in den meisten Fernsteuersendern erfolgt über handelsübliche Potentiometer, die als klassische Spannungsteiler arbeiten. Das Prinzip ist einfach:

- Zwischen den Polen A und B befindet sich eine Kohleschicht.
- Ein beweglicher Kontakt (die sogenannte „Wurzel“) verschiebt sich entlang dieser Schicht.
- Die gemessene Spannung an der Wurzel ist ein Teil der an A und B angelegten Spannung.

Beispiel: Liegen zwischen A und B 5 V an und der Knüppel steht in der Mitte, messen Sie zwischen A und W sowie zwischen W und B jeweils ca. 2,5 V. Bewegt sich der Knüppel, ändern sich die Spannungen entsprechend.

![](images/image\_010.png)

image11.png

## Praxis – Bestimmung der Pinbelegung

1. Schalten Sie den Fernsteuersender ein und nehmen Sie ein Multimeter zur Hand.
2. Vermeiden Sie Kurzschlüsse und Berührungen anderer Kontakte während der Messung.
3. Kontrollieren Sie, ob die Messleitungen des Multimeters korrekt angeschlossen sind (Schwarz an COM, Rot an V).
4. Falls unsicher, prüfen Sie die Polarität mit einer Batterie.
5. Messen Sie die Spannungen zwischen den Pins und notieren Sie die Werte:

- Pin 1 gegen Pin 2
- Pin 1 gegen Pin 3
- Pin 2 gegen Pin 3

6. Die größte gemessene Spannung entspricht der Versorgungsspannung (typisch 3 V, 3,3 V oder 5 V).
7. Das braune Kabel wird an den Minuspol (Masse), das rote an den Pluspol angeschlossen.
8. Das orange Kabel wird an den verbleibenden Pin (Wurzel) angeschlossen.

Betätigen Sie nun die linke obere Taste am Pad. Ein an den entsprechenden Empfängerausgang angeschlossenes Servo sollte ausschlagen. Ist der Ausschlag zu klein, kann später die Aussteuerung angepasst werden.

Für 3-polige Anschlüsse im 2,54 mm Rastermaß kann das mitgelieferte Steckergehäuse verwendet werden. Andernfalls kann das Buchsenkabel verlötet und das Pad gesteckt werden.
