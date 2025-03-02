# Monitor

\
A monitor is a benign circuit element that is connected to a terminal of another circuit element. It takes a sample when instructed, recording the time and the complex values of voltage and current, or power, at all phases. Other quantities may be saved depending on the setting of the Mode property. The data are saved in a file stream (a separate one for each monitor) at the conclusion of each step of a multistep solution (e.g., daily or yearly, or harmonics) or each solution in a Monte Carlo calculation. In essence, it works like a real power monitor. The data in the file may be converted to CSV form and, for example, brought into Excel. You may accomplish this by either the Show Monitor command or the Export Monitor command.

&nbsp;

For Monte Carlo runs, the hour is set to the number of the solution and seconds is set to zero. For Harmonic solutions, the first two fields are changed to Frequency and Harmonic.

&nbsp;

Monitors may be connected to both power delivery elements and power conversion elements.

&nbsp;

Parameters, in order, are:

&nbsp;

| Element | Name of an existing circuit element to which the monitor is to be connected. Note that there may be more than one circuit element with the same name (not wise, but it is allowed). The monitor will be placed at the first one found in the list. |
| --- | --- |
| Terminal | No. of the terminal to which the monitor will be connected. |
| Mode | Integer bitmask code to describe what it is that the monitor will save. Monitors can generally save two basic types of quantities: 1) Voltage and current; 2) Power. Can also save other selected quantities as defined below. The Mode codes are defined as follows:&nbsp; 0: Standard mode - V and I, each phase, complex&nbsp; 1: Power each phase, complex (kw and kvars)&nbsp; 2: Transformer taps (connect Monitor to a transformer winding)&nbsp; 3: State variables (connect Montor to a PCElement)&nbsp; 4: Flicker level and severity index (Pst) for voltages. No adders apply. Flicker level at simulation time step, Pst at 10-minute time step.&nbsp; 5: Solution variables (Iterations, etc). Normally, these would be actual phasor quantities from solution.&nbsp; 6: Capacitor Switching (connect Monitor to a capacitor, this mode records all the steps defined for the capacitor in separate channels)&nbsp; 7: Storage state variables (Storage devices only). Variables include kWhstored (SOC), kW, kvar, kWlosses, inverter losses, idling losses, efficiency, etc. Name of the variable is in the header for the channel, which may be retrieved in the Show command or through Header property of the COM interface.&nbsp; 8: All Transformer winding currents (Transformer or AutoTransformer elements). Useful for getting delta winding currents rather than the usual terminal currents.&nbsp; 9: Losses (watts, vars) of the monitored element.&nbsp; 10: All Transformer winding voltages (Transformer or AutoTransformer elements). Useful for getting voltages across actual windings rather than just the node voltages.&nbsp; Normally, the values would be actual phasor quantities, but for many modes, the mode number can be combined with the adders below to obtain other quantities.&nbsp; 11: All terminal node voltages and line currents of monitored device.&nbsp; +16: Sequence components: V012, I012&nbsp; +32: Magnitude only&nbsp; +64: Pos Seq only or Average of phases, if not 3 phases&nbsp; For example, Mode=33 will save the magnitude of the power (kVA) only in each phase. Mode=112 saves Positive sequence voltages and currents, magnitudes only. |
| Action | {clear \| save} parsing of this property forces clearing of the monitor's buffer, or saving to disk. |


&nbsp;

The name of the file created appears in the Result window.

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly bring your documentation online with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
