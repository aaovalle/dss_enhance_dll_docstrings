# Control Elements 

&nbsp;

One of the distinctive capabilities of the OpenDSS is that control elements are modeled separately from the power-carrying elements. This provides significant flexibility to create new models. Initially, control objects reflected only standard utility distribution system control devices. More recently, new, innovative models have been developed. Currently, there are nine controls provided with the program with more planned soon. This section gives some idea of how the control objects work and how you might exploit them.

&nbsp;

Control elements are polled after a power flow solution has been obtained. If any control needs to operate, it places a message on the Control Queue. When it comes time for the control to operate, the message is popped off the queue and the command executed. This allows for the simulation of controls that have time delays in their operation.

&nbsp;

The typical execution of the Solve command for a single snapshot power flow solution is:

&nbsp;

&#49;. Initialize Snapshot (\_InitSnap)

&#50;. Repeat until converged:

a. Solve Circuit (\_SolveNoControl)

b. Sample control devices (\_SampleControls)

c. Do control actions, if any (\_DoControlActions)

&nbsp;

The names in parentheses after the step is the corresponding command (see command reference above) that you would use if you wanted to “roll your own” solution method.

&nbsp;

Control elements typically have a Sample function that samples the voltage and current at the terminal that the control is monitoring. Each element of the Control element class also has a DoPendingAction function that is called from the control queue at the appropriated time. The Control element then takes the prescribed action or decides that it doesn’t need to (as is the case for many distribution system controls).

&nbsp;

&nbsp;

See Controls in the OpenDSS TechNotes and documentation section for further information and application examples&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your CHM Help File Capabilities with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
