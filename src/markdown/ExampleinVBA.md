# Example in VBA

&nbsp;

**EXAMPLE IN VISUAL BASIC**

&nbsp;

The code presented below is identical to the snippets presented throughout this chapter. It is provided in one convenient location for reference.

&nbsp;

&nbsp;

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

' \* Initialize OpenDSS

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

' Declare the OpenDSS related variables

Dim DSSObj As OpenDSSengine.DSS

Dim DSSText As OpenDSSengine.Text

Dim DSSCircuit As OpenDSSengine.Circuit

Dim DSSSolution As OpenDSSengine.Solution

' Instantiate the OpenDSS Object

DSSObj = New OpenDSSengine.DSS

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

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

' \* Examples Using the DSSText Object

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

' Load in an example circuit

DSSText.Command = "Compile 'C:\\example\\IEEE123Master.dss'"

' Create a new capacitor

DSSText.Command = "New Capacitor.C1 Bus1=1 Phases=3 kVAR=1200"

DSSText.Command = "~ Enabled=false" ' You can even use ~

' Change the bus for Line L1

DSSText.Command = "Line.L1.Bus1 = 5"

' Export voltage to a csv file

Dim Filename As String

DSSText.Command = "Export Voltages"

Filename = DSSText.Result

MsgBox("File saved to: " \& Filename)

&nbsp;

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

' \* Examples Using the DSSCircuit Object

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

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

' Set a capacitor's rated kVAR to 1200

DSSCircuit.SetActiveElement("Capacitor.C83")

DSSCircuit.ActiveDSSElement.Properties("kVAR").Val = 1200

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

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

' \* Examples Using the DSSSolution Object

' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

' Solve the Circuit

DSSSolution.Solve()

If DSSSolution.Converged Then

MsgBox("The Circuit Solved Successfully")

End If

&nbsp;

' Model effects of a large load pickup 30 seconds into a simulation

DSSText.Command = \_

"New Monitor.Mon1 element=Line.L100 mode=0"

DSSSolution.StepSize = 1 ' Set step size to 1 sec

DSSSolution.Number = 30 ' Solve 30 seconds of the simulation

' Set the solution mode to duty cycle, which forces loads to use their

' "duty cycle" loadshape and allows time based simulation

DSSSolution.Mode = OpenDSSengine.SolveModes.dssDutyCycle

DSSSolution.Solve()

&nbsp;

DSSCircuit.Enable("Load.L1") ' Enable the load

DSSSolution.Number = 30 ' Solve another 30 seconds of simulation

DSSSolution.Solve()

&nbsp;

MsgBox("Seconds Elapsed: " \& DSSSolution.Seconds)

' Plot the voltage for the 60 seconds of simulation

DSSText.Command = "Plot monitor object=Mon1 Channels=(1,3,5)"

***
_Created with the Standard Edition of HelpNDoc: [Easy EBook and documentation generator](<https://www.helpndoc.com>)_
