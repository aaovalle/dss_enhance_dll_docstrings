# Checking auxiliary options

&nbsp;

The auxiliary options that can be selected are intended to limit the variations of the active power limit and/or the desired reactive power during time steps. As a result of this verification, *pLopc*\[*t*\]*j* and *qDopc*\[*t*\]*j* are defined.

&nbsp;

&nbsp;

&nbsp;

![A diagram of a line

Description automatically generated with medium confidence](<lib/NewItem469.png>)

**Figure 13: watt-var curve**

&nbsp;

**Standard** The standard option (default) does not limit the variation of the active power limit and the desired reactive power, as can be seen in the [Equation 62](<OpenDSSDocumentation.md#\_bookmark70>) and [Equation 63](<OpenDSSDocumentation.md#\_bookmark71>).

&nbsp;

![Image](<lib/NewItem546.png>)

&nbsp;

![Image](<lib/NewItem547.png>)

&nbsp;

In this version of the model, the watt-pf and watt-var functions do not have the auxiliary options implemented. Therefore, the [Equation 62](<OpenDSSDocumentation.md#\_bookmark70>) and [Equation 63](<OpenDSSDocumentation.md#\_bookmark71>) are applied.

&nbsp;

**LPF** This option consists of applying the active power limit, *pLfun*\[*t*\]*j*, and/or the desired reactive power, *qDfun*\[*t*\]*j*, as input of a first-order low pass filter with time constant equal to *τ* . As a result, the values of the options are set according to Equations [64](<OpenDSSDocumentation.md#\_bookmark72>) and [65](<Checkingauxiliaryoptions.md#\_bookmark73>). These equations present as initial conditions the results of these equations in the previous time step, *pLopc*\[*t −* 1\] and *qDopc*\[*t −* 1\].

&nbsp;

![Image](<lib/NewItem548.png>)

&nbsp;

&nbsp;

![Image](<lib/NewItem549.png>)

&nbsp;

Where *τ* is the value set in the *LPFTau* property.

&nbsp;

**RF** This option limits the change of the active power limit and the desired reactive power between time steps to a maximum value. Equations [66](<OpenDSSDocumentation.md#\_bookmark74>) and [67](<OpenDSSDocumentation.md#\_bookmark75>) present the application of this option.

&nbsp;

![Image](<lib/NewItem550.png>)

&nbsp;

&nbsp;

![Image](<lib/NewItem551.png>)

&nbsp;

Where:

&nbsp;

* Δp/ΔtRF and&nbsp; Δq/ΔtRF are the value set in the *RiseFallLimit* property;

&nbsp;

* ∆*t* is the stepsize of the QSTS simulation. In other words, it corresponds to the difference between two consecutive time steps, *t* and *t −* 1, in a time scale.

***
_Created with the Standard Edition of HelpNDoc: [Elevate your documentation to new heights with HelpNDoc's built-in SEO](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
