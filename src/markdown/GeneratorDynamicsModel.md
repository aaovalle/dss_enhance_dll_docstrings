# Generator Dynamics Model 

&nbsp;

&nbsp;

&nbsp;

The Generator object automatically converts into a form of Thevenin equivalent model when the program switches to Dynamics mode. This would occur on a “set mode=dynamics” or “solve mode=dynamics …” statement as well a Faultstudy mode. Figure 1 shows the nominal form of the model for a delta-connected generator (no zero sequence modeled in the Generator). It consists of a voltage source behind subtransient reactance, Xd’ (Xdp property), in the positive sequence network while the negative sequence is modeled as an impedance using the value specified for Xd” (Xdpp property). The voltage, E1, is computed to approximately match the positive sequence power flow computed just prior to entering Dynamics mode.

&nbsp;

The machine dynamics are governed by the traditional swing equations for a single mass. This simple model works reasonably well for such analyses as generator infeed to faults , openconductor simulations, and short DG islanding simulations. The different reactance value for negative sequence yields a more accurate result for unbalanced circuit conditions than a simple voltage source behind three single-phase reactances. There are no built-in models for exciter and governor controls, which would obviously be needed for extended dynamics studies and microgrid simulations. Nevertheless, this model satisfies many needs of distribution planners for evaluating DG interconnections.

&nbsp;

![Image](<lib/NewItem131.png>)\
**Figure 1. Nominal Generator Model in Dynamics Mode**

&nbsp;

When the zero sequence must be included, such as for grounded-wye connected alternators, it has been found that the OpenDSS performs better by inserting a Yg/Delta transformer with the same kVA rating in front of the model shown in Figure 1. The impedance of the transformer is set to the zero sequence impedance of the machine, which is typically about 5% or so. Then the Xdp and Xdpp properties are decreased by that amount. The impedance of the transformer provides a little linear system isolation from the nonlinear machine that assists in the convergence of the solution algorithm. approximates inverters that tend to produce a current in phase with the voltage, and is often good enough for planning purposes.

***
_Created with the Standard Edition of HelpNDoc: [Easily create Help documents](<https://www.helpndoc.com/feature-tour>)_
