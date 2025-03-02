# Example 2

This example shows how to define a voltage source with different connections.

## &#49;.1.1 Delta-Connected

A voltage source can be specified as delta-connected by setting the terminal connections with the full node order bus specification, and properly assigning the adjacent nodes for each phase. In the example below, the bus order specification A internal.1.2.3 for the 1st terminal and A internal.2.3.1 for the 2nd terminal indicates that the first phase of the three-phase voltage source is connected to nodes 1 and 2 of bus A, whereas the second phase is connected between nodes 2 and 3, and so on.

Since the impedances are connected in series with the ideal voltage source in each phase, the impedances in the *VSource* element must be set to a very low value, while the actual impedances of the source must be modeled with a separate element, for example, a reactor, as shown in Figure 7. Note that an auxiliary bus was added between he *VSource* and the reactor. Also note that the *basekv* parameter must be multiplied by sqrt(3) because a wye connection is assumed by default, i.e., *basekv* is divided by sqrt(3) internally to determine the rated voltage in each phase.

&nbsp;

![Image](<lib/NewItem338.png>)

**Figure 7: 3-Phase Delta-Connected *Vsource* Element**

&nbsp;

New Circuit.TheveninEquivalent bus1=A\_internal.1.2.3 bus2=A\_internal.2.3.1 pu=1.1

\~ basekv=(13.83sqrt\*) Z0=\[0.000001,0.000001\] Z1=\[0.000001,0.000001\]

&nbsp;

New Reactor.SourceImpedance bus1=A\_internal.1.2.3 bus2=A.1.2.3

\~ Z0=\[0.025862916,0.077588748\] Z1=\[0.023094242,0.092376969\]

&nbsp;

Set voltagebases=\[13.8\]

Calcvoltagebases

&nbsp;

Solve&nbsp;

&nbsp;

## &#49;.1.2 Wye-Connected, with a grounding impedance

&nbsp;

A voltage source with a grounding impedance might be useful when considering a Wye-connected transformer’s winding as the voltage source of the model where the winding is grounded with an impedance. In this case, all is needed is to connect all phases of the 2nd terminal to a separate node, which is also connected to the element modeling the grounding impedance, as shown in Figure 8. In the example below, a reactor is used for that purpose.

![Image](<lib/NewItem339.png>)

**Figure 8: 3-Phase Wye-Connected *Vsource* Element Grounded through Impedance**

&nbsp;

New Circuit.TheveninEquivalent bus1=A bus2=A.4.4.4 pu=1.1 basekv=13.8

\~ Z0=\[0.025862916,0.077588748\] Z1=\[0.023094242,0.092376969\]

&nbsp;

New Reactor.Rg bus1=A.4 bus2=A.0 phases=1

\~ R=10 \!10Ohmsgroundingresistance

&nbsp;

Set voltagebases=\[13.8\]

Calcvoltagebases

&nbsp;

Solve&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Elevate your documentation to new heights with HelpNDoc's built-in SEO](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
