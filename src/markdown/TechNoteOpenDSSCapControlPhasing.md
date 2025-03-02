# TechNote OpenDSS CapControl Phasing

&nbsp;

***CapControl and RegControl Modifications***

&nbsp;

One issue with capacitor and regulator controls on 3phase banks is that some control monitor only one phase while some others monitor all three and evaluate the measurement differently. Properties have been added to both the CapControl and the RegControl to allow you to specify different ways of handling the monitored voltage or current.

&nbsp;

***CapControl***

&nbsp;

This applies to voltage control, current control, and voltage override. If the control type is 'kvar' the total kvar of the monitored circuit element is used. Two new properties have been added: CTPhase and PTPhase, for designating the monitored phase(s) for the CT and PT, respectively.

&nbsp;

Set these properties to one of the following:

&nbsp;

•The number of the phase (1, 2, or 3, etc.) to which the CT or PT is connected,

•AVG- averages the magnitudes of all phases

•MAX- controls on the maximum magnitude of all phases

•MIN- controls on the minimum magnitude of all phases

&nbsp;

If the controlled Capacitor object is delta connected, enter the first number of the LL pair (12,23,31,etc.). This series wraps back to the first phase (1) when the designated phase is equal to the number of phases. This is the same way many DSS objects work.

&nbsp;

The default value of both of these properties is 1. This is the same as voltage sampling in the previous versions, but is different than the currents. The current magnitudes were averaged.

&nbsp;

*Examples*

&nbsp;

New CapControl.mycontrol1 element=line.line1 terminal=1 capacitor=My3phcap type=voltage ptratio=60 on=118&nbsp;

New CapControl.mycontrol2 element=line.line1 terminal=1 capacitor=My3phcap type=voltage ptratio=60 on=118&nbsp;

New CapControl.mycontrol3 element=line.line1 terminal=1 capacitor=My3phcap type=current ctratio=1 on=200&nbsp;

New CapControl.mycontrol4 element=line.line1 terminal=1 capacitor=My3phcap type=current ctratio=1 on=200&nbsp;

New CapControl.mycontrol5 element=line.line1 terminal=1 capacitor=My3phcap type=current ctratio=1 on=200&nbsp;

\~ voltoverride=Yes ptratio=60 vmax=125 Ptphase=MAX

&nbsp;

***RegControl***

&nbsp;

The changes apply only to multiphase transformers such as those with LTC. The behavior for singlephase regulators is unchanged; the RegControl uses the winding voltage of singlephase regulator transformers and the line current.

&nbsp;

One property has been added: PTPhase. The current for the line drop compensator is assumed to be on the same phase.

&nbsp;

The options for the values are the same as the CapControl except that there is no AVG for now because of the way the LDC algorithm is currently written. We've got to do some thinking about what it means to average the phases for LDC before we proceed.

&nbsp;

Ptphase=MIN and Ptphase=MAX are implemented, where the phase is selected at each solution interval based on the voltage magnitude. For a regulator/LTC with LDC, the current used in the calculation is selected from the corresponding phase. The solution convergence of this approach is uncertain and currently untested, but you can choose the MIN or MAX option if you wish.

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Single source CHM, PDF, DOC and HTML Help creation](<https://www.helpndoc.com/help-authoring-tool>)_
