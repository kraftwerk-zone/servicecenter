# ControlPanel

## General

When starting the ControlPanel, the model must be operational: battery charged and connected, model and remote control switched on and bound, servos movable.

The system is automatically detected and all modules are displayed.

![](images/image\_023.png)

image72.png

 ![](images/image\_040.png)

image73.png

## Module Overview

By clicking on a module, you reach the output overview. There you can assign names, set on and off speeds, and configure additional parameters depending on the function.

Save changes with the floppy disk icon. Help is available via the question mark. With the eye icon, outputs on the model can be activated directly to facilitate assignment.

![](images/image\_025.png)

image74.png

## Dual Assignment

Each output can be assigned twice. Example:

- First level: parking light & high beam
- Second level: hazard warning lights

Switching between levels is configurable.

![](images/image\_026.png)

image75.png

 to ![](images/image\_027.png)

image77.png

## Menu

|  |  |
| --- | --- |
| **File** | Reconnect system, reload modules, discard temporary changes, save and open modules. |
| **Modules** | Show and load all modules. |
| **System Settings** | Basic system configuration. |
| **Device Information** | Information about modules, updates, factory settings. |
| **System Analysis** | Self-test, communication test, search for damaged modules. |
| **Channel Learning Assistant** | Supports channel learning. |
| **Logging** | Communication log for troubleshooting. |
| **Live Data Assistant** | Real-time display of stick positions and switch states. |
| **Effect Assistants** | Configuration of rotating beacon and KnightRider effects. |
| **Settings** | Advanced options, expert mode (warning about possible damage). |
| **Info** | Information about the ControlPanel and error reports. |

## Toolbar

![](images/image\_028.png)

image85.png

- Show main screen
- Reconnect system
- Reload modules
- Light Off / Parking Light / Low Beam / High Beam / Fog Lights / Rear Fog Light On/Off
- Show live data
- Device information
- System settings
- Show live output
- Open live update

## Live Data

The live data view shows stick positions and switch states in real time. Channels can be learned and functions switched on or off.

![](images/image\_029.png)

image86.png

|  |  |
| --- | --- |
| [[IMAGE\_078]] | When the channels are learned correctly, the blue dots must follow your stick movements. If you use CPPM, IBUS, or SBUS, the channels must also be assigned correctly. |
| 665544332211 [[IMAGE\_079]] | All channels are displayed here as actually measured. The learning information is not considered here, i.e., the bars can move down even if the stick is moved up. 1: A change of channel assignment should only be done if CPPM, IBUS, or SBUS is used. 2-5: These values are set by the learning process. 1000 – 2000 and 1500 center position are the standard values. The values can be adjusted and saved. 6: Scroll right to see the values for other channels (only relevant for CPPM, IBUS, SBUS) |
|  | The right side of the live data shows the switch states. Some can be set by clicking. The three function groups basic light functions, additional functions, and analog can be used as switches in the functions, e.g., in the simple switch function. [[IMAGE\_080]] [[IMAGE\_081]] |

![](images/image\_030.png)

image87.png

With correct learning, the blue dots follow the stick movements. For CPPM, I-BUS, or S-BUS, the channel assignment must be correct.

![](images/image\_031.png)

image88.png

The right side shows switch states, some of which can be changed by clicking.

![](images/image\_032.png)

image90.png

 ![](images/image\_033.png)

image91.png

## Updates

After connecting, the ControlPanel shows available updates for bus modules.

![](images/image\_043.png)

image6.png

Tips for a safe update:

- Update only one module at a time.
- Avoid power interruptions.
- Disconnect servos and motors during the update.
- Restart model and ControlPanel if problems occur.

![](images/image\_035.png)

image92.png

 ![](images/image\_043.png)

image6.png

Updates can reset factory settings. The ControlPanel automatically backs up all settings on the hard drive.

![](images/image\_037.png)

image93.png

 ![](images/image\_038.png)

image94.png

 ![](images/image\_039.png)

image95.png

After updates, all modules are displayed. The KLM 4/16 consists of the main module with four servo outputs and the integrated switch extension with 16 switch outputs.

![](images/image\_040.png)

image73.png

## Device Information

Displays basic information about modules. "Show Device" switches on the first three outputs, helpful with multiple extensions without name assignment.

Modules can be restarted, reset to factory settings, or updated.

![](images/image\_041.png)

image96.png

## System Analysis

Helps with troubleshooting by reading out information, searching for damaged modules, and communication tests.

![](images/image\_042.png)

image97.png

 ![](images/image\_043.png)

image6.png

## Channel Learning

The assistant supports channel learning. Set the correct assignment for K1 and K2 beforehand, especially when using control pads.

![](images/image\_044.png)

image98.png