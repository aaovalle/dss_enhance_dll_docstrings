# Export NodeNames 

&nbsp;

The Export NodeNames command has been added at version 7.6.3.20.

&nbsp;

This command is useful for creating script files where you need to do something with individual nodes. For example, you may want to populate the circuit with a bunch of SLG faults for a monte carlo fault study run (Solve mode=MF) for voltage sag analysis.

&nbsp;

This command mimics the DSSCircuit.AllNodeNames property in the COM interface.

&nbsp;

***Example:***

&nbsp;

Assume Export Nodenames yields: (from IEEE 8500 Node test feeder)

&nbsp;

m1009763.2

m1009763.1

m1009763.3

l2673322.2

m1069148.3

l2673309.3

m1069588.2

l2804270.2

m3036164.2

l2935553.2

m1209749.2

l2748840.2

m1108264.2

m1108263.2

l3085398.1

l3085398.2

l3085398.3

m1026891.1

m1026891.2

&nbsp;

Then you can manipulate the file with a text editor to quickly create a script placing 1phase faults at the selected nodes:

&nbsp;

New Fault.m1009763 Phases=1 Bus1=m1009763.2

New Fault.m1009763 Phases=1 Bus1=m1009763.1

New Fault.m1009763 Phases=1 Bus1=m1009763.3

New Fault.l2673322 Phases=1 Bus1=l2673322.2

New Fault.m1069148 Phases=1 Bus1=m1069148.3

New Fault.l2673309 Phases=1 Bus1=l2673309.3

New Fault.m1069588 Phases=1 Bus1=m1069588.2

New Fault.l2804270 Phases=1 Bus1=l2804270.2

New Fault.m3036164 Phases=1 Bus1=m3036164.2

New Fault.l2935553 Phases=1 Bus1=l2935553.2

New Fault.m1209749 Phases=1 Bus1=m1209749.2

New Fault.l2748840 Phases=1 Bus1=l2748840.2

New Fault.m1108264 Phases=1 Bus1=m1108264.2

New Fault.m1108263 Phases=1 Bus1=m1108263.2

New Fault.l3085398 Phases=1 Bus1=l3085398.1

New Fault.l3085398 Phases=1 Bus1=l3085398.2

New Fault.l3085398 Phases=1 Bus1=l3085398.3

New Fault.m1026891 Phases=1 Bus1=m1026891.1

New Fault.m1026891 Phases=1 Bus1=m1026891.2

&nbsp;

***Node Names:***

&nbsp;

You can get all bus names from Show Buses or Export Buscoords commands and parsing off the first column.

***
_Created with the Standard Edition of HelpNDoc: [Why Microsoft Word Isn't Cut Out for Documentation: The Benefits of a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
