# Properties

&nbsp;

&nbsp;

The properties, in numerical order, are:

&nbsp;

| **Property** | **Description** |
| --- | --- |
| *bus1* | Name of bus to which the generator is connected. Include node definitions if the terminal conductors are connected unusually. 3-phase Wye-connected generators have 4 conductors; Delta-connected have 3. Wye-connected generators, in general, have one more conductor than phases. 1-phase Delta has 2 conductors; 2-phase has 3. The remaining Delta, or line-line, connections have the same number of conductors as phases. |
| *Phases* | No. of phases this generator. |
| *Kv* | Base voltage for generator. For 2- or 3-phase generators, specified in phase-to-phase kV. For all other generators, the actual kV across the generator branch. If wye (star) connected, specify the phase-to-neutral (L-N) kV. If delta or phase-to-phase connected, specify the phase-to-phase (L-L) kV. |
| *Kw* | nominal kW for generator. Total of all phases. |
| *Pf* | nominal Power Factor for generator. Negative PF is leading (absorbing vars). Specify either PF or kvar (see below). If both are specified, the last one specified takes precedence. |
| *Model* | Integer defining how the generator will vary with voltage. Presently defined models are: 1: Generator injects a constant kW at specified power factor. 2: Generator is modeled as a constant admittance. 3: Const kW, constant kV. Somewhat like a conventional transmission power flow P-V generator. 4: Const kW, Fixed Q (Q never varies) 5: Const kW, Fixed Q(as a constant reactance) 6: Compute load injection from User-written Model.(see usage of Xd, Xdp) 7: Constant kW, kvar, but current is limited when voltage is below Vminpu |
| *Yearly* | Name of Yearly load shape. |
| *Daily* | Name of Daily load shape. |
| *Duty* | name of Duty cycle load shape. Defaults to Daily load shape if not defined. |
| *Dispvalue* | Dispatch value. If = 0.0 then Generator follows dispatch curves. If \> 0 then Generator is ON only when the global load multiplier exceeds this value. Then the generatorfollows dispatch curves (see also Status) |
| *Conn* | {wye \| y \| LN} for Wye (Line-Neutral) connection; {delta \| LL} for Delta (Line-Line) connection. Default = wye. |
| *Kvar* | Base kvar. If this is specified, will supercede PF. (see PF) |
| *Rneut* | Neutral resistance ohms. If entered as negative, non-zero number, neutral is assumed open, or ungrounded. Ignored for delta or line-line connected generators. Default is 0. |
| *Xneut* | Neutral reactance, ohms. Ignored for delta or line-line connected generators. Assumed to be in series with Rneut value. |
| *Status* | {fixed \| variable}. If Fixed, then dispatch multipliers do not apply. The generator is always at full power when it is ON. Default is Variable (follows curves). |
| *Class* | Integer number segregating the generator according to a particular user-defined class. Can be any number. |
| *Maxkvar* | Maximum kvar limit for Model = 3. Defaults to twice the specified load kvar. Always reset this if you change PF or kvar properties. |
| *Minkvar* | Minimum kvar limit for Model = 3. Enter a negative number if generator can absorb vars. Defaults to negative of Maxkvar. Always reset this if you change PF or kvar properties. |
| *Pvfactor* | Convergence deceleration factor for P-V generator model (Model=3). Default is 0.1. If the circuit converges easily, you may want to use a higher number such as 1.0. Use a lower number if solution diverges. Use Debugtrace=yes to create a file that will trace the convergence of a generator model. |
| *Debugtrace* | {Yes \| No } Default is no. Turn this on to capture the progress of the generator model for each iteration. Creates a separate file for each generator named "GEN\_name.CSV". |
| *Vminpu* | Default = 0.95. Minimum per unit voltage for which the Model is assumed to apply. Below this value, the generator model reverts to a constant impedance model. For Model 7, this is used to determine the upper current limit. For example, if Vminpu is 0.90 then the current limit is (1/0.90) = 111%. |
| *Vmaxpu* | Default = 1.05. Maximum per unit voltage for which the Model is assumed to apply. Above this value, the generator model reverts to a constant impedance model. |
| *ForceON* | {Yes \| No} Forces generator ON despite requirements of other dispatch modes. Stays ON until this property is set to NO, or an internal algorithm cancels the forced ON state. |
| *kVA* | kVA rating of electrical machine. Defaults to 1.2\* kW if not specified. Applied to machine or inverter definition for Dynamics mode solutions. |
| *MVA* | MVA rating of electrical machine. Alternative to using kVA=. |
| *Xd* | Per unit synchronous reactance of machine. Presently used only for Thevenin impedance for power flow calcs of user models (model=6). Typically use a value from 0.4 to 1.0. Default is 1.0 |
| *Xdp* | Per unit transient reactance of the machine. Used for Dynamics mode and Fault studies. Default is 0.27.For user models, this value is used for the Thevenin/Norton impedance for Dynamics Mode. |
| *Xdpp* | Per unit subtransient reactance of the machine. Used for Harmonics. Default is 0.20. |
| *H* | Per unit mass constant of the machine. MW-sec/MVA. Default is 1.0. |
| *D* | Damping constant. Usual range is 0 to 4. Default is 1.0. Adjust to get damping |
| *UserModel* | Name of DLL containing user-written model, which computes the terminal currents for Dynamics studies, overriding the default model. Set to "none" to negate previous setting. |
| *UserData* | String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model. |
| *ShaftModel* | Name of user-written DLL containing a Shaft model, which models the prime mover and determines the power on the shaft for Dynamics studies. Models additional mass elements other than the single-mass model in the DSS default model. Set to "none" to negate previous setting. |
| *ShaftData* | String (in quotes or parentheses) that gets passed to user-written shaft dynamic model for defining the data for that model. |
| *DutyStart* | Starting time offset \[hours\] into the duty cycle shape for this generator, defaults to 0. |
| *Balanced* | {Yes \| No\*} Default is No. For Model=7, force balanced current only for 3-phase generators. Force zero- and negative-sequence to zero. |
| *XRdp* | Default is 20. X/R ratio for Xdp property for FaultStudy and Dynamic modes. Required to match published textbook fault study cases that have generators with both R and X specified. |


&nbsp;

&nbsp;

Inherited Properties

&nbsp;

| *spectrum* | Name of harmonic voltage or current spectrum for this generator. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts. |
| --- | --- |
| *Basefreq* | Base frequency for which this generator is defined. Default is 60.0 |
| *Like* | Name of another Generator object on which to base this one |



***
_Created with the Standard Edition of HelpNDoc: [Converting Word Documents to eBooks: A Step-by-Step Guide with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
