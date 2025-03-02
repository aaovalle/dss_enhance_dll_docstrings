# 3-Phase Short-Circuit Power and Current Calculation

&nbsp;

In addition to sequence impedances, the pair 3-phase and 1-phase short-circuit powers, *S*¯*sc*3 and *S*¯*sc*1, or the pair 3-phase and 1-phase short-circuit currents, *I*˙*sc*3 and *I*˙*sc*1, can also be utilized to define the voltage source element.

In this section, *S*¯*sc*3 and *I*˙*sc*3 are calculated considering that the voltage source element is at a 3-phase short-circuit condition, as presented in [Figure 4](<3-PhaseShort-CircuitPowerandCurr.md#\_bookmark10>).

&nbsp;

![Image](<lib/NewItem303.png>)

&nbsp;

**Figure 4: *Vsource* Element at a 3-phase Short-Circuit Condition**

&nbsp;

The 3-phase short-circuit current and the line-to-line voltage between phases *A* and *B* are as follows.

&nbsp;

![Image](<lib/NewItem445.png>)

![Image](<lib/NewItem447.png>)

&nbsp;

Applying KVL on phase *A*, one can obtain:

&nbsp;

![Image](<lib/NewItem449.png>)

&nbsp;

Applying KCL to node *SC*,

&nbsp;

![Image](<lib/NewItem450.png>)

&nbsp;

By applying the equations above and also considering that *Z*¯1 = *Z*¯*s − Z*¯*m*, one can obtain:

&nbsp;

![Image](<lib/NewItem451.png>)

From [Equation 13](<3-PhaseShort-CircuitPowerandCurr.md#\_bookmark13>), it is possible to obtain the magnitude of the 3-phase short-circuit current as function of the positive sequence impedance, as presented below:

&nbsp;

![Image](<lib/NewItem452.png>)

![Image](<lib/NewItem454.png>)

&nbsp;

Since the voltage source is symmetric, the 3-phase short-circuit power is defined as three times the power provide by each phase.

&nbsp;

![Image](<lib/NewItem455.png>)

&nbsp;

Then, it is possible to obtain the magnitude of the 3-phase short-circuit power as function of the positive sequence impedance.

&nbsp;

![Image](<lib/NewItem456.png>)

&nbsp;

![Image](<lib/NewItem458.png>)

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Convert Your Word Doc to an eBook: A Step-by-Step Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
