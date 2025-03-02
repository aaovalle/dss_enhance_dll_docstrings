# Properties

&nbsp;

The properties are:

&nbsp;

| **Property** | **Description** |
| --- | --- |
| *Phases* |  No. of phases this induction machine. Default is 3.&nbsp; |
| *bus1* |  Name of bus to which the machine is connected. Include node definitions if the terminal conductors are connected unusually. 3-phase Wye-connected machines have 4 conductors; Delta-connected have 3. 1-phase Delta (or Line-Line) has 2 conductors; 2-phase has 3. The remaining Delta, or line-line, connections have the same number of conductors as phases.&nbsp; |
| *Kv* |  Base voltage for the induction machine. For 2- or 3-phase generators, specified in phase-to-phase kV. For all other generators, the actual kV across the generator branch. If wye (star) connected, specify the phase-to-neutral (L-N) kV. If delta or phase-to-phase connected, specify the phase-to-phase (L-L) kV.&nbsp; |
| *kW* |  Shaft Power, kW, for the Induction Machine. A positive value denotes power for a load. Negative value denotes an induction generator. Total of all phases.&nbsp; |
| *Pf* |  (Read Only) nominal Power Factor for machine under present conditions. You cannot specify PF for an induction machine; this is determined by circuit conditions. If negative, the watts and vars are flowing in opposite directions. Reactive power in an induction machine is almost always INTO the machine.&nbsp; |
| *Conn* |  Connection of stator: Delta or Wye. Default is Delta. Generally, delta is better for simulations in OpenDSS. Ungrounded Wye can lead to numerical instability.&nbsp; |
| *kVA* |  Rated kVA for the machine.&nbsp; |
| *H* |  Per unit mass constant of the machine. MW-sec/MVA. Default is 1.0&nbsp; |
| *D* |  Damping constant. Usual range is 0 to 4. Default is 1.0. Adjust to get damping in Dynamics mode.&nbsp; |
| *puRs* |  Per unit stator resistance. Default is 0.0053.&nbsp; |
| *puXs* |  Per unit stator leakage reactance. Default is 0.106&nbsp; |
| *puRr* |  Per unit rotor resistance. Default is 0.007&nbsp; |
| *puXr* |  Per unit rotor leakage reactance. Default is 0.12&nbsp; |
| *puXm* |  Per unit magnetizing reactance.Default is 4.0&nbsp; |
| *Slip* |  Initial slip value. Default is 0.007&nbsp; |
| *MaxSlip* |  Max slip value to allow. Default is 0.1. Set this before setting slip. In Dynamics simulations, the slip may exceed this value. This is mainly to allow the power flow solution to converge.&nbsp; |
| *SlipOption* |  Option for slip model. One of {fixedslip \| variableslip\* } Variable slip is the default and slip will be computed to satisfy the power specification. If fixed slip, kW is computed to match the slip specification.&nbsp; |
| *Spectrum* |  Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd", or blocked rotor, for machine - default. Not usually much of an issue for an induction machine. This model is still under development.&nbsp; |


&nbsp;

(The usual Daily, Yearly, Duty Loadshape Options)

***
_Created with the Standard Edition of HelpNDoc: [Create HTML Help, DOC, PDF and print manuals from 1 single source](<https://www.helpndoc.com/help-authoring-tool>)_
