# Phases and Other Conductors

&nbsp;

&nbsp;

Each terminal has one or more phases, or normal power-carrying conductors and, optionally, a number of other conductors to represent neutral, or grounding, conductors or conductors for any other purpose. By convention, if a device is declared as having N phases, the first N conductors of each terminal are assumed to be the phase conductors, in the same sequence on each terminal. Remaining conductors at each terminal refer to “neutral” or “ground” or "earth" conductors. However, the conductors can represent other power carrying conductors. There is no hard rule.&nbsp;

&nbsp;

*All terminals of a device are defined to have the same number of conductors*. For most devices, this causes no ambiguity, but for transformers with both delta and wye (star) winding connections, there will be an extra conductor at the delta-connected terminal. The neutral is explicit to allow connection of neutral impedances to the wye-connected winding. The extra conductor for the delta connection is simply connected to ground (voltage reference) and the admittances are all set to zero. Thus, the conductor effectively does not appear in the problem; it is ignored. However, you may see it appear in reports that explicitly list all the voltages and currents in a circuit.&nbsp;

&nbsp;

The terminal conductors and bus nodes may be combined to form any practical connection.&nbsp;

&nbsp;

*Buses have Nodes*: A bus may have any number of *nodes* (places to connect device terminal conductors). Nodes are integer numbers. The nodes may be arbitrarily numbered. However, the first N are by default reserved for the N phases of devices connected to them. Thus, if a bus has 3-phase devices connected to it, connections would be expected to nodes 1, 2, and 3. So the DSS would use these voltages to compute the sequence voltages, for example. Phase 1 would nominally represent the same phase throughout the circuit, although there is nothing to enforce that standard. It is up to the user to maintain a consistent definition. If only the default connections are used, the consistency is generally maintained automatically, although there can be exceptions.&nbsp;

&nbsp;

Any other nodes would simply be points of connection with no special meaning. Each Bus object keeps track of the allocation and designation of its nodes.&nbsp;

&nbsp;

Node 0 of a bus is always the voltage reference (a.k.a, ground, or earth). That is, it always has a voltage of exactly zero volts.
***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Publish Your Word Document as an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
