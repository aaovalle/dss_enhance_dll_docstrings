# Properties

&nbsp;

The storage element properties are listed as follows:

&nbsp;

&nbsp;

| **Property** | **Description** |
| --- | --- |
| *%Charge* |  Charging rate (input power) in Percent of rated kW. Default = 100.&nbsp; |
| *%Discharge* |  Discharge rate (output power) in Percent of rated kW. Default = 100.&nbsp; |
| *%EffCharge* |  Percent efficiency for CHARGING the storage element. Default = 90.&nbsp; |
| *%EffDischarge* |  Percent efficiency for DISCHARGING the storage element. Default = 90.Idling losses are handled by %IdlingkW property and are in addition to the charging and discharging efficiency losses in the power conversion process inside the unit.&nbsp; |
| *%Idlingkvar* |  Percent of rated kW consumed as reactive power (kvar) while idling. Default = 0.&nbsp; |
| *%IdlingkW* |  Percent of rated kW consumed while idling. Default = 1.&nbsp; |
| *%R* |  Equivalent percent internal resistance, ohms. Default is 0. Placed in series with internal voltage source for harmonics and dynamics modes. Use a combination of %IdlekW and %EffCharge and %EffDischarge to account for losses in power flow modes.&nbsp; |
| *%reserve* |  Percent of rated kWh storage capacity to be held in reserve for normal operation.&nbsp; Default = 20.&nbsp; This is treated as the minimum energy discharge level unless there is an emergency. For emergency operation set this property lower. Cannot be less than zero.&nbsp; |
| *%stored* |  Present amount of energy stored, % of rated kWh. Default is 100%.&nbsp; |
| *%X* |  Equivalent percent internal reactance, ohms. Default is 50%. Placed in series with internal voltage source for harmonics and dynamics modes. (Limits fault current to 2 pu.) Use %Idlekvar and kvar properties to account for any reactive power during power flow solutions.&nbsp; |
| *basefreq* |  Base Frequency for ratings.&nbsp; |
| *bus1* |  Bus to which the Storage element is connected. May include specific node specification.&nbsp; |
| *ChargeTrigger* |  Dispatch trigger value for charging the storage.&nbsp; If = 0.0 the Storage element state is changed by the State command or StorageController object.&nbsp; If \<\> 0 the Storage element state is set to CHARGING when this trigger level is GREATER than either the specified Loadshape curve value or the price signal or global Loadlevel value, depending on dispatch mode. See State property.&nbsp; |
| *class* |  An arbitrary integer number representing the class of Storage element so that Storage values may be segregated by class.&nbsp; |
| *conn* |  ={wye\|LN\|delta\|LL}. Default is wye.&nbsp; |
| *daily* |  Dispatch shape to use for daily simulations. Must be previously defined as a Loadshape object of 24 hrs, typically. In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.&nbsp; |
| *debugtrace* |  {Yes \| No } Default is no. Turn this on to capture the progress of the Storage model for each iteration. Creates a separate file for each Storage element named "STORAGE\_name.CSV".&nbsp; |
| *DischargeTrigger* |  Dispatch trigger value for discharging the storage. If = 0.0 the Storage element state is changed by the State command or by a StorageController object. If \<\> 0 the Storage element state is set to DISCHARGING when this trigger level is EXCEEDED by either the specified Loadshape curve value or the price signal or global Loadlevel value, depending on dispatch mode. See State property.&nbsp; |
| *DispMode* |  {DEFAULT \| FOLLOW \| EXTERNAL \| LOADLEVEL \| PRICE } Default = "DEFAULT". Dispatch mode.&nbsp; In DEFAULT mode, Storage element state is triggered to discharge or charge at the specified rate by the loadshape curve corresponding to the solution mode.&nbsp; In FOLLOW mode the kW and kvar output of the STORAGE element follows the active loadshape multipliers until storage is either exhausted or full. The element discharges for positive values and charges for negative values. The loadshapes are based on the kW and kvar values in the most recent definition of kW and PF or kW and kvar properties.&nbsp; In EXTERNAL mode, Storage element state is controlled by an external Storage controller. This mode is automatically set if this Storage element is included in the element list of a StorageController element. For the other two dispatch modes, the Storage element state is controlled by either the global default Loadlevel value or the price level.&nbsp; |
| *duty* |  Load shape to use for duty cycle dispatch simulations such as for solar ramp rate studies. Must be previously defined as a Loadshape object. Typically would have time intervals of 1-5 seconds. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.&nbsp; |
| *DynaData* |  String (in quotes or parentheses if necessary) that gets passed to the user-written dynamics model Edit function for defining the data required for that model.&nbsp; |
| *DynaDLL* |  Name of DLL containing user-written dynamics model, which computes the terminal currents for Dynamics-mode simulations, overriding the default model. Set to "none" to negate previous setting. This DLL has a simpler interface than the UserModel DLL and is only used for Dynamics mode.&nbsp; |
| *enabled* |  {Yes\|No or True\|False} Indicates whether this element is enabled.&nbsp; |
| *kv* |  Nominal rated (1.0 per unit) voltage, kV, for Storage element. For 2- and 3-phase Storage elements, specify phase-phase kV. Otherwise, specify actual kV across each branch of the Storage element. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.&nbsp; |
| *kVA* |  kVA rating of power output. Defaults to rated kW. Used as the base for Dynamics mode and Harmonics mode values.&nbsp; |
| *kvar* |  Get/set the present kvar value. Alternative to specifying the power factor. Side effect: the power factor value is altered to agree based on present value of kW.&nbsp; |
| *kW* |  Get/set the present kW value. A positive value denotes power coming OUT of the element, which is the opposite of a Load element. A negative value indicates the Storage element is in Charging state. This value is modified internally depending on the dispatch mode.&nbsp; |
| *kWhrated* |  Rated storage capacity in kWh. Default is 50.&nbsp; |
| *kWhstored* |  Present amount of energy stored, kWh. Default is same as kWh rated.&nbsp; |
| *kWrated* |  kW rating of power output. Base for Loadshapes when DispMode=Follow. Side effect: Sets KVA property.&nbsp; |
| *like* |  Make like another object, e.g.: New Storage.S2 like=S1 ...&nbsp; |
| *model* |  Integer code (default=1) for the model to use for powet output variation with voltage. Valid values are:&nbsp; 1:Storage element injects a CONSTANT kW at specified power factor. 2:Storage element is modeled as a CONSTANT ADMITTANCE. 3:Compute load injection from User-written Model.&nbsp; |
| *pf* |  Nominally, the power factor for discharging (acting as a generator). Default is 1.0. Setting this property will also set the kvar property.Enter negative for leading powerfactor (when kW and kvar have opposite signs.) A positive power factor for a generator signifies that the Storage element produces vars as is typical for a generator.&nbsp; |
| *phases* |  Number of Phases, this Storage element. Power is evenly divided among phases.&nbsp; |
| *spectrum* |  Name of harmonic voltage or current spectrum for this Storage element. Current injection is assumed for inverter. Default value is "default", which is defined when the DSS starts.&nbsp; |
| *State* |  {IDLING \| CHARGING \| DISCHARGING} Get/Set present operational state. In DISCHARGING mode, the Storage element acts as a generator and the kW property is positive. The element continues discharging at the scheduled output power level until the storage reaches the reserve value. Then the state reverts to IDLING. In the CHARGING state, the Storage element behaves like a Load and the kW property is negative. The element continues to charge until the max storage kWh is reached and Then switches to IDLING state. In IDLING state, the kW property shows zero. However, the resistive and reactive loss elements remain in the circuit and the power flow report will show power being consumed.&nbsp; |
| *TimeChargeTrig* |  Time of day in fractional hours (0230 = 2.5) at which storage element will automatically go into charge state. Default is 2.0. Enter a negative time value to disable this feature.&nbsp; |
| *UserData* |  String (in quotes or parentheses) that gets passed to user-written model for defining the data required for that model.&nbsp; |
| *UserModel* |  Name of DLL containing user-written model, which computes the terminal currents for both power flow and dynamics, overriding the default model. Set to "none" to negate previous setting.&nbsp; |
| *Vmaxpu* |  Default = 1.10. Maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model.&nbsp; |
| *Vminpu* |  Default = 0.90. Minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model.&nbsp; |
| *yearly* |  Dispatch shape to use for yearly simulations. Must be previously defined as a Loadshape object. If this is not specified, the Daily dispatch shape, if any, is repeated during Yearly solution modes. In the default dispatch mode, the Storage element uses this loadshape to trigger State changes.&nbsp; |
| *ControlMode* |  Defines the control mode for the inverter. It can be one of {GFM \| GFL\*}. By default it is GFL (Grid Following Inverter). Use GFM (Grid Forming Inverter) for energizing islanded micro-grids, but, if the device is connected to the grid, it is highly recommended to use GFL.&nbsp; GFM control mode disables any control action set by the InvControl device.&nbsp; |
| *DynamicEq* |  The name of the dynamic equation (DinamicExp) that will be used for defining the dynamic behavior of the generator. if not defined, the generator dynamics will follow the built-in dynamic equation.&nbsp; |
| *DynOut* |  The name of the variables within the Dynamic equation that will be used to govern the PVSystem dynamics.This PVsystem model requires 1 output from the dynamic equation: &nbsp; 1. Current.&nbsp; The output variables need to be defined in the same order.&nbsp; |
| *kp* |  It is the proportional gain for the PI controller within the inverter. Use it to modify the controller response in dynamics simulation mode.&nbsp; |
| *kvarMax* |  Indicates the maximum reactive power GENERATION (un-signed numerical variable in kvar) for the inverter. Defaults to kVA rating of the inverter.&nbsp; |
| *kvarMaxAbs* |  Indicates the maximum reactive power ABSORPTION (un-signed numerical variable in kvar) for the inverter. Defaults to kvarMax.&nbsp; |
| *kVDC* |  Indicates the rated voltage (kV) at the input of the inverter while the storage is discharging. The value is normally greater or equal to the kV base of the Storage device. It is used for dynamics simulation ONLY.&nbsp; |
| *LimitCurrent* |  Limits current magnitude to Vminpu value for both 1-phase and 3-phase Storage similar to Generator Model 7. For 3-phase, limits the positive-sequence current but not the negative-sequence.&nbsp; |
| *PFPriority* |  If set to true, priority is given to power factor and WattPriority is neglected. It works only if operating in either constant PF or constant kvar modes. Defaults to False.&nbsp; |
| *PITol* |  It is the tolerance (%) for the closed loop controller of the inverter. For dynamics simulation mode.&nbsp; |
| *SafeMode* |  (Read only) Indicates whether the inverter entered (Yes) or not (No) into Safe Mode.&nbsp; |
| *SafeVoltage* |  Indicates the voltage level (%) respect to the base voltage level for which the Inverter will operate. If this threshold is violated, the Inverter will enter safe mode (OFF). For dynamic simulation. By default is 80%&nbsp; |
| *VarFollowInverter* |  Boolean variable (Yes\|No) or (True\|False). Defaults to False, which indicates that the reactive power generation/absorption does not respect the inverter status.When set to True, the reactive power generation/absorption will cease when the inverter status is off, due to DC kW dropping below %CutOut.&nbsp; The reactive power generation/absorption will begin again when the DC kW is above %CutIn.&nbsp; When set to False, the Storage will generate/absorb reactive power regardless of the status of the inverter.&nbsp; |
| *WattPriority* |  {Yes/No\*/True/False} Set inverter to watt priority instead of the default var priority.&nbsp; |



***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
