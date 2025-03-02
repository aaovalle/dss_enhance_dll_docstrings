# Fault Simulations

&nbsp;

A fault simulation is often a dynamics simulation, but doesn't have to be. A Fault object may be applied in conventional SNAPSHOT power flow mode, but the solution will be slightly different than in other modes. When the voltage falls below the nominal range, power consuming and power producing devices switch to constant impedance models. Convergence can sometimes be a problem, but is generally not.

In dynamics mode, the generators are converted to a dynamic model after a conventional power flow solution. Then the fault(s) are applied and the solution proceeds. Multiple faults can be applied simultaneously.

A Fault object is simply a multi-phase resistor branch (two-terminal) in which the second terminal defaults to being connected to ground. The dynamic mode is used for simulation of overcurrent protection devices.


***
_Created with the Standard Edition of HelpNDoc: [Easily create Web Help sites](<https://www.helpndoc.com/feature-tour>)_
