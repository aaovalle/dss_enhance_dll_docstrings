# DynamicExp

&nbsp;

DynamcExp (dynamic expressions), is an element that can be used for describing differential equations in OpenDSS. These equations can be used for describing the dynamic behavior of a PCE directly from the script. The description is done by using standard RPN notation (see RPN Expressions) plus some extra symbols that are used for identifying the beginning and end of an equations.

&nbsp;

The properties of the DynamicExp object are as follows:

&nbsp;

| NVariables&nbsp; | Number of state variables within the differential equation. |
| --- | --- |
| VarNames | Array of strings containing the names of the state variables to be consider within the differential equation. |
| Var | The name of the active state variable, it can be used to obtain the values of a particular variable. |
| VarIdx | (read only) Returns an integer indicating the index of the active state variable (activated with the Var property). If there is no state variable active, returns -1. |
| Expression | Use this property for writing the differential equation. The equation must be contained within brackets and each equation must be separated by semicolon character (;). |


&nbsp;

The differential equation described within an DynamicExp object preserves most of the notation and variable distribution, for example, consider the following set of swing equations used for describing the dynamcis of a generator (single mass).

&nbsp;

![Image](<lib/eq52.png>)

&nbsp;

These equations can be described using DynamicExp as follows:

&nbsp;

New DynamicExp.myDiffEq nvariables=6

\~ varnames=\[Speed Mass PShaft Pterm Damp theta\]

\~ expression=\[Speed dt = 1 Mass / (Pshaft Pterm - Damp Speed \* -) \*;&nbsp;

theta dt = Speed\]

&nbsp;

As can be seen in the declaration above, the only variants to the RPN expressions are the operands dt and =. The first one is used for determining the variable where the calculation of the derivative will be placed, the second one, separates the output variable from the rest of the expression. This declaration serves for describing multiple equations correlated. The equivalent block diagram is as shown in Figure 41.

&nbsp;

![Image](<lib/NewItem121.png>)

Figure 41. Equivalent block diagram for differential equations proposed

&nbsp;

Once the DynamicExp is defined it can be assigned and initialized from a PCE to describe its dynamic (electromechanical) behavior. This behavior will be evident only during dynamics simulation mode. For example, consider the following generator declaration in which the DynamicExp myDiffEq declared above

&nbsp;

New Generator.G1 Bus1=LT kV=24 kW=(2220000 0.9 \*) kvar=(2220000 0.436 \*) Model=1 vminpu= 0.80 Vmaxpu=1.4 DynamicEq=myDiffEq

\~ MVA=2220 XRdp=1e12 Xdp=0.3 Xdpp=0.25

// Initializes the dynamic equation's state variables

\~ Damp = 0 PShaft = P0 Pterm = P Speed = 0 theta = Edp

\~ Mass = (3.5 2 \* 2220000000 376.99112 / \*)

\~ DynOut = \[Speed theta\]

&nbsp;

As can be seen in the declaration for the generator, the DynamicExp is assigned to the generator G1 (if not, the generator will use the built-in equations in dynamics simulation mode) using the property DynamicEq. The variable initialization comes next. The initialization can be done using constants or by assigning a value calculated at the end of the simulation time step. The calculated values that can be use for initialization/assignment are as follows:

&nbsp;

| **Value tag** | **Description** |
| --- | --- |
| P | It is the active power at the terminal of the PCE |
| Q | It is the reactive power at the terminal of the PCE |
| VMag | It is the magnitude of the voltage at the terminals of the PCE. If the PCE is multiphase, the value assigned is the voltage magnitude for the phase reporting the highest value. |
| VAng | It is the phase angle (deg) of the voltage at the terminals of the PCE. If the PCE is multiphase, the value assigned is the voltage angle for the phase reporting the highest value. |
| IMag | It is the magnitude of the current at the terminals of the PCE. If the PCE is multiphase, the value assigned is the current magnitude for the phase reporting the highest value. |
| IAng | It is the angle of the current at the terminals of the PCE. If the PCE is multiphase, the value assigned is the current angle for the phase reporting the highest value. |
| P0 | t is the same as P but it will only use for initialization purposes. |
| Q0 | It is the same as Q but it will only use for initialization purposes. |
| mod | Internal modulation signal (for IBRs only). |
| kVDC | DC link rating (for IBRs only) |


&nbsp;

Finally, the outputs to be used to fed in the generator’s dynamic variables are defined with the property DynOut. In the case of the generator, the dynamic variables are the speed and angle, which are used for describing the angular speed of the rotor. The outputs need to be indicated in that same order, first, the variable used for storing the speed value and then, the name of the variable used for storing the angle value, both as the result the integration of the expression declared at myDiffEq.

&nbsp;

The number and order of variables requiring inputs from differential equations vary depending on the models. Check on the model’s reference to findout what are those variables and their assignment order.

&nbsp;

Also consider naming the variables to be used within the DynamicExp with names that are not similar or the same as the properties of the element they will be linked to. This will prevent OpenDSS from assigning values to the PCE properties instead of state variables.

&nbsp;

For example, consider using DynamicExp with an Inverter-based resource (IBR) such as a PV system. In this case, the equation to implement is as follows:

&nbsp;

![Image](<lib/eq54.png>)

&nbsp;

This equation can be implemented using DynamicExp as follows:

&nbsp;

New DynamicExp.myDiffEq nvariables=4 varnames=\[it vdc modul vac\]

\~ expression=\[it dt = 1 0.61059E-3 / ( -0.230187 it \* modul vdc \* + vac - ) \*\]

&nbsp;

In this case, R and LS representing the RL series filter for the inverter (See OpenDSS Dynamic mode) are represented as constants in ohms and Henrys, 0.230187 Ohms and 0.61mH respectively. Then, for assigning this expression to a PV system, this can be declared as follows:

&nbsp;

New "PVSystem.mypv" phases=3 conn=wye bus1=PVBus daily=pvshape kv=0.48 kVA=500 Pmpp=500 kVDC=0.600 %R=50 %X=50 kP=0.05 KVDC=0.600 PITol=1

\~ DynamicEq=myDiffEq

\~ it = IMag vdc = kKVDC modul=mod vac = VMag

\~ DynOut = \[it\]

&nbsp;

The dynamic output for IBRs in OpenDSS is current, which differs from the outputs declared for rotating machines such as the generator. Other parameters such as the DC link nominal value, proportional control value and tolerance are unique to IBR models for dynamics simulation, see OpenDSS Dynamics Mode document for details.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily create EBooks](<https://www.helpndoc.com/feature-tour>)_
