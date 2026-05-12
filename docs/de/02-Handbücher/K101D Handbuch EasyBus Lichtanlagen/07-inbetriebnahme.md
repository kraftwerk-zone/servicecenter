# Inbetriebnahme

Für die Inbetriebnahme der KraftwerK EasyBus Systeme sind keine speziellen Schritte erforderlich. Dennoch empfehlen wir, die folgende Checkliste zu beachten:

## Anschluss an den Empfänger

![](images/image\_052.png)

image6.png

Vor dem Anschluss des KLM 4/16 an den Empfänger überprüfen Sie bitte die Belegung der Empfängerausgänge. Verwenden Sie dazu ein Servo, um jeden Ausgang auf korrekte Funktion zu testen, und notieren Sie die Belegung.

![](images/image\_007.jpg)

image7.jpeg

**Hinweis:** Es empfiehlt sich, das Modell aufzubocken, um ein unbeabsichtigtes Losfahren zu verhindern.

Schließen Sie die Servokabel für Lenkung und Gas an die entsprechenden Empfängerausgänge an. Fahrtenregler und Lenkservo werden an die Servoausgänge des KLM angeschlossen. Die Kanäle K1 und K2 können optional verwendet werden.

**Tipp:** Der Anschluss von Gas- und/oder Lenkungskanal kann entfallen, wenn Brems-, Rückfahrlicht und/oder Blinker analog eingespeist werden (siehe Abschnitt 11.5 „Actros 3363 Brems-/Rückfahrlicht und Blinker vom Fahrtenregler“).

**Tipp:** Alternativ können Fahrtenregler und/oder Lenkservo auch mit einem Y-Kabel direkt an den Empfänger angeschlossen werden, um Störungen durch den KLM zu vermeiden.

## Anschluss der Beleuchtungsplatinen

Alle Erweiterungs- oder Beleuchtungsplatinen können direkt oder über Verteilerplatinen an die Busausgänge des Lichtassistenten angeschlossen werden.

## Einlernen der Kanäle

![](images/image\_052.png)

image6.png

Das Einlernen der Kanäle ist entscheidend für den ordnungsgemäßen Betrieb der KraftwerK EasyBus Anlagen. Nach jeder Änderung an der Fernsteueranlage (z.B. Ausschläge, Drehrichtungen, Mittelstellungen) müssen die Kanäle neu eingelernt werden.

Servos und Motoren, die von KraftwerK Anlagen gesteuert werden, sollten über das ControlPanel angepasst werden. Vermeiden Sie das Einlernen über das Menü Ihrer Fernsteueranlage.

1. Fernsteuerung einschalten und Modell aufbocken, sodass keine Antriebsräder den Boden berühren.
2. Modell einschalten. Nach dem doppelten Blinken der grünen LED bringen Sie Gas- und Lenkungskanal für 5 Sekunden in den Endausschlag, bis die rote LED für ca. 1 Sekunde leuchtet.
3. Knüppel wieder in Mittelstellung bringen.

Die rote LED signalisiert mit unterschiedlicher Anzahl von Blinkern, welcher Kanal eingelernt wird:

- 1x kurz: Gasknüppel – Vollausschlag Gas, dann Vollausschlag Bremse
- 2x kurz: Lenkknüppel – Vollausschlag links, dann rechts
- 3x kurz: Zusatzkanal K1 – Vollausschlag links, dann rechts
- 4x kurz: Zusatzkanal K2 – Vollausschlag oben, dann unten

Nach Rückkehr aller Knüppel in die Mittelstellung leuchtet die rote LED dauerhaft und signalisiert das Ende des Lernvorgangs. Das System startet automatisch neu und zeigt mit dem doppelten Blinken der grünen LED die Betriebsbereitschaft an.
