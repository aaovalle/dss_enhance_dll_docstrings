# Starting out With the COM Interface 

&nbsp;

&nbsp;

First of all, make sure that the programming environment you are using is connected to the OpenDSS COM interface. In Visual Basic, this is done by going to Tools \> References or Project \> Add Reference depending on what version you are using. From here, select the OpenDSSEngine COM type library.

&nbsp;

To instantiate an OpenDSS object and create a link to commonly used functions, use the following code:

&nbsp;

' Declare the OpenDSS related variables

Dim DSSObj As OpenDSSengine.DSS

Dim DSSText As OpenDSSengine.Text

Dim DSSCircuit As OpenDSSengine.Circuit

Dim DSSSolution As OpenDSSengine.Solution

&nbsp;

' Instantiate the OpenDSS Object

DSSObj = New OpenDSSengine.DSS

&nbsp;

' Start up the Solver

If Not DSSObj.Start(0) Then

MsgBox("Unable to start the OpenDSS Engine")

Return

End If

&nbsp;

' Set up the Text, Circuit, and Solution Interfaces

DSSText = DSSObj.Text

DSSCircuit = DSSObj.ActiveCircuit

DSSSolution = DSSCircuit.Solution

&nbsp;

As can be seen, from the DSS parent object several useful children classes exist. These are

&nbsp;

 The Text interface, which provides access to the command line interpreter interface. Using this object, one can directly execute OpenDSS scripting commands, as found in the previous section “The Basics of the OpenDSS Scripting Language.”

&nbsp;

 The Circuit interface, which provides access to the elements that make up the circuit. Using members of this object, one can iterate through, edit, and monitor various circuit elements.

&nbsp;

 The Solution interface, which provides access to the solution. Using members of this object, one can define solution parameters, solve the circuit, and view properties of the solution, like the number of iterations it took. The next several sections will take a more in‐depth look at these interfaces.

&nbsp;

The next several sections will take a more in‐depth look at these interfaces.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Single source CHM, PDF, DOC and HTML Help creation](<https://www.helpndoc.com/help-authoring-tool>)_
