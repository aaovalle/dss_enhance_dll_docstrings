# Checking inverter limits

&nbsp;

The convergence process must use values that respect the limits presented in the modeling of the PC element, in this sense, the values of the active power limit and the desired reactive power are calculated considering the restrictions of the inverter. As a result of this check, *pLlim*\[*t*\]*j* and *qDlim*\[*t*\]*j* are defined.

[Equation 68](<Checkinginverterlimits.md#\_bookmark76>) presents the calculation for the mode that have the smart inverter volt-watt function.

&nbsp;

![Image](<lib/NewItem552.png>)

&nbsp;

&nbsp;

For modes that have the smart inverter volt-var, DRC, watt-pf or watt-var functions, the checking the inverter limits depends on the options of the *RefReactivePower* property, as can be seen below:

**–** For *VARMAX*, the calculation of the reactive power limit of the inverter is performed by means of [Equation 69](<OpenDSSDocumentation.md#\_bookmark77>) when the inverter is configured to give priority to active power.

&nbsp;

&nbsp;

![Image](<lib/NewItem553.png>)

&nbsp;

On the other hand, with priority for reactive power, the calculation follows [Equation 70](<OpenDSSDocumentation.md#\_bookmark78>).

&nbsp;

&nbsp;

![Image](<lib/NewItem554.png>)

&nbsp;

For watt-pf function, besides the two priority options above, it can also have power factor priority, as shown in [Equation 71](<OpenDSSDocumentation.md#\_bookmark79>)

&nbsp;

![Image](<lib/NewItem555.png>)

&nbsp;

**–** For *VARAVAL*, the calculation of the reactive power limit is also performed using [Equation 70](<OpenDSSDocumentation.md#\_bookmark78>). The watt-pf function does not have this option, it always works with *VARMAX*.

Where *\|QLimit*\[*t*\]*j\|* and *\|QLimitneg* \[*t*\]*j\|* are calculated in Step 5 of sub subsection 1.2.1.

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Help Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com>)_
