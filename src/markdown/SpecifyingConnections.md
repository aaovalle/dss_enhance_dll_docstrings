# Specifying Connections

&nbsp;

&nbsp;

The user can define how terminals are to be connected to buses in three ways, not just one way:&nbsp;

&nbsp;

• Generically connect a circuit element’s *terminal* to a *bus* without specifying node-to-conductor connections. This is the default connection. Normal phase sequence is assumed. Phase 1 of the terminal is connected to Node 1 of the Bus, and so on. Neutrals default to ground (Node 0).&nbsp;

• Explicitly specify the first phase of the device is connected to node *j* of the bus. The remaining phases are connected in normal 3-phase sequence (1-2-3 rotation). Neutral&nbsp; conductors default to ground (Node 0).&nbsp;

• Explicitly specify the connection for all phases of each terminal. Using this mode, neutrals (star points) may be left floating. Any arbitrary connection maybe achieved. The syntax is:&nbsp;

&nbsp;

BUSNAME.*i.j.k* where i, j, k refer to the nodes of a bus.&nbsp;

&nbsp;

This is interpreted as the first conductor of the terminal is connected to node i of the bus designated by BUSNAME; the 2nd conductor is connected to node j, etc.&nbsp;

&nbsp;

The default node convention for a terminal-to-bus connection specification in which the nodes are not explicitly designated is:&nbsp;

&nbsp;

BUSNAME.1.0.0.0.0.0.0. … (Single-phase terminal)&nbsp;

BUSNAME.1.2.0.0.0.0.0. … (two-phase terminal)&nbsp;

BUSNAME.1.2.3.0.0.0.0 … (3-phase terminal)&nbsp;

&nbsp;

If the desired connection is anything else, it must be explicitly specified. Note: a bus object "learns" its definition from the terminal specifications. Extra nodes are created on the fly as needed. They are simply designations of places to connect conductors from terminals. For a 3-phase wye-connected capacitor with a neutral reactor, specify the connections as follows:

&nbsp;

BUSNAME.1.2.3.4 {for 3-phase wye-connected capacitor}&nbsp;

BUSNAME.4 {for 1-phase neutral reactor (2nd terminal defaults to node 0)}
***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of HelpNDoc for CHM Help File Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
