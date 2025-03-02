# Registers 11 and 12: Load EEN and UE

&nbsp;

These two registers record a different approach to compute EEN and UE values: They ask each Load element in the zone if it is “unserved.” The nominal criterion is undervoltage.

&nbsp;

If you set Option=Voltage for an Energymeter object, only the voltage is used. The global options NormVminpu and EmergVminpu are used for this value. If the voltage is between NormVminpu and EmergVminpu, the EEN is proportioned to how far below the NormVminpu it is. If the voltage is less than EmergVminpu, the UE value for the load is computed in proportion to the degee it is below EmergVminpu, continuing on the same slope as the EEN calculation. In multi-phase elements, the lowest phase voltage is used.

&nbsp;

The default behavior (Option=Combined) is to consider both line overload and undervoltage. If a line, or other power delivery element, serving the load is overloaded, the load is considered unserved in the same percentage that the line is overloaded. This actually takes precedence over&nbsp; the voltage criteria, which assumes that any undervoltage is due to the line overload. A line is considered to serve the load if it is between the EnergyMeter and the load. Note that some inaccuracies can occur if the meter zone is not properly defined, such as if loops exist.

***
_Created with the Standard Edition of HelpNDoc: [Save time and frustration with HelpNDoc's WinHelp HLP to CHM conversion feature](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
