# Fahrverhalten

## Fahrtenreglertyp

Grundsätzlich ist jeder Fahrtenregler mit EasyBus kompatibel. Für korrekte Brems- und Rückfahrlichtsteuerung muss der richtige Fahrtenreglertyp eingestellt werden:

- **Einfach:** Rückwärtsfahrt startet sofort bei Knüppel nach hinten.
- **Bremse getrennt:** Erst Bremse, dann Rückwärtsfahrt nach erneutem Ziehen.
- **Standard Tempomat:** Verzögerung geht direkt in Rückwärtsfahrt über.
- **Servonaut Tempomat:** Gangschaltung über K1, Servoausgang auf „Proportionalfunktion K1“ einstellen.
- **Servonaut Leerlauf:** Wie Servonaut Tempomat, aber mit Leerlaufstellung zwischen Vorwärts und Rückwärts.
- **Servonaut K40:** Brems- und Rückfahrlicht im K40-Stil geschaltet.
- **Analog Brems-/Rücklicht:** Schaltausgänge eines Fahrtenreglers analog einspeisen (siehe Kapitel 11.4).

## Intelligentes Bremslicht

Das Bremslicht schaltet bereits bei Verzögerung, nicht erst bei Rückwärtsfahrt. Sensitivität und Nachleuchtdauer sind in den Systemeinstellungen einstellbar.

## Lenkungstyp

Standardmäßig muss der Blinker manuell eingeschaltet und wird automatisch zurückgestellt. Alternativ kann der „Automatische Blinker“ gewählt werden, der bei Kurvenfahrt automatisch aktiviert wird. Der „Blinker Schwellwert“ definiert die Aktivierungsschwelle.

## Kurvenlichttyp

Das Kurvenlichtverhalten ist über den Parameter „Kurvenlichttyp“ einstellbar. Die Optionen sind selbsterklärend.
