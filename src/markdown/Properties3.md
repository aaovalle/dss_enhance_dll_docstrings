# Properties

The properties associated to the wind turbine generator in OpenDSS, called WindGen object, are shown in [Table 1](<OpenDSSDocumentation.md#\_Ref162280291>).

&nbsp;

Table 1. Properties for declaring the WinGen Object in OpenDSS

&nbsp;

|  |  | **Property** | **Description** |
| --- | --- | --- | --- |
|  |  | *Ag* | Gearbox ratio (Default 1/90) |
|  |  | *APCFlg* | &#49; to enable active power control. Use it for dynamic simulations. |
|  |  | *Basefreq* | Base Frequency for ratings. |
|  |  | *Bus1* | Bus to which the WindGen is connected.&nbsp; May include specific node specification. |
|  |  | *Class* | An arbitrary integer number representing the class of WindGen so that WindGen values may be segregated by class. |
|  |  | *Conn* | (wye\|LN\|delta\|LL).&nbsp; Connection mode to the grid. Default is wye. |
|  |  | *Cp* | Turbine performance coefficient (deafult 0.41) |
|  |  | *Daily* | Wind speed shape to use for daily-mode simulations.&nbsp; Must be previously defined as a Loadshape object. If this is not specified, a constant value is assumed (no variation). Set to NONE to reset to no load shape. Nominally for 24 simulations.&nbsp; If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated. |
|  |  | *debugtrace* | (Yes \| No )&nbsp; Default is no.&nbsp; Turn this on to capture the progress of the WindGen model for each iteration.&nbsp; Creates a separate file for each WindGen named "GEN\_name.CSV". |
|  |  | *Delt0* | User defined internal simulation step. Use it for dynamic simulations. |
|  |  | *Duty* | Load shape to use for duty cycle wind speed simulations such as for wind or solar generation. Must be previously defined as a Loadshape object. Typically, it would be time intervals less than 1 hr -- perhaps, in seconds. Set to NONE to reset to no loadshape. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat. |
|  |  | *DutyStart* | Starting time offset \[hours\] into the duty cycle shape for this WindGen, defaults to 0 |
|  |  | *DynamicEq* | The name of the dynamic equation (DinamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation. |
|  |  | *DynOut* | The name of the variables within the Dynamic equation that will be used to govern the generator dynamics.This generator model requires 2 outputs from the dynamic equation:1. Shaft speed (velocity) relative to synchronous speed.2. Shaft, or power, angle (relative to synchronous reference frame). The output variables need to be defined in the same order.&nbsp; |
|  |  | *enabled* | (Yes\|No or True\|False) Indicates whether this element is enabled. |
|  |  | *kV* | Nominal rated (1.0 per unit) voltage, kV, for WindGen. For 2- and 3-phase WindGens, specify phase-phase kV. Otherwise, for phases=1 or phases\>3, specify actual kV across each branch of the WindGen. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV. |
|  |  | *kVA* | kVA rating of electrical machine. Defaults to 1.2\* kW if not specified. Applied to machine or inverter definition for Dynamics mode solutions. |
|  |  | *kvar* | Specify the base kvar.&nbsp; Alternative to specifying the power factor.&nbsp; Side effect:&nbsp; the power factor value is altered to agree based on present value of kW. |
|  |  | *kW* | Total base kW for the WindGen.&nbsp; A positive value denotes power coming OUT of the element, which is the opposite of a load. This value is modified depending on the dispatch mode. Unaffected by the global load multiplier and growth curves. If you want there to be more generation, you must add more WindGens or change this value. |
|  |  | *Lamda* |  Tip speed ratio (Default 7.95)&nbsp; |
|  |  | *like* | Make like another object, &nbsp; e.g.:New WindGen.WG2 like=WG1&nbsp; …&nbsp; |
|  |  | *Model* | Integer code for the model to use for generation variation with voltage. Valid values are:&nbsp; &nbsp; WindGen injects a constant kW at the specified power factor.&nbsp; WindGen is modeled as a constant admittance.&nbsp; Const kW, Fixed Q (Q never varies)&nbsp; Const kW, Fixed Q(as a constant reactance) Compute load injection from User-written Model.&nbsp; |
|  |  | *MVA* | MVA rating of electrical machine.&nbsp; Alternative to using kVA. |
|  |  | *N\_WTG* | Number of WTG in aggregation. Use it for dynamic simulations. |
|  |  | *P* | Number of pole pairs of the induction generator (Default 2) |
|  |  | *pd* | Air density in kg/m3 (Default 1.225) |
|  |  | *PF* | WindGen power factor. Default is 0.80. Enter negative for leading powerfactor (when kW and kvar have opposite signs.) A positive power factor for a WindGen signifies that the WindGen produces vars as is typical for a synchronous WindGen. Induction machines would be generally specified with a negative power factor. |
|  |  | *Phases* | Number of phases for the Wind generator |
|  |  | *Ploss* | Name of the XYCurve object describing the active power losses in pct versus the wind speed. |
|  |  | *Pss* | Per unit steady state output active power. Use it for dynamic simulations. |
|  |  | *QFlg* | &#49; to enable reactive power and voltage control. Use it for dynamic simulations. |
|  |  | *QMode* | Q control mode (0:Q, 1:PF, 2:VV). Use it for dynamic simulations. |
|  |  | *Qss* | Per unit steady state output reactive power. Use it for dynamic simulations. |
|  |  | *Rad* | Rotor radius in meters (Default 40) |
|  |  | *Rthev* | per unit Thevenin equivalent R. Use it for dynamic simulations. |
|  |  | *SimMechFlg* | &#49; to simulate mechanical system. Otherwise (0), it will only consider the electrical model. Use it for dynamic simulations. |
|  |  | *Spectrum* | Name of harmonic voltage or current spectrum for this WindGen. Default value is "default", which is defined when the DSS starts. |
|  |  | *UserData* | String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model. |
|  |  | *UserModel* | Name of DLL containing user-written model, which computes the terminal currents for Dynamics studies, overriding the default model.&nbsp; Set to "none" to negate previous setting. |
|  |  | *VCutIn* | Cut-in speed for the wind generator (m/s - default 5) |
|  |  | *VCutOut* | Cut-out speed for the wind generator (m/s - default 23) |
|  |  | *Vmaxpu* | Default = 1.10.&nbsp; Maximum per unit voltage for which the Model is assumed to apply. Above this value, the Windgen model reverts to a constant impedance model. |
|  |  | *Vminpu* | Default = 0.90.&nbsp; Minimum per unit voltage for which the Model is assumed to apply. Below this value, the Windgen model reverts to a constant impedance model.&nbsp; |
|  |  | *Vss* | Per unit steady state output voltage. Use it for dynamic simulations. |
|  |  | *VV\_Curve* | Name of the XY curve defining the control curve for implementing Vol-var control with this device. |
|  |  | *Vwind* | Wind speed in m/s. It is overridden by its yearly, daily, duty loadshapes if assigned for these types of simulations.&nbsp; |
|  |  | *Xthev* | per unit Thevenin equivalent X. Use it for dynamic simulations. |
|  |  | *Yearly* | Wind speed shape to use for yearly-mode simulations.&nbsp; Must be previously defined as a Loadshape object. If this is not specified, a constant value is assumed (no variation). Set to NONE to reset to no load shape. Nominally for 8760 simulations.&nbsp; If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated. |



***
_Created with the Standard Edition of HelpNDoc: [Create help files for the Qt Help Framework](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
