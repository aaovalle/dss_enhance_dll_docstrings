# Capacitor

&nbsp;

&nbsp;

The capacitor model is basically implemented as a two-terminal power delivery element. However, if you don't specify a connection for the second bus, it will default to the 0 node (ground reference) of the same bus to which the first terminal is connected. That is, it defaults to a grounded wye (star) shunt capacitor bank.

&nbsp;

These connection rules also apply to Vsource, Reactor, and Fault elements.

&nbsp;

![Image](<lib/NewItem122.png>)\
Figure 1: Definition of Capacitor Object

&nbsp;

If you specify the connection to be "delta" then the second terminal is eliminated.

&nbsp;

If you wish a series capacitor, simply specify a second bus connection.

&nbsp;

If you wish an ungrounded wye capacitor, set all the second terminal conductors to an empty node on the first terminal bus, e.g.:

&nbsp;

...Bus1=B1 bus2 = B1.4.4.4 \! for a 3-phase capacitor

&nbsp;

Of course, any other connection is possibly by explicitly specifying the nodes.

&nbsp;

While the Capacitor object is frequently treated as if it were a single capacitor bank, it is actually implemented as a multistep tuned filter bank. Many of the properties can be specified as arrays. See Numsteps property.

&nbsp;

If you wish to represent a filter bank, specify either the XL or Harm property. When a Capcontrol object switches a capacitor, it does so by incrementing or decrementing the active step.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
