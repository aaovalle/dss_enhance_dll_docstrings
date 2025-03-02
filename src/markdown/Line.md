# Line

&nbsp;

\
\
The Line element is used to model most multi-phase, two-port lines or cables. It is a “Pi” model with shunt capacitance. This is a Power Delivery element described by its impedance. Impedances may be specified by symmetrical component values or by matrix values. Alternatively, you may simply refer to an existing LineCode object from which the impedance values will be copied. Or you may specify an existing Geometry object and the line impedances will be computed.

&nbsp;

You can define the line impedance at a base frequency directly in a Line object definition or you can import the impedance definition from a LineCode object. Both of these definitions of impedance are quite similar except that the LineCode object can perform Kron reduction. (See LineCode Object).

&nbsp;

If the Geometry property is specified, all previous definitions are ignored. The DSS will compute the impedance matrices from the specified geometry each time the frequency changes.

&nbsp;

Whichever definition is the most recent applies, as with nearly all DSS functions.\
\
Note the units property; you can declare any length measurement in whatever units you please. Internally, everything is converted to meters. Just be sure to declare the units. Otherwise, they are assumed to be compatible with other data or irrelevant.

&nbsp;

The default Line object is a 1000-ft overhead line with 336 MCM ACSR conductor on a 8-ft crossarm. It is defined by symmetrical component values:

&nbsp;

R1 = 0.0580 ohms per 1000 ft

X1 = 0.1206 ohms per 1000 ft

R0 = 0.1784 ohms per 1000 ft

X0 = 0.4047 ohms per 1000 ft

C1 = 3.4e-9 nF per 1000ft

C0 = 1.6e-9 nF per 1000ft

&nbsp;

The corresponding values of Rg and Xg for Rho=100 and 60 Hz are:

&nbsp;

Rg = 0.01805 ohms per 1000 ft

Xg = 0.155081 ohms per 1000 ft

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
