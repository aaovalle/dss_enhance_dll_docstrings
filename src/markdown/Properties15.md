# Properties

&nbsp;

The properties for the reactor object are as follows:

&nbsp;

| **Property** | **Description** |
| --- | --- |
| *phases* | Number of phases. |
| *bus1* | Name of first bus. Examples:&nbsp; bus1=busname bus1=busname.1.2.3 |
| *bus2* | Name of 2nd bus. Defaults to all phases connected to first bus, node 0. (Shunt Wye Connection) Not necessary to specify for delta (LL) connection |
| *kv* | For 2, 3-phase, kV phase-phase. Otherwise specify actual coil rating. |
| *kvar* | Total kvar, all phases. Evenly divided among phases. Only determines X. Specify R separately |
| *conn* | \={wye \| delta \|LN \|LL} Default is wye, which is equivalent to LN. If Delta, then only one terminal. |
| *Parallel* | {Yes \| No} Default=No. Indicates whether Rmatrix and Xmatrix are to be considered to be in parallel. This makes a significant difference in harmonic studies. Default is series. For other models, specify R and Rp. |
| *R* | Resistance (in series with reactance), each phase, ohms. |
| *Rmatrix* | Resistance matrix, lower triangle, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or R. |
| *Rp* | Resistance in parallel with R and X (the entire branch). Assumed infinite if not specified. |
| *X* | Reactance, each phase, ohms at base frequency. |
| *Xmatrix* | Reactance matrix, lower triangle, ohms at base frequency. Order of the matrix is the number of phases. Mutually exclusive to specifying parameters by kvar or X. |
| *Z* | Alternative way of defining R and X properties. Enter a 2-element array representing R +jX in ohms. Example: Z=\[5 10\] \! equivalent to R=5 X=10 |
| *Z1* | Positive-sequence impedance, ohms, as a 2-element array representing a complex number. Example: Z1=\[1, 2\] \! represents 1 + j2 If defined, Z1, Z2, and Z0 are used to define the impedance matrix of the REACTOR. Z1 MUST BE DEFINED TO USE THIS OPTION FOR DEFINING THE MATRIX. Side Effect: Sets Z2 and Z0 to same values unless they were previously defined. |
| *Z2* | Negative-sequence impedance, ohms, as a 2-element array representing a complex number. Example: Z2=\[1, 2\] \! represents 1 + j2 Used to define the impedance matrix of the REACTOR if Z1 is also specified. Note: Z2 defaults to Z1 if it is not specifically defined. If Z2 is not equal to Z1, the impedance matrix is asymmetrical. |
| *Z0* | Zero-sequence impedance, ohms, as a 2-element array representing a complex number. Example: Z0=\[3, 4\] \! represents 3 + j4 Used to define the impedance matrix of the REACTOR if Z1 is also specified. Note: Z0 defaults to Z1 if it is not specifically defined. |
| *RCurve* | Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency. Applies to resistance specified by R or Z property. If actual values are not known, R often increases by approximately the square root of frequency. |
| *LCurve* | Name of XYCurve object, previously defined, describing per-unit variation of phase inductance, L=X/w, vs. frequency. Applies to reactance specified by X, LmH, Z, or kvar property.L generally decreases somewhat with frequency above the base frequency, approaching a limit at a few kHz. |
| *LmH* | Inductance, mH. Alternate way to define the reactance, X, property |


&nbsp;

Properties inherited from the circuit element class:

&nbsp;

| *normamps* | Normal rated current. |
| --- | --- |
| *emergamps* | Maximum current. |
| *repair* | Hours to repair. |
| *faultrate* | No. of failures per year. |
| *pctperm* | Percent of failures that become permanent. |
| *basefreq* | Base Frequency for ratings. |
| *enabled* | {Yes\|No or True\|False} Indicates whether this element is enabled. |
| *like* | Make like another object, e.g.:&nbsp; New Reactor.R2 like=R1 ... |



***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
