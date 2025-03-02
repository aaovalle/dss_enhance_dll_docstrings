# Generator 

&nbsp;

&nbsp;

&nbsp;

A Generator is a Power Conversion element similar to a Load object. Its rating is basically defined by its nominal kW and PF or its kW and kvar. Then it may be modified by a number of multipliers, including the global circuit load multiplier, yearly load shape, daily load shape, and a dutycycle load shape.

&nbsp;

For power flow studies, the generator is essentially a negative load that can be dispatched. For Harmonics mode, the generator is converted to a voltage source behind the value specified for Xd” that approximately matches the power flow solution. For dynamics mode, the generator is converted to a voltage source behind an impedance with the impedance dependent on the model chosen.

&nbsp;

If the dispatch value (DispValue property) is 0, the generator always follows the appropriate dispatch curve, which is simply a Loadshape object. If DispValue\>0 then the generator only comes on when the global circuit load multiplier exceeds DispValue. When the generator is on, it always follows the dispatch curve appropriate for the type of solution being performed.

&nbsp;

If you want to model a generator that is fully on whenever it is dispatched on, simply designate "Status=Fixed". The default is "Status=Variable" (i.e., it follows a dispatch curve. You could also define a dispatch curve that is always 1.0.

&nbsp;

The Generator object is an excellent host for user-defined PCElement models supplied as User-written DLLs (generator model=6). You can use this to research models of various DER elements that produce power as well as those that consume power for which specific OpenDSS models do not exist. A template is provided with the installation of the OpenDSS program in the IndMach012a.DLL. The source code for this DLL is available.

&nbsp;

Generators have their own energy meters that record:

&nbsp;

&#49;. Total kwh

&#50;. Total kvarh

&#51;. Max kW

&#52;. Max kVA

&#53;. Hours in operation

&#54;. $ (Price signal \* energy generated)

&nbsp;

Generator meters reset with the circuit energy meters and take a sample with the circuit energy meters as well. The Energy meters also used trapezoidal integration so that they are compatible with Load-Duration simulations.

&nbsp;

Generator power models for power flow simulations are:

&nbsp;

&#49;. Constant P, Q (\* dispatch curve, if appropriate).\
&#50;. Constant Z (For simple, approximate solution)

&#51;. Constant P, \|V\| somewhat like a standard power flow with voltage magnitudes and angles as the variables instead of P and Q.

&#52;. Constant P, fixed Q. P follows dispatch; Q is always the same.

&#53;. Constant P, fixed reactance. P follows dispatch, Q is computed as if it were a fixed reactance.

&#54;. User-written model

&#55;. Current-limited constant P, Q model (like some inverters).

&nbsp;

Most of the time you will use #1 for planning studies, assuming you want to specify a specific power. All load models can follow Loadshapes. Some follow only the P component while the Type 1 can follow both a P and Q characteristic.

&nbsp;

The default is for the generator to be a current injection source (Norton equivalent). Thus, its primitive Y matrix is similar to a Load object with a nominal equivalent admittance at rated voltage included in the primitive Y matrix and the injection current representing the amount required to compensate the Norton equivalent to achieve the desired terminal current. However, if the generator model is switched to Admittance from PowerFlow (see Set Mode command), the generator terminal current is computed simply from equivalent admittance that is included in the system Y matrix.

&nbsp;

Generator powers are assumed balanced over the number of phases specified. If you would like unbalanced generators, enter separate single-phase generators.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Free HTML Help documentation generator](<https://www.helpndoc.com>)_
