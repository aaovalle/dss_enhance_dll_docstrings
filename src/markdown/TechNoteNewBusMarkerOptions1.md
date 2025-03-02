# TechNote New Bus Marker Options

&nbsp;

&nbsp;

***New Bus Marker Options***

&nbsp;

By request, some new or revised options are available for placing marks on buses on Circuit Plots.

&nbsp;

During the conversion to 7.6, the AddBusMarker command was temporarily disabled. The functionality has been restored, but it works a little differently. Previously you would add markers after the plot was created. Now, you define the markers for the bus BEFORE the circuit plot is created. The markers remain defined (they are persistent) until you clear them (ClearBusMarkers) or clear the circuit.

&nbsp;

It is OK to define markers for buses that do not exist. The definition is ignored.

&nbsp;

See below for available marker codes:

&nbsp;

***AddBusMarker***

&nbsp;

Add a marker to a bus in a circuit plot. Markers must be added before issuing the Plot command. Effect is persistent until circuit is cleared. See also ClearBusMarkers command. For example, you would execute a script like this sometime before executing a Plot Circuit command:

&nbsp;

ClearBusMarkers \!...Clears any previous bus markers

AddBusMarker Bus=Mybusname1 code=5 color=Red size=3

AddBusMarker Bus=Mybusname2 code=35 color=Blue size=4

... etc ...

&nbsp;

You can use any of the standard color names or RGB numbers. See Help on C1 property in Plot command.

&nbsp;

***Special Markers for Selected Classes***

&nbsp;

You can also define markers for certain classes of elements. Previously, there were options for Transformer objects and Switch objects. Now you can also mark Capacitors, Regulators, PVSystem, and Storage elements.

&nbsp;

Set MarkCapacitor=Yes

Set MarkRegulator=Yes

Set MarkPVSystem=Yes

Set MarkStorage=Yes

Set MarkSwitches=Yes

Set Markransformer=Yes

&nbsp;

You can also define a marker code if the default is insufficient:

&nbsp;

Set CapMarkerCode=37

Set RegMarkerCode=47

Set PVMarkerCode=15

Set StoreMarkerCode=9

Set TransMarkerCode=35

&nbsp;

Finally, you can change the size of the markers if the default size is too small or too large.

&nbsp;

Set CapMarkerSize=3

Set RegMarkerSize=3

Set PVMarkerSize=2

Set StoreMarkerSize=2

Set TransMarkerSize=1

&nbsp;

Note: you cannot change the Switch Marker Code or size

&nbsp;

***Standard Color Names***

&nbsp;

Standard color names are:

&nbsp;

•Black

•Maroon

•Green

•Olive

•Navy

•Purple

•Teal

•Gray

•Silver

•Red

•Lime

•Yellow

•Blue

•Fuchsia

•Aqua

•LtGray

•DkGray

•White

&nbsp;

***Available Marker Codes***

&nbsp;

![Image](<lib/NewItem55.png>)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily create EPub books](<https://www.helpndoc.com/feature-tour>)_
