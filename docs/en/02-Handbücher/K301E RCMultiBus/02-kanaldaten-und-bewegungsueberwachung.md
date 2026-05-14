# Channel Data and Movement Monitoring

Each channel value is stored and can be individually assigned to each servo or motor output. Additionally, the movement of each channel is monitored, from which a bitfield is generated. This bitfield has three dimensions:

- **Direction:** top / bottom
- **Movement Intensity:** full / half
- **Status:** permanent / in memory

| CH | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH1 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| CH2 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| … |  |  |  |  |  |  |  |
| CHx | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |

## Examples of Movement Monitoring

- **Example 1:** Channel 4 is moved to +30% → Flag *CH4 Permanent/Top/Half* is set.
- **Example 2:** Channel 4 is moved back within 0.5 seconds → Flag *CH4 Permanent/Top/Half* is cleared, Flag *CH4 Memory/Top/Half* is set.
- **Example 3:** Channel 1 is moved to -100% → Flag *CH1 Permanent/Bottom/Full* is set.
- **Example 4:** Channel 1 is moved back after one second → Flag *CH1 Permanent/Bottom/Full* is cleared, Flag *CH1 Memory/Bottom/Full* is set.