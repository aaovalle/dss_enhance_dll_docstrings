# Zig-zag Transformer

&nbsp;

**Zig-zag Transformer**

&nbsp;

***How to Define a Zig-Zag Transformer***

&nbsp;

Here is a nice, compact script for modeling a zigzag transformer courtesy of Bob Arritt:

&nbsp;

New Transformer.ZZ1A phases=1 buses=\[B1.1.5 B1.4.7\] conns=\[delta delta\] kVs=\[11 11\] kvas=\[920.4 920.4\] XHL=0.468

New Transformer.ZZ1B phases=1 buses=\[B1.2.6 B1.4.5\] conns=\[delta delta\] kVs=\[11 11\] kvas=\[920.4 920.4\] XHL=0.468

New Transformer.ZZ1C phases=1 buses=\[B1.3.7 B1.4.6\] conns=\[delta delta\] kVs=\[11 11\] kvas=\[920.4 920.4\] XHL=0.468

&nbsp;

\! ZZ1 Neutral

New Reactor.ZZ1 phases=1 bus1=B1.4 R=23.8 X=0 \! 0.001

&nbsp;

In this script everything is connected to the same bus at different nodes. The main conductors are 1, 2, 3 and 4 (the neutral end). Nodes 5, 7 are used for the internal connections. The transformer is to be applied to a 33 kV system. This the kV rating of each single phase winding is 33 kV / 3 = 11 kV. You can also do this by connecting the winding to different buses and then use short jumpers (LINE or REACTOR) to accomplish the connection. However, the definition shown works just fine and it is not necessary to use two buses.

&nbsp;

***Alternative***

&nbsp;

If only the zero sequence behavior need be modeled, and you are not serving any load off the zigzag, you can get the same effect with a simple 2-winding YgD transformer.

&nbsp;

For example, a definition that is equivalent to the one above in terms of zero sequence impedance is:

&nbsp;

New Transformer.ZZ phases=3 buses=\[B1.1.2.3.4 B1.5.6.7\] conns=\[Wye delta\] kVs=\[33 16.4\] kvas=\[2761 2761\] XHL=0.468

\! ZZ1 Neutral

New Reactor.ZZ1 phases=1 bus1=B1.4 R=23.8 X=0 \! 0.001

&nbsp;

The voltage rating of the delta winding is irrelevant.

***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation Process with HelpNDoc's Advanced Features](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
