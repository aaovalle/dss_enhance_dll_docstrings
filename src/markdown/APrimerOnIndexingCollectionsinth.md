# A Primer On Indexing Collections in the DSS COM Circuit Interface

&nbsp;

***A Primer On Indexing Collections in the DSS COM Circuit Interface***

&nbsp;

The Circuit interface, for example, has a Buses collection and a CktElements collection. You can address a specific Bus or CktElement using an variant index (either a string or an integer):

&nbsp;

V = DSSobj.ActiveCircuit.CktElements("LINE.L2").SeqCurrents

&nbsp; &nbsp; -or-

V = DSSobj.ActiveCircuit.CktElements(idx).SeqCurrents

&nbsp;

Where idx is an integer index.

&nbsp;

This is faster than the first method because it doesn't have to search for LINE.L2. Note that this action sets the referenced element as the active element. To do another operation on the same element immediately, you would simply do: Vlosses = DSSobj.ActiveCircuit.ActiveElement.Losses.

&nbsp;

In VB, it is most efficient to assign a variable to the active circuit interface and then use a With clause:

&nbsp;

DSSCircuit = DSSobj.ActiveCircuit ...

With

DSSCircuit V = .CktElements(idx).SeqCurrents

Vlosses = .ActiveElement.Losses

' you could also keep a variable set to the ActiveElement because that is a fixed interface.

End With

&nbsp;

What integer do you use for idx? It is the zero-based absolute index of the element in the active circuit determined by the order in which the elements are defined. (Inside the DSS, nearly all arrays are 1..n. However, nearly all arrays returned by the COM interface are zero-based to avoid problems with C and VB.) You can get it by

&nbsp;

• idx = DSSobj.ActiveCircuit.SetActiveElement("LINE.L2") ' do this once and save the index

• Get all the circuit names and search for the one(s) you want, for example:

&nbsp;

Vnames = DSSobj.ActiveCircuit.AllElementNames

For i = lbound(Vnames) to ubound(Vnames)

If Vnames(i) = "LINE.L2" Then ' I think this will work in VB (may need to convert to same case)

V = DSSobj.ActiveCircuit.CktElements(i).SeqCurrents (….do something with the sequence currents and leave&nbsp;

End If

Next i

&nbsp;

Collections that are indexed this way (by either name or integer) include:

&nbsp;

Buses

CktElements

Properties

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
