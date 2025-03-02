# Common properties

The common properties that need to be defined in InvControl are listed below:

* *DERList* : Array list of PVSystem and/or Storage2 elements to be controlled. If not specified, all PVSystem and Storage2 in the circuit are assumed to be controlled by this control;
* *mode*: Smart inverter function in which the InvControl will control the PC elements specified in *DERList*, according to the options below:

  * *VOLTVAR*: Smart inverter volt-var function. This mode attempts to CONTROL the vars, according to one or two volt-var curves, depending on the monitored voltages, present active power output, and the capabilities of the PC element;
  * *VOLTWATT* : Smart inverter volt-watt function. This mode attempts to LIMIT the watts, according to one defined volt-watt curve, depending on the monitored voltages and the capabilities of the PC element;
  * *DYNAMICREACCURR*: Smart inverter Dynamic Reactive Current (DRC) function. This mode attempts to increasingly counter deviations by CONTROLLING vars, depending on the monitored voltages, present active power output, and the capabilities of the PC element;
  * *WATTPF* : Smart inverter watt-pf function. This mode attempts to CONTROL the vars, according to a watt-pf curve, depending on the present active power output, and the capabilities of the PC element;
  * *WATTVAR*: Smart inverter watt-var function. This mode attempts to CONTROL the vars, according to a watt-var curve, depending on the present active power output, and the capabilities of the PC element;

* *Combimode*: Combination of smart inverter functions in which the InvControl will control the PC elements in *DERList*, according to the options below:

  * *VV\_VW* : Smart inverter volt-var and volt-watt function;
  * *VV\_DRC* : Smart inverter volt-var and DRC function.

* *voltage\_curvex\_ref* : Base voltage that is considered to calculate the monitored voltage in *pu*, the options are listed below:

  * *rated* : It uses as base voltage the rated voltage of the controlled element;
  * *avg* : It uses an average value as the base voltage. This average value is calculated using the monitored voltage values of previous time steps that are stored in a moving window. This window has a length in units of time, defined in the *avgwindowlen*;
  * *ravg* : It uses as base voltage the rated voltage of the controlled element. However, the value that is used to calculate the monitored voltage in *pu* is the average value of the moving window described in option *avg*.

* *avgwindowlen*: The time length of the averaging window;
* *VoltageChangeTolerance*: Tolerance in *pu* of the control loop convergence associated to the monitored voltage in *pu*. This value is compared with the difference of the monitored voltage in *pu* of the current and previous control iterations of the control loop;
* *RateofChangeMode*: Auxiliary option that aims to limit the changes of the desired reactive power and the active power limit between time steps, the alternatives are listed below:

  * *INACTIVE* : It indicates there is no limit on rate of change imposed for either active or reactive power output;
  * *LPF* : A low-pass RC filter is applied to the desired reactive power and/or the active power limit to determine the output power as a function of a time constant defined in the *LPFTau* property;
  * *RISEFALL*: A rise and fall limit in the change of active and/or reactive power expressed in terms of *pu* power per second, defined in the *RiseFallLimit*, is applied to the desired reactive power and/or the active power limit.

* *RiseFallLimit* : Limit in *pu* power per second used by the *RISEFALL* option of the *Rate- ofChangeMode* property. The base value for this ramp is defined in the *RefReactivePower* property and/or in *VoltwattYAxis*;
* *LPFTau*: Filter time constant of the *LPF* option of the *RateofChangeMode* property. The time constant will cause the low-pass filter to achieve 95% of the target value in 3 time constants.
* *monBus*: Array list of monitored buses with their nodes;
* *monBusesVbase*: Array list of rated voltages of the buses and their nodes presented in the

*monBus* property. This list may have different line-to-line and/or line-to-ground voltages;

* *monVoltageCalc*: Calculation options for monitored voltage in *V* . These options can be applied to the nodal voltages of the controlled element or to the list of voltages of the buses defined in the property *monBus*:

  * *AVG*: Calculates the mean of the voltages;
  * *MAX* : Stores the maximum voltage;
  * *MIN* : Stores the minimum voltage.

Considering that the list of voltages of the buses defined in *monBus* may present values with different magnitudes, the list that is used in this step corresponds to the list that presents its Volts values based on the same base voltage, which is the rated voltage of the controlled element. Step 3 of subsection 2.4 presents this process in more details.


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your CHM Help File Creation with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
