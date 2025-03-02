# Example 3 - Unbalanced Voltage Source

In order to model an unbalanced voltage source, three independent single-phase voltage sources are required. Those must be connected appropriately to represent the desired connection configuration. Since the voltage sources are independent, the source impedance must be modeled with a separate element to preserve the mutual coupling between phases. In the example below, a reactor is used for that purpose. Note that, in this case, if the desired configuration is Wye, the *basekV* parameter must be specified as a line-to-neutral voltage.

&nbsp;

![Image](<lib/NewItem340.png>)

**Figure 9: 3-Phase Wye Grounded-Connected Unbalanced *Vsource* Element**

&nbsp;

&nbsp;

New Circuit.ThA bus1=A\_internal.1 phases=1 pu=1.1 basekv=7.97

\~ Z0=\[1e-6,1e-6\] Z1=\[1e-6,1e-6\]

New Vsource.ThB bus1=A\_internal.2 phases=1 pu=1.1 basekv=7.97

\~ Z0=\[1e-6,1e-6\] Z1=\[1e-6,1e-6\]

New Vsource.ThC bus1=A\_internal.3 phases=1 pu=1.1 basekv=7.97

\~ Z0=\[1e-6,1e-6\] Z1=\[1e-6,1e-6\]

&nbsp;

New Reactor.SourceImpedance bus1=A\_internal.1.2.3 bus2=A.1.2.3

\~ Z0=\[0.025862916,0.077588748\] Z1=\[0.023094242,0.092376969\]

&nbsp;

Set voltagebases=\[13.8\]

Calcvoltagebases

&nbsp;

Solve&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Keep Your Sensitive PDFs Safe with These Easy Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
