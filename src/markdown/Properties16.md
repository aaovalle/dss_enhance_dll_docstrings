# Properties

&nbsp;

Properties, in order, are:

&nbsp;

| Phases | Number of phases. Default is 3. |
| --- | --- |
| Windings | Number of windings. Default is 2. |


&nbsp;

For defining the winding values one winding at a time, use the following parameters. Always start the winding definition with "wdg = …" when using this method of defining transformer parameters. The remainder of the tags are optional as usual if you keep them in order.

&nbsp;

| Wdg | Integer representing the winding which will become the active winding for subsequent data. |
| --- | --- |
| Bus | Definition for the connection of this winding (each winding is connected to one terminal of the transformer and, hence, to one bus). |
| Conn | Connection of this winding. One of {wye \| ln} for wye connected banks or {delta \| ll} for delta (line-line) connected banks. Default is wye. |
| Kv | Rated voltage of this winding, kV. For transformers designated 2- or 3-phase, enter phase-to-phase kV. For all other designations, enter actual winding kV rating. Two-phase transfomers are assumed to be employed in a 3-phase system. Default is 12.47 kV. |
| Kva | Base kVA rating (OA rating) of this winding. |
| Tap | Per unit tap on which this winding is set. |
| %R | Percent resistance of this winding on the rated kVA base. (Reactance is between two windings and is specified separately -- see below.) |
| rneut | Neutral resistance to ground in ohms for this winding. Ignored if delta winding. For open ungrounded neutral, set to a negative number. Default is –1 (capable of being ungrounded). The DSS defaults to connecting the neutral to node 0 at a bus, so it will still be ground when the system Y is built. To make the neutral floating, explicitly connect it to an unused node at the bus, e.g., Bus=Busname.1.2.3.4, when node 4 will be the explicit neutral node. |
| xneut | Neutral reactance in ohms for this winding. Ignored if delta winding. Assumed to be in series with neutral resistance. Default is 0. |


&nbsp;

Use the following properties to set the winding values using arrays (setting of wdg= … is ignored). The names of these properties are simply the plural form of the property name above.

&nbsp;

| Buses | Array of bus definitions for windings \[1, 2. …\]. |
| --- | --- |
| Conns | Array of winding connections for windings \[1, 2. …\]. |
| KVs | Array of kV ratings following rules stated above for the kV field for windings \[1,2,…\]. |
| KVAs | Array of base kVA ratings for windings \[1,2,…\]. |
| Taps | Array of per unit taps for windings \[1,2,…\]. |
| %Rs | Array of percent resistances for windings \[1, 2. …\] |


&nbsp;

Use the following propertis to define the reactances of the transformer. For 2- and 3-winding transformers, you may use the conventional XHL, XLT, and XHT (or X12, X23, X13) parameters. You may also put the values in an array (xscarray), which is required for higher phase order transformers. There are always n\*(n-1)/2 different short circuit reactances, where n is the number of windings. Always use the kVA base of the first winding for entering impedances. Impedance values are entered in percent.

&nbsp;

| XHL (or X12) | Percent reactance high-to-low (winding 1 to winding 2). |
| --- | --- |
| XLT (or X23) | Percent reactance low-to-tertiary (winding 2 to winding 3). |
| XHT (or X13) | Percent reactance high-to-tertiary (winding 1 to winding 3). |
| XscArray | Array of n\*(n-1)/2 short circuit reactances in percent on the first winding's kVA base. "n" is number of windings. Order is (12, 13, 14, …1n, 23, 24, … 34, …) |


&nbsp;

General transformer rating data:

&nbsp;

| Thermal | Thermal time constant, hrs. Default is 2. |
| --- | --- |
| n | Thermal exponent, n, from IEEE/ANSI C57. Default is 0.8. |
| m | Thermal exponent, m, from IEEE/ANSI C57. Default is 0.8. |
| flrise | Full-load temperature rise, degrees centigrade. Default is 65. |
| hsrise | Hot-spot temperatire rise, degrees centigrade. Default is 15. |
| %Loadloss | Percent Losses at rated load.. Causes the %r values to be set for windings 1 and 2. |
| %Noloadloss | Percent No load losses at nominal voltage. Default is 0. Causes a resistive branch to be added in parallel with the magnetizing inductance. |
| %imag | Percent magnetizing current. Default is 0. An inductance is used to represent the magnetizing current. This is embedded within the transformer model as the primitive Y matrix is being computed. |
| Ppm\_Antifloat | Parts per million (PPM) for anti floating reactance to be connected from each terminal to ground. Default is 1. That is, the diagonal of the primitive Y matrix is increased by an amount equal to rated kVA/1.0e6. Prevents a singular matrix if delta winding left floating. Zig-Zag transformers are also susceptible to this. Set this to zero if you don’t need it and the resulting impedance to ground is affecting the results. Is inconsequential for most cases. Can be negative to represent capacitive ground, if you prefer (but you can create unintentional resonances at very high frequencies.) |
| NormHKVA | Normal maximum kVA rating for H winding (1). Usually 100 - 110% of maximum nameplate rating. |
| EmergHKVA | Emergency maximum kVA rating for H winding (1). Usually 140 - 150% of maximum nameplate rating. This is the amount of loading that will cause 1% loss of life in one day. |
| Sub | Yes/No. Flag that designates whether this transformer is to be treated as a substation. Default is No. Allows substations to show up differently on circuit plots. |
| MaxTap | Max per unit tap for the active winding. Default is 1.10 |
| MinTap | Min per unit tap for the active winding. Default is 0.90 |
| NumTaps | Total number of taps between min and max tap. Default is 32 (16 raise and 16 lower taps about the neutral position). The neutral position is not counted. |
| SubName | Substation Name. Optional. Default is null. If specified, printed on plots |
| Bank | Name of the bank this transformer is part of, for CIM, MultiSpeak, and other industry database interfaces. |
| XfmrCode | Name of a library entry of the XfmrCode class for transformer properties. The named XfmrCode must already be defined. You can use this instead of the properties of the same name in the Transformer class. |
| XRConst | {Yes\|No\*} Default is NO. Signifies whether or not the X/R is assumed contant for harmonic studies, a common assumption. Note: You may also insert a frequency-dependent Reactor object in series with the transformer to impart frequency-dependent characteristics. |
| LeadLag | {Lead \| Lag (default) \| ANSI (default) \| Euro } Designation in mixed Delta-wye connections signifying the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro". |
| Seasons | Defines the number of ratings to be defined for the transformer, to be used only when defining seasonal ratings using the "Ratings" property. |
| Ratings | An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert multiple ratings to change during a QSTS simulation to evaluate different ratings in transformers. Is given in kVA. |


&nbsp;

Inherited Properties:

&nbsp;

| FaultRate | Failure rate for transformer. Defaults to 0.007 per year. All are considered permanent. |
| --- | --- |
| Basefreq | Base frequency, Hz. Default is 60.0 |
| Like | Name of another Transformer object on which to base this one. |


&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Don't Let Unauthorized Users View Your PDFs: Learn How to Set Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
