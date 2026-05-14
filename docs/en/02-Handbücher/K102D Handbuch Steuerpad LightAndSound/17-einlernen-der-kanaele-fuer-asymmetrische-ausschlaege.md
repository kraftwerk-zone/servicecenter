# Learning the Channels for Asymmetric Deflections

This section is only relevant if all previous steps have been carried out correctly and high beam or fog lights show too small or no deflections.

Possible causes:

- Misadjusted center position (trimmer, subtrim)
- Electronic limitation of the channel
- Inexpensive remote control transmitter with nonlinear control curve

![](images/image\_019.png)

image20.png

If possible, reset all settings for the used channel and start the normal learning process again.

If this is not possible, the control for positive and negative deflections must be set separately.

Open the Live Data Assistant and focus on the value marked below (when using K2 on the value to the left). This value changes when pressing a button and should be as close as possible to the following target values:

| Function | Value (µs) |
| --- | --- |
| Center position | 1500 |
| Level button | 1000 \* |
| Parking light | 1070 \*\* |
| Minus button | 2000 \* |
| Saddle coupling | 1930 \*\* |

\* Depending on the remote control transmitter, level button and minus button may be swapped.

\*\* The same applies for parking light and saddle coupling.

The greater the control, the further the values move away from 1500 µs when pressing a button. The deflection of the level button should be as far away as possible, but the deflection for parking light must be clearly different. The same applies for minus button and saddle coupling.

Set the control for both deflections separately:

- Press **Setup+** and **S4** to set the maximum control for the positive deflection.
- Check the values for level button and parking light. If the values are too similar (e.g. 1930 and 1925), reduce the control with **Setup+** and **S3** and check again. The difference should be at least 50 µs.
- Repeat the process for the negative deflection with **Setup-** and the corresponding S-buttons. Check the values for minus button and saddle coupling.

![](images/image\_020.png)

image21.png