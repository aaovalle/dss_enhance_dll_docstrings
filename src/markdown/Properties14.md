# Properties

&nbsp;

The properties, in order, are:

&nbsp;

| bus1 | Name of bus for terminal 1. Node order definitions optional. |
| --- | --- |
| bus2 | Name of bus for terminal 2 |
| Linecode | Name of an existing LineCode object containing impedance definitions. |
| Length | Length multiplier to be applied to the impedance data. |
| Phases | No. of phases. Default = 3. A line has the same number of conductors per terminal as it has phases. Neutrals are not explicitly modeled unless declared as a “phase”, and the impedance matrices must be augmented accordingly. For example, a three-phase line has a 3x3 Z matrix with the neutral reduced, or a 4x4 Z matrix with the neutral retained. |


&nbsp;

**Symmetrical Component Impedance Definition Properties**

&nbsp;

If any of the following properties are used, the Line object primitive Y matrix is computed using the present values of the other symmetrical component line properties. This is the default method. One limitation to using the symmetrical component method is you can’t correctly represent asymmetrical line constructions. Use the matrix properties or the Geometry property to overcome this limitation.

&nbsp;

| R1 | positive-sequence resistance, ohms per unit length. |
| --- | --- |
| X1 | positive-sequence reactance, ohms per unit length. |
| R0 | zero-sequence resistance, ohms per unit length. |
| X0 | zero-sequence reactance, ohms per unit length. |
| C1 | positive-sequence capacitance, nanofarads per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Cmatrix and B1 |
| C0 | zero-sequence capacitance, nanofarads per unit length. |
| B1 | Alternate way to enter C1, microS per unit length. |
| B0 | Alternate way to enter C0, microS per unit length. |
| Normamps | Normal ampacity, amps. |
| Emergamps | Emergency ampacity, amps. Usually the one-hour rating. |
| Faultrate | Number of faults per year per unit length. This is the default for this general line construction. |
| Pctperm | Percent of the faults that become permanent (requiring a line crew to repair and a sustained interruption). |
| Repair | Hours to repair. |
| BaseFreq | Base Frequency at which the impedance values are specified. Default = 60.0 Hz. |


&nbsp;

**Matrix Impedance Definition Properties**

&nbsp;

You may define line impedances in a Line object definition using matrices. If you use any of the following properties and do not supercede it with a symmetrical component property or either a LineCode or Geometry property, the primitive Y matrix is computed assuming you wish to use the quantities defined through the matrix properties below. The default matrix values correspond to the symmetrical component defaults described above. The remain at those values until you change them. Matrix properties allow you great flexibility in modeling all sorts of line asymmetries. If you will be solving at some frequency other than the base frequency, be sure to define Rg and Xg (see LineCode object description).

&nbsp;

| R1 | positive-sequence resistance, ohms per unit length. |
| --- | --- |
| X1 | positive-sequence reactance, ohms per unit length. |
| R0 | zero-sequence resistance, ohms per unit length. |
| X0 | zero-sequence reactance, ohms per unit length. |
| C1 | positive-sequence capacitance, nanofarads per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Cmatrix and B1 |
| C0 | zero-sequence capacitance, nanofarads per unit length. |
| B1 | Alternate way to enter C1, microS per unit length. |
| B0 | Alternate way to enter C0, microS per unit length. |
| Normamps | Normal ampacity, amps. |
| Emergamps | Emergency ampacity, amps. Usually the one-hour rating. |
| Faultrate | Number of faults per year per unit length. This is the default for this general line construction. |
| Pctperm | Percent of the faults that become permanent (requiring a line crew to repair and a sustained interruption). |
| Repair | Hours to repair. |
| BaseFreq | Base Frequency at which the impedance values are specified. Default = 60.0 Hz. |


&nbsp;

**Matrix Impedance Definition Properties**

&nbsp;

You may define line impedances in a Line object definition using matrices. If you use any of the following properties and do not supercede it with a symmetrical component property or either a LineCode or Geometry property, the primitive Y matrix is computed assuming you wish to use the quantities defined through the matrix properties below. The default matrix values correspond to the symmetrical component defaults described above. The remain at those values until you change them. Matrix properties allow you great flexibility in modeling all sorts of line asymmetries. If you will be solving at some frequency other than the base frequency, be sure to define Rg and Xg (see LineCode object description).

&nbsp;

| Rmatrix | Series resistance matrix, ohms per unit length. See Command Language for syntax. Lower triangle form is acceptable. |
| --- | --- |
| Xmatrix | Series reactance matrix, ohms per unit length. |
| Cmatrix | Shunt nodal capacitance matrix, nanofarads per unit length. |
| Switch | {y/n \| T/F} Default= no/false. Designates this line as a switch for graphics and algorithmic purposes. SIDE EFFECT: Sets R1=0.001 X1=0.0. You must reset if you want something different. |
| Rg | Carson earth return resistance per unit length used to compute impedance values at base frequency. For making better frequency adjustments. Applies to line impedances defined using the Line object properties described here or to impedances defined by LineCode objects. Does not apply to impedances defined by Geometry. See explanation in LineCode object. Default values are same as for default LineCode object, which corresponds to the default Line object impedances. Set both Rg and Xg = 0 if you do not wish for earth return correction to be adjusted when the frequency of the solution is different than the base frequency. |
| Xg | Carson earth return reactance per unit length used to compute impedance values at base frequency. For making better frequency adjustments. Applies to line impedances defined using the Line object properties described here or to impedances defined by LineCode objects. Does not apply to impedances defined by Geometry. See explanation in LineCode object. Default values are same as for default LineCode object, which corresponds to the default Line object impedances. Set both Rg and Xg = 0 if you do not wish for earth return correction to be adjusted when the frequency of the solution is different than the base frequency. |
| Rho | Earth resistivity used to compute earth correction factor. Overrides Line geometry definition if specified. Default=100 meter ohms. |
| Geometry | Geometry code for LineGeometry Object. Supercedes any previous definition of line impedance. Line constants are computed for each frequency change or rho change. CAUTION: may cause the number of phases to be redefined. |
| EarthModel | One of {Carson \| FullCarson \| Deri}. Default is the global value established with the Set EarthModel option. See the Options Help on EarthModel option. This is used to override the global value for this line. This option applies only when the "geometry" property is used. |
| Units | Length Units = {none \| mi \| kft \| km \| m \| Ft \| in \| cm } Default is None - assumes length units match impedance units. |
| Seasons | Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property. |
| Ratings | An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert multiple ratings to change during a QSTS simulation to evaluate different ratings in lines. |
| LineType | Code designating the type of line. One of: OH, UG, UG\_TS, UG\_CN, SWT\_LDBRK, SWT\_FUSE, SWT\_SECT, SWT\_REC, SWT\_DISC, SWT\_BRK, SWT\_ELBOW. OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH. |
| EpsRmedium | Default=1.0. Relative Permittivity of the medium. Used by lines with a geometry definition. Defaults to 1.0 for air. |
| HeightOffset | Default=0.0. Average Height (or depth) offset to be applied on top of coordinates of geometry or spacing. Use negative value for depth in underground lines. |
| HeightUnit | Height offset Units = {mi\|kft\|km\|m\|Ft\|in\|cm }. If none is detected, meters is assumed. |
| conductors | Array of conductor names for use in line constants calculation. Must be used in conjunction with the Spacing property. Specify the Spacing first, and "ncond" wires. Specify the conductor type followed by the conductor name.&nbsp; E.g.: &nbsp; conductors=\[cndata.cncablename, tsdata.tscablename, wiredata.wirename\]&nbsp; If a given position in the spacing is not to be used in the line, use "none" in the entry of the conductors array. |
| Like | Name of an existing Line object to build this like. |



***
_Created with the Standard Edition of HelpNDoc: [How to Protect Your PDFs with Encryption and Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
