# System Settings

Basic module settings that significantly influence model behavior can be configured here.

![](images/image\_029.png)

image47.png

- **Name:** Module name for identification, especially when using multiple KLB modules.
- **Learning Mode Active:** Enables/disables manual learning mode (throttle and steering sticks to endpoints).
- **Cutoff Voltage:** Default 6.4 V for 7.2 V NiMH/NiCd batteries or 2S LiPo. Set to 9.6 V for 3S LiPo.
- **Model Number:** Switch between up to 3 models.
- **Short/Long Press Threshold:** Defines duration for a press to count as long.
- **Volume:** Initial sound volume; adjusts automatically if controlled via potentiometer or stick.
- **Half Travel Threshold:** Defines the range considered as half travel.
- **Full Travel Threshold:** Defines the range considered as full travel.
- **Infrared Transmission Power:** Set 1 for close LED spacing, 3 for wider spacing.
- **Motor Profile:** Influences start behavior and cruise control.
- **Automatic Motor Start:** Starts motor when throttle stick is slightly moved forward.
- **Motor Stop Delay:** Time in seconds before motor stops after throttle inactivity.
- **Daytime Running Lights Always On:** If unchecked, daytime lights activate only when parking lights are on.
- **Blinker On/Off Durations:** Adjust pulse on/off times to control blink speed.
- **Speed Controller Type:** Currently supports only "Separate Brake".
- **Reverse Driving:** Can link warning and turn signals to reverse lights.
- **Brake Light Sensitivity:** Adjusts sensitivity of intelligent brake light.
- **Brake Light Afterglow:** Controls brake light duration after stopping.
- **Reverse Light Afterglow:** Controls reverse light duration after stopping.
- **Steering Type:** Automatic blinkers or manual operation.
- **Blinker Threshold:** Defines activation and reset points for automatic blinkers.
- **Cornering Light Type:** Always on or only with headlights.
- **Motor Runs Immediately:** Motor runs immediately after power on or requires manual start.
- **Party Mode:** Defines functions activated by the party mode button on the pad.
- **Pad Light & Sound Adjustments:** Fine-tuning of smallest travel ranges for left/right halves of the control pad.
- **Hydraulic RPM Increase:** Defines motor RPM increase when a hydraulic channel is active.
- **Hydraulic Afterrun:** Defines delay after hydraulic channel deactivation.

![](images/image\_030.png)

image48.png

## Channel Assignments K1 – K32

- **None:** Channel not used.
- **Pad Light & Sound:** Used when control pad is connected to this channel.
- **Custom:** User-defined assignments for half/full, short/long travel as memory or direct function.

![](images/image\_031.png)

image49.png

## Possible Settings

![](images/image\_032.png)

image50.png

- RS1 K1 Standard, RS1 K2 Standard, RS1 K3 Standard: Default values for RS1 channels K1-K3.
- Sound Change: Switch between sounds via button press.
- Model Selector: Switch between models; current model must be defined in system settings.
- Standby Switch: Standby mode similar to the physical RS1 switch.
- Volume: Direct volume control via remote control.
- Hydraulics: Triggers motor sound RPM increase.
