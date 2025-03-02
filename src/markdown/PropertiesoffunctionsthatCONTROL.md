# Properties of functions that CONTROL reactive power

The functions that control reactive power of the controlled element have in common a property that defines the base reactive power and two that are associated with the control loop convergence. These functions are volt-var, DRC, watt-pf, watt-var, volt-watt combined with volt-var and volt-var combined with DRC.

* *RefReactivePower* : Defines the base reactive power for both the provided and absorbed reactive power, according to one of the following options:

  * *VARAVAL*: The base values for the provided and absorbed reactive power are equal to the available reactive power;
  * *VARMAX* : The base values of the provided and absorbed reactive power are equal to the value defined in the *kvarMax* and *kvarMaxAbs* properties, respectively.

* *VarChangeTolerance*: Tolerance in *pu* of the convergence of the control loop associated with reactive power. For the same control iteration, this value is compared to the difference between the desired reactive power value in *pu* with the output reactive power in *pu* of the controlled element;
* *deltaQ\_factor* : Maximum change in *pu* from the prior reactive output power to the desired reactive output power during each control iteration. If it is not set or set equal&nbsp; 1, OpenDSS will use its automatic convergence algorithm.


***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
