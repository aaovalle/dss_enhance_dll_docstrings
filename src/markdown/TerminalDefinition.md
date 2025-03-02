# Terminal Definition

&nbsp;

&nbsp;

Each electrical element in the power system has one or more terminals. Each terminal has one or more conductors. The conductors are numbered \[1, 2, 3,…\]. Each conductor conceptually contains a disconnect switch that can be controlled by a control element (the fuse shown in the figure below has been deprecated from the model). Fuses, relays, and reclosers are modeled as control elements that monitor terminal currents and then open or close switches. Thus, it is not necessary to insert an explicit switch element, which increases the problem size.&nbsp;

&nbsp;

If the terminal is connected to an N-phase device, the first N conductors are assumed to correspond to the phases, in order. The remaining conductors may be virtually any other conductor but are frequently neutrals or other non-power conductors.&nbsp;

&nbsp;

The OpenDSS bus is a connecting place with 1 or more nodes for connecting individual phases and other conductors from the terminals of both power delivery elements and power conversion elements.

&nbsp;

![Image](<lib/NewItem19.png>)\
Figure 1: Terminal Definition (Note: the fuse has been deprecated)&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
