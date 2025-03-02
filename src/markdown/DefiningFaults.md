# Defining Faults

&nbsp;

***Fault Object Topology***

&nbsp;

The Fault object in OpenDSS is simply a two-terminal multiphase resistor. At its simplest, it is a simply a from-to branch with a resistor in each phase specified by the R property. The default value for R, if not specified is 0.1 milliohms, which represents a nearbolted fault. It is not possible to specify a zero resistance fault in OpenDSS because the resistive network must be represented by an admittance. The figure below depicts the concept for a simple 3phase Fault object.

&nbsp;

![Image](<lib/NewItem35.png>)

&nbsp;

At its most complex, the resistive network is specified as a nodal conductance matrix (Gmatrix property), which can theoretically represent any resistive network between the two terminals.

Since the Fault object is simply a resistive network, it may be used to model more than just short circuit faults. You can use it for a series resistance between two buses. You can use it to represent a resistive load, although it will not be tabulated as a load. Of course, you can do this with a Reactor, too by setting X=0.

&nbsp;

***Connection Rules***

&nbsp;

The connection rules for Fault objects are the same as for Capacitor and Reactor objects. When the Bus1 property is specified, the Bus2 property defaults to Node 0 of the same bus. That is, the Fault defaults to a line-to-ground connected object. To achieve other types of faults, the user specifies the Bus2 property. Several examples follow.

&nbsp;

***Single Line-to-Ground Fault***

&nbsp;

The default Fault object is a single line-to-ground fault. The example below of a SLG fault connected to MyBus, phase 3, can be defined by:

&nbsp;

New Fault.MySLGFault phases=1 Bus1=MyBus.3

&nbsp;

![Image](<lib/NewItem36.png>)

&nbsp;

The Bus2 property defaults to MyBus.0. Thus, the fault represents a fault to ground (the zero volt reference).

&nbsp;

***Single Phase Line-to-Neutral Fault***

&nbsp;

If the fault were to represent a single-phase fault to a neutral conductor that is explicitly modeled instead of ground (earth), you would have to explicitly define the Bus2 property. For example, if the neutral wire were connected to MyBus.4, you would specify Bus2=MyBus.4

&nbsp;

New Fault.MySLNFault phases=1 Bus1=MyBus.3 Bus2=MyBus.4

&nbsp;

![Image](<lib/NewItem37.png>)

&nbsp;

***Line-to-Line Fault***

&nbsp;

It might seem logical to declare a LineLine fault as a 2-phase Fault object because the fault involves two phases. However, it is simply a 1phase fault connected between two phases of the same bus. For example, a LL fault between Phases 2 and 3 would be declared:

&nbsp;

New Fault.MyLLFault phases=1 Bus1=MyBus.2 Bus2=MyBus.3

&nbsp;

![Image](<lib/NewItem38.png>)

&nbsp;

***&#50; Line-to-ground Faults***

&nbsp;

The simplest way to declare a 2-line-to-ground fault is to declare the Fault object to be a 2-phase element. This will connect a small resistance from each phase to ground

&nbsp;

New Fault.MyLLGFault phases=2 Bus1=MyBus.2.3

&nbsp;

The Bus2 property defaults to MyBus.0.0. This Fault is represented schematically:

&nbsp;

![Image](<lib/NewItem39.png>)

&nbsp;

This works fine for low impedance faults. If you wanted to represent different resistances L-L and then to ground, you have a couple of options:

&nbsp;

&#49;. You can define two separate single-phase Fault objects connected appropriately.

&#50;. Use the Gmatrix property to define a nodal conductance matrix that represents the fault resistances.

&nbsp;

To demonstrate the latter, let's assume you want to represent a 2-ohm fault between phases 2 and 3 and then a 10-ohm fault from phase 3 to ground with the connections illustrated in this figure:

&nbsp;

![Image](<lib/NewItem40.png>)

&nbsp;

The conductance between phases 2 and 3 is (1/2) = 0.5 S. The conductance to ground from phase 3 is 0.1 S. The G matrix would be:

&nbsp;

![Image](<lib/eq9.png>)

&nbsp;

The diagonal elements of G are the sum of all conductances connected to the node represented by the row. The offdiagonal elements are the negative of the conductances between the nodes represented by the rows. In this example, there is 0.5 S between the two nodes and 0.1 S between the second node and ground. Therefore, there is a total of 0.5 + 0.1 = 0.6 S for the diagonal for the second node.

&nbsp;

Define the Fault object as 2 phases, which will then expect a 2x2 matrix for the Gmatrix property (entered as lower triangle).

&nbsp;

New Fault.MyOtherLLGFault phases=2 Bus1=MyBus.2.3 Gmatrix=\[0.5 \| -0.5 0.6\]

&nbsp;

Let the Bus2 property default to MyBus.0.0. This will give the desired effect with the specified Gmatrix. This is the way the Fault object is currently programmed.

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easy Qt Help documentation editor](<https://www.helpndoc.com>)_
