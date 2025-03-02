# TechNote Opening Switches

&nbsp;

***Opening Switches***

&nbsp;

There has been recent interest in how the Open command works. The scanned figure below describes the basic algorithm.

&nbsp;

![Image](<lib/NewItem74.png>)

&nbsp;

&nbsp;

![Image](<lib/eq10.png>)

&nbsp;

To open Terminal 1 at Bus , we force I1=0&nbsp;

&nbsp;

![Image](<lib/eq11.png>)

&nbsp;

Perform Kron Reduction to eliminate Row and Column 1&nbsp;

&nbsp;

![Image](<lib/eq12.png>) Where ![Image](<lib/eq13.png>)

&nbsp;

To prevent Bus 1 from being Inadvertly Isolated we connect a ![Image](<lib/eq14.png>) \[S\] to eah node of BUS 1 by replacling Y11 with a&nbsp; matrix with ![Image](<lib/eq14.png>) \[S\] on each diagonal. Now, the equation is&nbsp;

&nbsp;

![Image](<lib/eq35.png>)

&nbsp;

The circuit model for this is :&nbsp;

&nbsp;

![Image](<lib/NewItem75.png>)

&nbsp;

This example is for a 3-phase lines or reactors. However, the procedure is the same regardless of the number of phases or whether it has one terminal or 10 terminals.

&nbsp;

All circuit elements in OpenDSS are modeled by a "primitive Y" matrix. After the matrix is formed, a Kron reduction is performed for each conductor that is to be opened. This forces the current in that conductor to zero.

&nbsp;

The diagonal of the row and column being eliminated is replaced by a tiny admittance (1.0e12 + j0). This effectively places a high resistance to ground, which prevents the node from floating in case there is nothing else connected to it.

&nbsp;

One issue to remember with the Open command is that the voltage at the terminal being opened is no longer available. It is eliminated from the problem.

&nbsp;

***Open a Line By Reconnecting***

&nbsp;

Instead of using the Open command, you can simply reconnect the element to another bus or set of nodes. For example, if you had a Line object defined as

&nbsp;

New Line.MyLine1 Bus1=MyBus1.1.2.3 Bus2=MyBus2.1.2.3 Linecode=MyLinecode Length=5

&nbsp;

You can open terminal 1 by

&nbsp;

Line.MyLine1.Bus1=MyBus1.11.12.13

&nbsp;

This reconnects the first terminal to nodes 11, 12, and 13. Assuming nothing else is connected to these nodes, this will effectively open the line. One advantage of this is that the voltages at the open terminal nodes (MyBus1.11.12.13) are now available in addition to the voltages at MyBus1.1.2.3, if there was something else connected to nodes MyBus1.1.2.3. If not, these nodes will disappear from the problem until the Line object is reconnected.

&nbsp;

Using a High Impedance for an Open Switch

&nbsp;

This is usually done with a REACTOR object representing a switch. For example, a closed switch might have an impedance of (0.001 + j0) ohms. And an open switch might have a resistance of 100 Mohms. This will generally work, although you may have to adjust the resistance value if it causes numerical problems.

&nbsp;

An example script:

&nbsp;

New Reactor.Switch Bus1=TheFirstBus Bus2=TheSecondBus R=0.001 X=0 \! define the switch closed.

...

// open the switch

Reactor.Switch.R=1.0E8

...

// Close it again

Reactor.Switch.R=0.001

...

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
