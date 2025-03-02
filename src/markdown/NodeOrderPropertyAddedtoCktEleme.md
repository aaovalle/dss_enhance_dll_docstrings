# NodeOrder Property Added to CktElement Interface

&nbsp;

**NodeOrder Property Added to CktElement Interface**

&nbsp;

In version 7.6.3.20, the NodeOrder property was added to the CktElement interface to give the node number to which a conductor is connected. Corresponds to the array values returned in Voltages, Currents, and Powers property. Users must use NodeOrder as a key because there is no guarantee that the conductors are connected to the same phase, or node number, on each side of a line, for example. You could transpose a line by altering the connections. This was an omission from the COM interface that was brought to our attention by a user. This avoids users having to write code to parse the Busnames string array to gives the text form of the bus connections.

&nbsp;

Some sample VBA code:

&nbsp;

Set DSSCktElement = DSSCircuit.ActiveElement

DSSCircuit.SetActive "Line.MyLine"

V = DSSCktElement.NodeOrder

For i = lbound(V) to Ubound(V): Debug.Print V(i): Next i

&nbsp;

***Changes to Bus Interface***

&nbsp;

Also, in the Bus interface, the Voltages and puVoltages properties now return the values in order from lowest node number to highest. Also, the Nodes property, which is used to interpret the phase of the values, was modified to correspond to the order of the Voltages.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Make Documentation a Breeze with HelpNDoc's Clean and Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
