# The Newton method

&nbsp;

The Newton method is a simple implementation of the Newton-Raphson method that uses the Y-Bus matrix as reference for reproducing the effects of the Jacobian matrix when calculating the circuit model voltages. However, in this version of the Newton algorithm the Y-Bus matrix remains unchanged, offering a different implementation from the original method.

&nbsp;

In this method, the injection currents are adjusted to reduce the voltage mismatch obtained after operating:

&nbsp;

![Image](<lib/eq3.png>)

&nbsp;

Where Iinj is the input, Ysystem is the Y-BUs admittance matrix and V is the partial voltage for the present iteration. At each iteration the voltage is added until the voltage mismatch is below the convergence tolerance as follows:

&nbsp;

![Image](<lib/NewItem 20.png>)

&nbsp;

The implementation of this algorithm is depicted below:

&nbsp;

![Image](<lib/NewItem 21.png>)

Figure 2. Newton method implementation in OpenDSS

&nbsp;

The current injections are associated to each PCE mode defined when describing the circuit.


***
_Created with the Standard Edition of HelpNDoc: [Free CHM Help documentation generator](<https://www.helpndoc.com>)_
