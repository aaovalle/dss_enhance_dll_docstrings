# Properties

&nbsp;

Properties:

&nbsp;

| **Property** | **Description** |
| --- | --- |
| phases | Number of phases. Defaults to 3. For 3 or less, phase shift defaults to 120 degrees. |
| bus1 | Name of bus to which source is connected.&nbsp; bus1=busname bus1=busname.1.2.3 |
| amps | Magnitude of current source, each phase, in Amps. |
| angle | Phase angle in degrees of first phase: e.g.,Angle=10.3. Phase shift between phases defaults to 120 degrees when number of phases \<= 3 |
| frequency | Source frequency. Defaults to circuit fundamental frequency. |
| scantype | {pos\*\| zero \| none} Maintain specified sequence for harmonic solution. Default is positive sequence. Otherwise, angle between phases rotates with harmonic. |
| sequence | {pos\*\| neg \| zero} Set the phase angles for the specified symmetrical component sequence for solution modes other than Harmonics. Default is positive sequence. |
| spectrum | Harmonic spectrum assumed for this source. Default is "default". |


&nbsp;

Inherited properties

&nbsp;

| **Property** | **Description** |
| --- | --- |
| basefreq | Base Frequency for ratings. |
| enabled | {Yes\|No or True\|False} Indicates whether this element is enabled. |
| like | Make like another object, e.g.: New Isource.Is2 like=Is1 ... |



***
_Created with the Standard Edition of HelpNDoc: [Make CHM Help File Creation a Breeze with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
