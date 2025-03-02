# Control Mode 1 (Mode=1)

&nbsp;

In this control mode the voltage regulation controller regulates the voltage at the output of the UPFC device. In this mode, the controller used to perform the reactive power compensation will not perform any control action.

The voltage regulation is made considering a Thevenin series equivalent of a voltage source, where the parallel impedance is given by the impedance of the series transformer Xs. Then, the value of the current source *Is* will be given by:

&nbsp;

![Image](<lib/NewItem583.png>)

&nbsp;

Where *Vdiff1* is the calculated as follows:

&nbsp;

![Image](<lib/NewItem584.png>)

&nbsp;

And *Is\[z-1\]* is a shift register containing the value of the current source *Is* calculated in the previous iteration. Equations (3) and (4) are used to calculate the value of the current source until reach convergence, which is calculate considering the tolerance defined in the property Tol1. When the convergence is reached, the value of *Is* will be equal to *Is\[z-1\]*.

On the other hand, the value for the current source *Ic* is calculated by using the following expression:

&nbsp;

![Image](<lib/NewItem585.png>)

&nbsp;

Equation (5) refers to power’s balance, which basically allows to balance the power at the input and the output of the UPFC. However, the UPFC device converts active power into reactive power and add it at the load side to elevate/reduce the voltage magnitude and take it to the reference voltage. As a result, equation (5) is reformulated as follows:

&nbsp;

![Image](<lib/NewItem586.png>)

&nbsp;

In (6), *Losses* corresponds to the losses programmed in the XY curve (Y axis) when the input voltage acquires certain value respect to the RefkV property (pu).

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Document into a Professional eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
