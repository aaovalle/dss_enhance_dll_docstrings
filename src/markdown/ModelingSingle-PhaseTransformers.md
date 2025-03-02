# Modeling Single-Phase Transformers

&nbsp;

**Modeling Single-phase, Center-tapped Distribution Transformers**

&nbsp;

The question frequently arises concerning how to model the typical US-style single-phase distribution transformer with a 120/240V secondary. Since there is no special transformer model in the DSS for this device, it is constructed using a single-phase transformer with three windings (this is physically what the transformer is). The schematic of the model is as shown in the figure below.

&nbsp;

![Image](<lib/NewItem178.png>)

Center-Tapped 1-Phase Transformer Model

&nbsp;

First, note the polarities of the windings. The usual error is to not properly connect Winding 3. It must be connected between Node 0 of Bus2 and Node 2, in that order.

&nbsp;

This transformer may be modeled by the following scripts. The first script is for a Line-to-neutral connected transformer on Phase 1; the second is a Line-to-Line connected transformer between phases 1 and 2.

&nbsp;

\! Line-to-Neutral Connected 1-phase Center-tapped transformer

&nbsp;

New Transformer.Example1-ph phases=1 Windings=3

\~ Xhl=2.04 Xht=2.04 Xlt=1.36 %noloadloss=.2

\~ Buses=\[bus1.1 bus2.1.0 bus2.0.2\] \!\!\! Note polarity

\~ kVs=\[7.2 .12 .12\] \! ratings of windings

\~ kVAs=\[25 25 25\]

\~ %Rs = \[0.6 1.2 1.2\]

\~ conns=\[wye wye wye\] \! default

&nbsp;

\! Line-to-Line Connected 1-phase Center-tapped transformer

&nbsp;

New Transformer.Example1-ph phases=1 Windings=3

\~ Xhl=2.04 Xht=2.04 Xlt=1.36 %noloadloss=.2

\~ Buses=\[bus1.1.2 bus2.1.0 bus2.0.2\] \!\!\! Note polarity

\~ kVs=\[12.47 .12 .12\] \! ratings of windings

\~ kVAs=\[25 25 25\]

\~ %Rs = \[0.6 1.2 1.2\]

\~ conns=\[delta wye wye\]

&nbsp;

Note that the winding voltage ratings are defined on the actual coil rating.

&nbsp;

The next point of confusion is what to assume for the impedances of the 3-winding transformer and the winding resistances. Some errors often occur when users attempt to take the default values. Some recommendations:

&nbsp;

&#49;. Do not take the default short-circuit reactance values; the default values are designed for a typical large power transformer that has 3 windings, such as a Y-D connection. The impedances to the 3rd winding are too large (30 and 35%) for a typical distribution transformer. Use the values in the example if you don’t know exactly what they are.

&nbsp;

&#50;. Do not use “%loadloss=…” to set the winding resistances. This property sets only windings 1 and 2. Explicitly set the winding resistances to avoid confusion.

&nbsp;

The impedance in the example above more closely represent a Core form, interlaced connection (see the figure below from Tom Short’s book). Note that the LV windings are close together and are inside the HV winding. Short circuit reactance is a function of the spacing between the windings. The greater the spacing, the higher the reactance. In Shell form designs, one LV winding is wound outside the HV winding while the other is inside. Therefore, the impedancebetween the two low voltage windings (XLT=) is likely higher than the percent impedance between either one of the LV windings to the HV winding. In both cases, the typical HV-LV impedance with be on the order of 2-3% for most distribution transformers.

&nbsp;

![Image](<lib/NewItem179.png>)

Common distribution transformer winding constructions.

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Make Documentation a Breeze with HelpNDoc's Clean and Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
