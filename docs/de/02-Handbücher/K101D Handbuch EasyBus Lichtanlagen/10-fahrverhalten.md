# Fahrverhalten

## Fahrtenreglertyp

Der KLM 4/16 ist mit allen Fahrtenreglern kompatibel. Für korrekte Brems- und Rückfahrlichtsteuerung muss der Fahrtenreglertyp in den Systemeinstellungen korrekt eingestellt werden:

- **Einfach:** Rückwärtsfahrt beginnt sofort beim Zurückziehen des Knüppels.
- **Bremse getrennt:** Zuerst Bremse, dann Rückwärtsfahrt nach erneutem Zurückziehen.
- **Standard Tempomat:** Für Regler, die direkt von Verzögerung auf Rückwärtsfahrt schalten.
- **Servonaut Tempomat:** Gangknüppel an K1 anschließen, Servoausgang auf „Proportionalfunktion K1“ einstellen.
- **Servonaut Leerlauf:** Wie Servonaut Tempomat, aber mit Leerlaufstellung zwischen Vorwärts und Rückwärts.
- **Servonaut K40:** Brems- und Rückfahrlicht im K40-Stil schalten.
- **Analog Brems-/Rücklicht:** Schaltausgänge des Fahrtenreglers analog einspeisen (siehe Abschnitt 11.4).

## Intelligentes Bremslicht

Das Bremslicht wird bereits bei Verzögerung aktiviert. Empfindlichkeit und Nachleuchtdauer sind in den Systemeinstellungen einstellbar.

## Lenkungstyp

Standardmäßig muss der Blinker manuell eingeschaltet werden und schaltet sich automatisch zurück. Alternativ kann ein automatischer Blinker aktiviert werden, der bei Kurvenfahrt automatisch schaltet. Der „Blinker Schwellwert“ definiert die Aktivierungsschwelle.

## Kurvenlichttyp

Das Verhalten des Kurvenlichts kann über den Parameter „Kurvenlichttyp“ gesteuert werden. Die Optionen sind selbsterklärend.
