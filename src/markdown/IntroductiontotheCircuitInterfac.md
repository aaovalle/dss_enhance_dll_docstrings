# Introduction to the Circuit Interface

&nbsp;

The circuit interface is commonly used to edit the properties of the various elements in a circuit. Nearly all the element classes in OpenDSS (ie, Lines, Loads, Capacitors, CapControls, etc…) have a child object under the circuit interface. These child objects also have convenient functions to allow one to iterate through the member elements which are useful when looping. For example, this script will loop through all the loads in a circuit and scale the kW up by 20%:

&nbsp;

' Step through every load and scale it up

Dim iLoads As Integer ' Track what load we're on

&nbsp;

iLoads **=** DSSCircuit.Loads.First

While iLoads

' Scale load by 120%

DSSCircuit.Loads.kW **=** DSSCircuit.Loads.kW \* 1.2

' Move to next load

iLoads **=** DSSCircuit.Loads.Next

End While

&nbsp;

If one wants to edit a specific element, use the SetActiveElement method and the ActiveDSSElement interface as shown below:

&nbsp;

' Set a capacitor's rated kVAR to 1200

DSSCircuit.SetActiveElement("Capacitor.C83")

DSSCircuit.ActiveDSSElement.Properties("kVAR").Val = 1200

&nbsp;

However, the benefit of this method over simply using the text interface, as shown below, is debatable. Use whichever method makes sense to you.

&nbsp;

' Does the same thing as the previous snippet

DSSText.Command = "Capacitor.C83.kVAR = 1200"

&nbsp;

Another useful feature of the Circuit Interface is to retrieve power flow results, such as bus voltages, element losses, etc… This example gets the bus names and voltages:

&nbsp;

' Get bus voltages

Dim BusNames As String()

Dim Voltages As Double()

BusNames = DSSCircuit.AllBusNames

Voltages = DSSCircuit.AllBusVmagPu

&nbsp;

' See what an arbitrary bus's voltage is

MsgBox(BusNames(5) \& "'s voltage mag in per unit is: " \& Voltages(5))

&nbsp;

For more on getting power flow results from the circuit interface, see the “All commands” (AllElementLoses, AllNodeVmagByPhase, etc…) in the COM Interface section.

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Workflow with HelpNDoc's Intuitive UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
