# Example 1

Assume that the *Vsource* element presents the following parameters:

&nbsp;

* Name: *TheveninEquivalent*
* Nominal Voltage: *\|E*˙*AB \|* = 13#8202;*.*&#8202;8 *kV*
* Operating Voltage: *\|e*˙*A\|* = 1#8202;*.*&#8202;1 *pu*
* Connection Bus: *A*
* Connection Configuration: *Y g*
* Zero Sequence Impedance: *Z*¯0 = 0#8202;*.*&#8202;025862916 + *j ×* 0#8202;*.*&#8202;077588748 Ω
* Positive Sequence Impedance: *Z*¯1 = 0#8202;*.*&#8202;023094242 + *j ×* 0#8202;*.*&#8202;092376969 Ω

&nbsp;

The code snippet below presents the circuit element definition with such parameters:

&nbsp;

New Circuit.TheveninEquivalent bus1=A pu=1.1 basekv=13.8

\~ Z0=\[0.025862916,0.077588748\] Z1=\[0.023094242,0.092376969\]

&nbsp;

Set voltagebases=\[13.8\]

Calcvoltagebases

&nbsp;

Solve&nbsp;

&nbsp;

It is assumed that only the short-circuit powers are known. To assume the same voltage source as above, the short-circuit powers are first calculated from equations [(17)](<3-PhaseShort-CircuitPowerandCurr.md>), [(24)](<Single-PhaseShort-CircuitPoweran.md>) and [(26)](<Single-PhaseShort-CircuitPoweran.md>) considering the same source characteristics as in the previous example.

&nbsp;

![Image](<lib/NewItem330.png>)

&nbsp;

It is important to note that OpenDSS only takes the magnitude of the short-circuit powers as input parameters. The angles must be entered indirectly through the *x*1*r*1 parameter, which represents the *X1/R1* ratio, where *R*1 and *X*1 are the positive sequence resistance and reactance, respectively.

With that, the positive sequence impedance and the three-phase short-circuit power can be written as follows.

&nbsp;

![Image](<lib/NewItem331.png>)

&nbsp;

Thus, the three-phase short-circuit power angle can be specified through *x*1*r*1 following Equation 29.

&nbsp;

![Image](<lib/NewItem332.png>)

To enter the single-phase short-circuit power angle, *x*0*r*0 property is utilized, which represents *X0/R0*ratio, where *R*0 and *X*0 are the zero sequence resistance and reactance, respectively.

*Z*¯0 can be calculated from the short-circuit powers. First, *Z*¯1 is calculated through [Equation 30](<OpenDSSDocumentation.md#\_bookmark30>).

&nbsp;

![Image](<lib/NewItem333.png>)

Second, *Z*¯*s* is calculated with [Equation 31](<OpenDSSDocumentation.md#\_bookmark31>).

&nbsp;

![Image](<lib/NewItem334.png>)

With *Z*¯1 and *Z*¯*s*, *Z*¯0 can be calculate through [Equation 32](<OpenDSSDocumentation.md#\_bookmark32>), which is the result of the manipulation of [Equation 26](<OpenDSSDocumentation.md#\_bookmark23>).

&nbsp;

![Image](<lib/NewItem335.png>)

&nbsp;

Finally, the relation X0/R0 is calculated following [Equation 33](<OpenDSSDocumentation.md#\_bookmark33>).

&nbsp;

![Image](<lib/NewItem336.png>)

The magnitude of the short-circuit powers and the ratios *X0/R0* and *X1/R1* are utilized to define the circuit element as follows:

&nbsp;

New Circuit.TheveninEquivalent bus1=A pu=1.1 basekv=13.8

\~ MVAsc3=2000 x1r1=4 MVAsc1=2100 x0r0=3

&nbsp;

Set voltagebases=\[13.8\]

Calcvoltagebases

&nbsp;

Solve&nbsp;

To define the same element but the short-circuit current parameters, those can be obtained from [(27)](<RelationsbetweenObtainedParamete.md>) and [(28)](<RelationsbetweenObtainedParamete.md>).

&nbsp;

![Image](<lib/NewItem337.png>)

&nbsp;

As in the short-circuit powers case, the short-circuit currents magnitude and *X0/R0* and *X1/R1* ratios are used. With the short-circuit currents data *I*˙*sc*1 and *I*˙*sc*1, the short-circuit powers are calculated with [(27)](<RelationsbetweenObtainedParamete.md>) and [(28)](<RelationsbetweenObtainedParamete.md>) and, therefore, the method for obtaining *X0/R0* and *X1/R1* presented above can be used.

The source definition with the short-circuit currents data is presented below:

&nbsp;

New Circuit.TheveninEquivalent bus1=A pu=1.1 basekv=13.8

\~ Isc3=83674 x1r1=4 Isc1=87858 x0r0=3

&nbsp;

Set voltagebases=\[13.8\]

Calcvoltagebases

&nbsp;

Solve&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
