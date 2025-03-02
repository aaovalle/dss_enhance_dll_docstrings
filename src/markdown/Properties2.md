# Properties 

&nbsp;

The properties, in order, are:

&nbsp;

| Element | Name of an existing circuit element to which the monitor is to be connected. Note that there may be more than one circuit element with the same name (not wise, but it is allowed). The monitor will be placed at the first one found in the list. |
| --- | --- |
| Terminal | No. of the terminal to which the monitor will be connected, normally the source end. |
| Action | Optional action to execute. One of |
| Clear | reset all registers to zero |
| Save | Saves (appends) the present register values to a file. File name is MTR\_metername.CSV, where metername is the name of the energy meter. |
| Take | Takes a sample at the present solution. |
| Option | Enter a string ARRAY of any combination of the following. Options processed left-to-right: (E)xcess : (default) UE/EEN is estimate of only energy exceeding capacity (T)otal : UE/EEN is total energy after capacity exceeded. (R)adial : (default) Treats zone as a radial circuit (M)esh : Treats zone as meshed network (not radial). (C)ombined: (default) Load UE or EEN are computed from both overload and undervoltage criteria. (V)oltage: Load UE/EEN are computed only from the undervoltage criteria. Example: option=(E, R, C) |


&nbsp;

In a meshed network, the overload registers represent the total of the power delivery element overloads and the load UE/EEN registers will contain only those loads that are "unserved", which are those with low voltages. In a radial circuit, the overload registers record the max overload (absolute magnitude, not percent) in the zone. Loads become unserved either with low voltage or if any line in their path to the source is overloaded.

&nbsp;

| KWNorm | Upper limit on kW load in the zone, Normal configuration. Default is 0.0 (ignored). If specified, overrides limits on individual lines for overload EEN. KW above this limit for the entire zone is considered EEN. |
| --- | --- |
| KWEmerg | Upper limit on kW load in the zone, Emergency configuration. Default is 0.0 (ignored). If specified, overrides limits on individual lines for overload UE. KW above this limit for the entire zone is considered UE. |
| Peakcurrent | ARRAY of current magnitudes representing the peak currents measured at this location for the load allocation function (for loads defined with xfkva=). Default is (400, 400, 400). Enter one current for each phase. |
| Zonelist | ARRAY of full element names for this meter's zone. Default is for meter to find it's own zone. If specified, DSS uses this list instead. It can access the names in a single-column text file. Examples:&nbsp; zonelist=\[line.L1, transformer.T1, Line.L3\] zonelist=(file=branchlist.txt) |
| LocalOnly | {Yes \| No} Default is NO. If Yes, meter considers only the monitored element for EEN and UE calcs. Uses whole zone for losses. |
| Mask | Mask for adding registers whenever all meters are totalized. Array of floating point numbers representing the multiplier to be used for summing each register from this meter. Default = (1, 1, 1, 1, ... ). You only have to enter as many as are changed (positional). Useful when two meters monitor same energy, etc. |
| Losses | {Yes \| No} Default is YES. Compute Zone losses. If NO, then no losses at all are computed. |
| LineLosses | {Yes \| No} Default is YES. Compute Line losses. If NO, then none of the line losses are computed. |
| XfmrLosses | {Yes \| No} Default is YES. Compute Transformer losses. If NO, transformers are ignored in loss calculations. |
| SeqLosses | {Yes \| No} Default is YES. Compute Sequence losses in lines and segregate by line mode losses and zero mode losses. |
| &#51;PhaseLosses | {Yes \| No} Default is YES. Compute Line losses and segregate by 3-phase and other (1- and 2-phase) line losses. |
| VbaseLosses | {Yes \| No} Default is YES. Compute losses and segregate by voltage base. If NO, then voltage-based tabulation is not reported. Make sure the voltage bases of the buses are assigned BEFORE defining the EnergyMeter to ensure that it will automatically pick up the voltage bases. Or, issue the CalcVoltageBases command after defining the EnergyMeter. Each voltage base has four(4) loss registers: total, line, load, and no-load, respectively. There are sufficient registers to report losses in five (5) different voltage levels. |
| BaseFreq | Base frequency for ratings. |
| Enabled | {Yes\|No or True\|False} Indicates whether the element is enabled. |
| Like | Name of another EnergyMeter object on which to base this one. |


&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Create HTML Help, DOC, PDF and print manuals from 1 single source](<https://www.helpndoc.com/help-authoring-tool>)_
