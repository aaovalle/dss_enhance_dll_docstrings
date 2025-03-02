# Using the Fault Object

&nbsp;

A Fault object is a constant-impedance power delivery circuit element almost like any other. The user simply applies the fault and solves. The result is the best approximation to the actual faulted condition that can be achieved for this fault given the load models, which may or may not be accurate for voltages outside the normal band. There are some conditions where faults are treated specially. For example, during the Fault Study mode (Mode=FAULTSTUDY), all fault objects are disabled. The Fault Study mode then computes fault currents with a different algorithm The Monte Carlo fault mode also alters fault objects.

The Fault model is basically implemented very similarly to the Capacitor or Reactor as a two-terminal power delivery element. The fault is nominally an uncoupled, multiphase resistance branch. You may also specify the fault as a nodal conductance (G) matrix, which will give you complete control over the definition for any complex fault situation, including coupling between the phases. You can use the Fault object to represent a two terminal resistance if you like, keeping in mind that some solution modes (e.g., FAULTSTUDY) may disable the element so that it is no longer in the circuit.

In Monte Carlo Fault mode, the fault resistance is varied by the % standard deviation specified. If the standard deviation is entered as zero (default), the resistance is varied uniformly.

Like the Capacitor, if you don't specify a connection for the second bus, it will default to the 0 node (ground reference) of the same bus to which the first terminal is connected. That is, it defaults to a grounded wye (star) shunt resistance.

&nbsp;

&nbsp;

&nbsp;

![Image](<lib/NewItem288.png>)

&nbsp;

Figure 1. Definition of Fault Object

&nbsp;

Unlike the capacitor, you cannot specify a delta connection. If you need one, simply make one using the terminal connections. You may also use the Gmatrix property to enter an arbitrary conductance matrix representing any connection you wish.

&nbsp;

If you wish to model a series uncoupled resistor, simply specify an appropriate second bus connection.

&nbsp;

If you wish to model an ungrounded wye resistor, set all the second terminal conductors to an empty node on the first terminal bus, e.g.:

&nbsp;

...Busl=Bl bus2 = Bl.4.4.4&nbsp; \! for a 3-phase ungrounded fault

&nbsp;

**Examples of Scripts for Using Fault Objects**

&nbsp;

A simple script:

&nbsp;

Compile circuitfile.txt \! Define the circuit

Solve

New fault.fl busl=xxx&nbsp; &nbsp; \! Defines a SLG Faukt

Solve

&nbsp;

Show currents \! Show currents in the fault and system

Show voltages LN Nodes&nbsp; \! Show voltages throughout the system

&nbsp;

This script applies a SLG fault at bus "xxx" on phase 1, since all the defaults were taken. The solution mode is generally SNAPSHOT at this point, so this is a quasi-power flow solution. The load and generator models will generally attempt to consume or produce the specified power unless the voltage drops too low. Then they revert to constant impedance models.

&nbsp;

An alternative for doing this solution is:

&nbsp;

Compile circuitfile.txt \!define the circuit

Solve

New fault.fl busl=xxx&nbsp; &nbsp; \! defines a SLG fault&nbsp;

Solve mode=dynamic number=l &nbsp; \! Do one time step in dynamics mode

&nbsp;

Show currents&nbsp; &nbsp; &nbsp; &nbsp; \! see currents in the fault and system&nbsp;

Show voltages&nbsp; &nbsp; &nbsp; &nbsp; \! voltages throughout the system

&nbsp;

This script also performs a solution for the specified fault, but switches to dynamic mode first. This forces the generator models to switch to voltage-behind-reactance models like those used in dynamic

simulations. They no longer attempt to force a particular power down the line, but simply act as voltage sources. This gives a better answer in most cases, although the previous method may be good enough. By doing only 1 solution step (number=\!), only the initial fault current is computed. This is generally the highest and is adequate for planning purposes.&nbsp;

.

If the generators employ a sophisticated dynamics model that changes with time, more solution steps can be executed in Dynamics mode to see the change in fault current with time.

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with HelpNDoc's User-Friendly UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
