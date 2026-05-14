# Driving Behavior

## Speed Controller Type

Basically, every speed controller is compatible with EasyBus. For correct brake and reverse light control, the correct speed controller type must be set:

- **Simple:** Reverse drive starts immediately when the stick is pulled backward.
- **Brake Separate:** Brake first, then reverse drive after pulling again.
- **Standard Cruise Control:** Deceleration transitions directly into reverse drive.
- **Servonaut Cruise Control:** Gear shifting via K1, set servo output to "Proportional function K1".
- **Servonaut Neutral:** Like Servonaut Cruise Control, but with neutral position between forward and reverse.
- **Servonaut K40:** Brake and reverse light switched in K40 style.
- **Analog Brake/Reverse Light:** Switch outputs of a speed controller fed in analog (see chapter 11.4).

## Intelligent Brake Light

The brake light switches already during deceleration, not only during reverse driving. Sensitivity and afterglow duration can be adjusted in the system settings.

## Steering Type

By default, the turn signal must be switched on manually and is automatically reset. Alternatively, the "Automatic Turn Signal" can be selected, which is automatically activated during cornering. The "Turn Signal Threshold" defines the activation threshold.

## Cornering Light Type

The cornering light behavior can be set via the parameter "Cornering Light Type". The options are self-explanatory.