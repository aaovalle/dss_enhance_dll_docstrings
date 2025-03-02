# Properties

&nbsp;

The properties for the PVSystem object are listed below:

&nbsp;

|  | **Property** | **Description** |
| --- | --- | --- |
|  | *phases* |  Number of Phases, this PVSystem element.&nbsp; Power is evenly divided among phases.&nbsp; |
|  | *bus1* |  Bus to which the PVSystem element is connected.&nbsp; May include specific node specification.&nbsp; |
|  | *kv* |  Nominal rated (1.0 per unit) voltage, kV, for PVSystem element. For 2- and 3-phase PVSystem elements, specify phase-phase kV. Otherwise, specify actual kV across each branch of the PVSystem element. If 1-phase wye (star or LN), specify phase-neutral kV. If 1-phase delta or phase-phase connected, specify phase-phase kV.&nbsp; |
|  | *irradiance* |  Get/set the present irradiance value in kW/sq-m. Used as base value for shape multipliers. Generally entered as peak value for the time period of interest and the yearly, daily, and duty load shape objects are defined as per unit multipliers (just like Loads/Generators).&nbsp; |
|  | *Pmpp* |  Get/set the rated max power of the PV array for 1.0 kW/sq-m irradiance and a user-selected array temperature. The P-TCurve should be defined relative to the selected array temperature.&nbsp; |
|  | *Temperature* |  Get/set the present Temperature. Used as fixed value corresponding to PTCurve property. A multiplier is obtained from the Pmpp-Temp curve and applied to the nominal Pmpp from the irradiance to determine the net array output.&nbsp; |
|  | *pf* |  Nominally, the power factor for the output power. Default is 1.0. Setting this property will cause the inverter to operate in CONSTANT POWER FACTOR MODE. Enter negative when kW and kvar have opposite signs. A positive power factor signifies that the PVSystem element produces vars as is typical for a generator.&nbsp; &nbsp; |
|  |  |  |
|  | *conn* |  ={wye\|LN\|delta\|LL}.&nbsp; Default is wye.&nbsp; |
|  | *kvar* |  Get/set the present kvar value.&nbsp; Setting this property forces the inverter to operate in CONSTANT KVAR MODE.&nbsp; |
|  | *kVA* |  kVA rating of inverter. Used as the base for Dynamics mode and Harmonics mode values.&nbsp; |
|  | *%Cutin* |  % cut in power -- % of kVA rating of inverter. When the inverter is OFF, the power from the array must be greater than this for the inverter to turn on.&nbsp; |
|  | *%Cutout* |  % cut out power -- % of kVA rating of inverter. When the inverter is ON, the inverter turns OFF when the power from the array drops below this value.&nbsp; |
|  | *EffCurve* |  An XYCurve object, previously defined, that describes the PER UNIT efficiency vs PER UNIT of rated kVA for the inverter. Inverter output power is discounted by the multiplier obtained from this curve.&nbsp; |
|  | *P-TCurve* |  An XYCurve object, previously defined, that describes the PV array PER UNIT Pmpp vs Temperature curve. Temperature units must agree with the Temperature property and the Temperature shapes used for simulations. The Pmpp values are specified in per unit of the Pmpp value for 1 kW/sq-m irradiance. The value for the temperature at which Pmpp is defined should be 1.0. The net array power is determined by the irradiance \* Pmpp \* f(Temperature)&nbsp; |
|  | *%R* |  Equivalent percent internal resistance, ohms. Default is 0. Placed in series with internal voltage source for harmonics and dynamics modes. Use a combination of %IdlekW and %EffCharge and %EffDischarge to account for losses in power flow modes.&nbsp; |
|  | *%X* |  Equivalent percent internal reactance, ohms. Default is 50%. Placed in series with internal voltage source for harmonics and dynamics modes. (Limits fault current to 2 pu.) Use %Idlekvar and kvar properties to account for any reactive power during power flow solutions.&nbsp; |
|  | *model* |  Integer code (default=1) for the model to use for power output variation with voltage. Valid values are:&nbsp; 1: PVSystem element injects a CONSTANT kW, kvar at specified power factor or kvar value 2: PVSystem element is modeled as a CONSTANT ADMITTANCE. 3: Compute load injection from User-written Model.&nbsp; |
|  | *Vminpu* |  Default = 0.90.&nbsp; Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model.&nbsp; |
|  | *Vmaxpu* |  Default = 1.10.&nbsp; Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.&nbsp; |
|  | *yearly* |  Dispatch shape to use for YEARLY simulations.&nbsp; Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, If any, is repeated during Yearly solution modes. In the default dispatch mode, the PVSystem element uses this loadshape to trigger State changes.&nbsp; |
|  | *daily* |  Dispatch shape to use for DAILY simulations.&nbsp; Must be previously defined as a Loadshape object of 24 hrs, typically.&nbsp; In the default dispatch mode, the PVSystem element uses this loadshape to trigger State changes.&nbsp; |
|  | *duty* |  Load shape to use for DUTY cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.&nbsp; |
|  | *Tyearly* |  Temperature shape to use for YEARLY simulations.&nbsp; Must be previously defined as a TShape object. If this is not specified, the Daily dispatch shape, If any, is repeated during Yearly solution modes. The PVSystem element uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.&nbsp; |
|  | *Tdaily* |  Temperature shape to use for DAILY simulations.&nbsp; Must be previously defined as a TShape object of 24 hrs, typically.&nbsp; The PVSystem element uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.&nbsp; |
|  | *Tduty* |  Temperature shape to use for DUTY cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a TShape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat. The PVSystem model uses this TShape to determine the Pmpp from the Pmpp vs T curve. Units must agree with the Pmpp vs T curve.&nbsp; |
|  | *class* |  An arbitrary integer number representing the class of PVSystem element so that PVSystem values may be segregated by class.&nbsp; |
|  | *UserModel* |  Name of DLL containing user-written model, which computes the terminal currents for Dynamics studies, overriding the default model.&nbsp; Set to "none" to negate previous setting.&nbsp; |
|  | *UserData* |  String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model.&nbsp; |
|  | *debugtrace* |  {Yes \| No }&nbsp; Default is no.&nbsp; Turn this on to capture the progress of the PVSystem model for each iteration.&nbsp; Creates a separate file for each PVSystem element named "PVSystem\_name.CSV".&nbsp; |
|  | *spectrum* |  Name of harmonic voltage or current spectrum for this PVSystem element. Current injection is assumed for inverter. Default value is "default", which is defined when the DSS starts.&nbsp; |
|  | *%PminkvarMax* |  Minimum active power as percentage of Pmpp that allows the inverter to produce/absorb reactive power up to its kvarMax or kvarMaxAbs.&nbsp; |
|  | *%PminNoVars* |  Minimum active power as percentage of Pmpp under which there is no vars production/absorption.&nbsp; |
|  | *%Pmpp* |  Upper limit on active power as a percentage of Pmpp.&nbsp; |
|  | *AmpLimit* |  Is the current limiter per phase for the IBR when operating in GFM mode. This limit is imposed to prevent the IBR to enter into Safe Mode when reaching the IBR power ratings. Once the IBR reaches this value, it remains there without moving into Safe Mode. This value needs to be set lower than the IBR Amps rating.&nbsp; |
|  | *AmpLimitGain* |  Use it for fine tuning the current limiter when active, by default is 0.8, it has to be a value between 0.1 and 1. This value allows users to fine tune the IBRs current limiter to match with the user requirements.&nbsp; |
|  | *Balanced* |  {Yes \| No\*} Default is No.&nbsp; Force balanced current only for 3-phase PVSystems. Forces zero- and negative-sequence to zero. &nbsp; |
|  | *basefreq* |  Base Frequency for ratings.&nbsp; |
|  | *class* |  An arbitrary integer number representing the class of PVSystem element so that PVSystem values may be segregated by class.&nbsp; |
|  | *ControlMode* |  Defines the control mode for the inverter. It can be one of {GFM \| GFL\*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded microgrids, but, if the device is connected to the grid, it is highly recommended to use GFL.&nbsp; GFM control mode disables any control action set by the InvControl device.&nbsp; |
|  | *DutyStart* |  Starting time offset \[hours\] into the duty cycle shape for this PVSystem, defaults to 0.&nbsp; |
|  | *DynamicEq* |  The name of the dynamic equation (DinamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation.&nbsp; |
|  | *DynOut* |  The name of the variables within the Dynamic equation that will be used to govern the PVSystem dynamics.This PVsystem model requires 1 output from the dynamic equation: &nbsp; 1. Current.&nbsp; The output variables need to be defined in the same order.&nbsp; |
|  | *kp* |  It is the proportional gain for the PI controller within the inverter. Use it to modify the controller response in dynamics simulation mode.&nbsp; |
|  | *kvarMax* |  Indicates the maximum reactive power GENERATION (un-signed numerical variable in kvar) for the inverter (as an un-signed value). Defaults to kVA rating of the inverter.&nbsp; |
|  | *kvarMaxAbs* |  Indicates the maximum reactive power ABSORPTION (un-signed numerical variable in kvar) for the inverter (as an un-signed value). Defaults to kVA rating of the inverter.&nbsp; |
|  | *kVDC* |  Indicates the rated voltage (kV) at the input of the inverter at the peak of PV energy production. The value is normally greater or equal to the kV base of the PV system. It is used for dynamics simulation ONLY.&nbsp; |
|  | *LimitCurrent* |  Limits current magnitude to Vminpu value for both 1-phase and 3-phase PVSystems similar to Generator Model 7. For 3-phase, limits the positive-sequence current but not the negative-sequence.&nbsp; |
|  | *PFPriority* |  {Yes/No\*/True/False} Set inverter to operate with PF priority when in constant PF mode. If "Yes", value assigned to "WattPriority" is neglected. If controlled by an InvControl with either Volt-Var or DRC or both functions activated, PF priority is neglected and "WattPriority" is considered. Default = No.&nbsp; |
|  | *PITol* |  It is the tolerance (%) for the closed loop controller of the inverter. For dynamics simulation mode.&nbsp; |
|  | *SafeMode* |  (Read only) Indicates whether the inverter entered (Yes) or not (No) into Safe Mode.&nbsp; |
|  | *SafeVoltage* |  Indicates the voltage level (%) respect to the base voltage level for which the Inverter will operate. If this threshold is violated, the Inverter will enter safe mode (OFF). For dynamic simulation. By default is 80%&nbsp; |
|  | *VarFollowInverter* |  Boolean variable (Yes\|No) or (True\|False). Defaults to False which indicates that the reactive power generation/absorption does not respect the inverter status.When set to True, the PVSystem reactive power generation/absorption will cease when the inverter status is off, due to panel kW dropping below %Cutout.&nbsp; The reactive power generation/absorption will begin again when the panel kW is above %Cutin.&nbsp; When set to False, the PVSystem will generate/absorb reactive power regardless of the status of the inverter.&nbsp; |
|  | *WattPriority* |  {Yes/No\*/True/False} Set inverter to watt priority instead of the default var priority.&nbsp; |


&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily Add Encryption and Password Protection to Your PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
