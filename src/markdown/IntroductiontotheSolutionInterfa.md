# Introduction to the Solution Interface

&nbsp;

The Solution Interface is used to monitor and control the OpenDSS solution process and control procedures. This includes solving the circuit, setting the solution mode, monitoring convergence, reporting the time interval for time and duty based solution, and other such

aspects of solving an OpenDSS circuit.

&nbsp;

At its most fundamental level, the solution interface allows one to solve the circuit:

&nbsp;

' Solve the Circuit

DSSSolution.Solve()

If DSSSolution.Converged Then

MsgBox("The Circuit Solved Successfully")

End If

&nbsp;

One can also control the solution at a more granular level. For example, say one wanted to model the effects of a large load pickup 30 seconds into a simulation. The code below could be used:

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

&nbsp;

Finally, the circuit interface grants very specific information into the method and control behind the solution. Using the various “Solve” methods (ex, Solve, SolveDirect, SolveNoControl, etc…) and other functions like SystemYChanged and MostIterationsDone, granular control of and information on the solution process can be obtained. Using CheckControls and other methods in the Solution Interface, along with the DSSCircuit.CtrlQueue interface, specialized control schemes can be implemented.

***
_Created with the Standard Edition of HelpNDoc: [Easily create CHM Help documents](<https://www.helpndoc.com/feature-tour>)_
