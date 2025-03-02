# Line Model Revision

&nbsp;

&nbsp;

***Revision Sept 2006***

In this document, recent (2006) additions to the Line object model and supporting object types, Linecode, LineGeometry, and Wiredata are described.

&nbsp;

***Update: 2010***

There have been several modifications since the original 2006 modifications, but this Tech Note has the basic information.

&nbsp;

**LINE Object**

&nbsp;

This model was modified from the standard model in 2005 to better represent the variation in earth impedance with frequency. The added properties are shown below in bold black. With the latest revision the geometry property was added so that the line impedance could be computed on the fly at the present solution frequency. The geometry property requires a linegeometry object to be defined, which in turn requires one or more wiredata objects to be defined.

&nbsp;

You can define the line impedance at a base frequency directly in a Line object definition or you can import the impedance definition from a LineCode object. Both of these definitions of impedance are quite similar except that the LineCode object can perform Kron reduction. (See LineCode Object below).

&nbsp;

If the geometry property is specified all previous definitions are ignored. The DSS will compute the impedance matrices from the specified geometry each time the frequency changes. Whichever definition is the most recent applies, as with nearly all DSS functions. Note the addition of the units property. You can declare any length measurement in whatever units you please. Internally, everything is converted to meters. Just be sure to declare the units. Otherwise, they are assumed to be compatible with other data or irrelevant.

&nbsp;

***Line Object Property Descriptions***

&nbsp;

• bus1 Name of bus to which first terminal is connected. Example: bus1=busname (assumes all terminals connected in normal phase order) bus1=busname.3.1.2.0 (specify terminal to node connections explicitly)

•&nbsp; bus2 Name of bus to which 2nd terminal is connected.

• linecode Name of linecode object describing line impedances that are supplied to OpenDSS. If you use a line code, you do not need to specify the impedances in the Line object definition. The line code must have been PREVIOUSLY defined. The values specified last will prevail over those specified earlier (lefttoright sequence of properties). If no line code or impedance data are specified, line object defaults to 336 MCM ACSR on 4 ft spacing.

• length Length of line. Default is 1.0. If units do not match the impedance data, specify "units" property.

• phases Number of phases, this line.

• r1 Positive-sequence Resistance, ohms per unit length. See also Rmatrix.

• x1 Positive-sequence Reactance, ohms per unit length. See also Xmatrix

• r0 Zero-sequence Resistance, ohms per unit length.

• x0 Zero-sequence Reactance, ohms per unit length.

• c1 Positive-sequence capacitance, nf per unit length. See also Cmatrix.

• c0 Zero-sequence capacitance, nf per unit length.

• rmatrix Resistance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. For balanced line models, you may use the standard symmetrical component data definition instead.

• xmatrix Reactance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. For balanced line models, you may use the standard symmetrical component data definition instead.

• cmatrix Nodal Capacitance matrix, lower triangle, nf per unit length.Order of the matrix is the number of phases. May be used to specify the shunt capacitance of any line configuration. For balanced line models, you may use the standard symmetrical component data definition instead.

• Switch {y/n \| T/F} Default= no/false. Designates this line as a switch for graphics and algorithmic

purposes. SIDE EFFECT: Sets R1=0.001 X1=0.0. You must reset if you want something different.

• Rg Carson earth return resistance per unit length used to compute impedance values at base frequency. For making better frequency adjustments. Default=0

• Xg Carson earth return reactance per unit length used to compute impedance values at base frequency. For making better frequency adjustments. Default=0

• rho Default=100 meter ohms. Earth resitivity used to compute earth correction factor. Overrides Line geometry definition if specified.

• geometry Geometry code for LineGeometry Object. Supercedes any previous definition of line impedance. Line constants are computed for each frequency change or rho change. CAUTION: may alter number of phases.

• units Length Units = {none \| mi\|kft\|km\|m\|Ft\|in\|cm } Default is None assumes length units match impedance units.

• normamps Normal rated current.

• emergamps Maximum current.

• faultrate No. of failures per year.

• pctperm Percent of failures that become permanent.

• repair Hours to repair.

• basefreq Base Frequency for ratings.

• enabled {Yes\|No or True\|False} Indicates whether this element is enabled.

• like Make like another object, e.g.: New Capacitor.C2 like=c1 ...

&nbsp;

&nbsp;

***Line Code***

&nbsp;

The revised LineCode object is similar to the original LineCode Object with a few things added. It will now perform a Kron reduction, reducing out the specified neutral conductor in the impedance matrices (See Help on LineCode if using a recent version of OpenDSS). This applies only if the impedance is specified as a matrix. If the impedance is defined as symmetrical components, this function does not apply because symmetrical component values already assume the reduction.

&nbsp;

By specifying the values of Rg, Xg, and rho, the DSS will take the base frequency impedance matrix values and adjust the earth return component for frequency. Skin effect in the conductors is not modified. To represent skin effect, you have to define the geometry property of the Line object.

&nbsp;

***Property Descriptions***

&nbsp;

• nphases Number of phases in the line this line code data represents. Setting this property reinitializes the line code. Impedance matrix is reset for default symmetrical component.

• r1 Positive-sequence Resistance, ohms per unit length. See also Rmatrix.

• x1 Positive-sequence Reactance, ohms per unit length. See also Xmatrix

• r0 Zero-sequence Resistance, ohms per unit length.

• x0 Zero-sequence Reactance, ohms per unit length.

• c1 Positive-sequence capacitance, nf per unit length. See also Cmatrix.

• c0 Zero-sequence capacitance, nf per unit length.

• units Length Units = {none \| mi\|kft\|km\|m\|Ft\|in\|cm } Default is None assumes length units match impedance units.

• rmatrix Resistance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. For balanced line models, you may use the standard symmetrical component data definition instead.

• xmatrix Reactance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. For balanced line models, you may use the standard symmetrical component data definition instead.

• cmatrix Nodal Capacitance matrix, lower triangle, nf per unit length.Order of the matrix is the number of phases. May be used to specify the shunt capacitance of any line configuration. For balanced line models, you may use the standard symmetrical component data definition instead.

• basefreq Base Frequency for ratings.

• normamps Normal ampere limit on line. This is the so-called Planning Limit. It may also be the value above which load will have to be dropped in a contingency. Usually about 75% 80% of the emergency (onehour) rating.

• emergamps Emergency ampere limit on line (usually onehour rating). (15) faultrate Number of faults per unit length per year.

•&nbsp; pctperm Percentage of the faults that become permanent.

•&nbsp; repair Hours to repair.

•&nbsp; Kron Kron=Y/N. Default=N. Perform Kron reduction on the impedance matrix after it is formed, reducing order by 1. Do this only on initial definition after matrices are defined. Ignored for symmetrical components.

• Rg Carson earth return resistance per unit length used to compute impedance values at base frequency. For making better frequency adjustments. Default=0

• Xg Carson earth return reactance per unit length used to compute impedance values at base frequency. For making better frequency adjustments. Default=0

• rho Default=100 meter ohms. Earth resitivity used to compute earth correction factor. Overrides Line geometry definition if specified.

• like Make like another object, e.g.: New Capacitor.C2 like=c1 ...

&nbsp;

***WIREDATA***

&nbsp;

This class of data defines the raw conductor data that is used to compute the impedance for a line geometry. Note that you can use whatever units you want for any of the dimensional data – be sure to declare the units. Otherwise, the units are all assumed to match, which would be very rare for conductor data. Conductor data is usually supplied in a hodgepodge of units. Everything is converted to meters internally to the DSS

&nbsp;

Property Descriptions

&nbsp;

• Rdc dc Resistance, ohms per unit length (see Runits). Defaults to Rac if not specified.

• Rac Resistance at 60 Hz per unit length. Defaults to Rdc if not specified.

• Runits Length units for resistance: ohms per {mi\|kft\|km\|m\|Ft\|in\|cm } Default=none.

• GMRac GMR at 60 Hz. Defaults to .7788\*radius if not specified.

• GMRunits Units for GMR: {mi\|kft\|km\|m\|Ft\|in\|cm } Default=none.

• radius Outside radius of conductor. Defaults to GMR/0.7788 if not specified.

• radunits Units for outside radius: {mi\|kft\|km\|m\|Ft\|in\|cm } Default=none.

• normamps Normal ampacity, amperes. Defaults to Emergency amps/1.5 if not specified.

• emergamps Emergency ampacity, amperes. Defaults to 1.5 \* Normal Amps if not specified.

• diam Diameter; Alternative method for entering radius.

• like Make like another object, e.g.: New Capacitor.C2 like=c1 ...

&nbsp;

***LINEGEOMETRY Class***

&nbsp;

This class of data is used to define the positions of the conductors. Note the Reduce option. This allows you to use the linegeometry class to automatically reduce out any neutral conductors down to the number of phases.

&nbsp;

Property Description

• nconds Number of conductors in this geometry. Default is 3. Triggers memory allocations. Define first\!

• nphases Number of phases. Default =3; All other conductors are considered neutrals and might be reduced out when Reduce is set to Yes.

• cond Set this = number of the conductor you wish to define. Default is 1.

• wire Code from WireData. MUST BE PREVIOUSLY DEFINED. no default.

• x x coordinate.

• h Height of conductor.

• units Units for x and h: {mi\|kft\|km\|m\|Ft\|in\|cm } Initial default is "ft", but defaults to last unit defined

• normamps Normal ampacity, amperes for the line. Defaults to first conductor if not specified.

• emergamps Emergency ampacity, amperes. Defaults to first conductor if not specified.

• reduce {Yes \| No} Default = no. Reduce to Nphases (Kron Reduction). Reduce out neutrals.

• like Make like another object, e.g.: New Capacitor.C2 like=c1 ...

&nbsp;

***Examples***

&nbsp;

**Define the wire data:**

&nbsp;

New Wiredata.ACSR336 GMR=0.0255000 DIAM=0.7410000 RAC=0.3060000

\~ NormAmps=530.0000

\~ Runits=mi radunits=in gmrunits=ft

New Wiredata.ACSR1/0 GMR=0.0044600 DIAM=0.3980000 RAC=1.120000

\~ NormAmps=230.0000

\~ Runits=mi radunits=in gmrunits=ft

&nbsp;

**Define the Geometry data:**

&nbsp;

New Linegeometry.HC2\_336\_1neut\_0Mess nconds=4 nphases=3

\~ cond=1 Wire=acsr336 x=1.2909

h=13.716 units=m

\~ cond=2 Wire=acsr336 x=0.502

h=13.716 \!units=m

\~ cond=3 Wire=acsr336 x=0.5737 h=13.716 \!units=m

\~ cond=4 Wire= ACSR1/0 x=0 h=14.648 \! units=m \! neutral

New Line.Line1 Bus1=xxx Bus2=yyy

\~ Geometry= HC2\_336\_1neut\_0Mess

\~ Length=300 units=ft

&nbsp;

Check out the line constants at 60 and 600 Hz in per km values: (This command shows line constants for all defined geometries)

&nbsp;

Show lineconstants freq=60 units=km

Show lineconstants freq=600 units=km

&nbsp;

*(If the number of conductors=3, this Show command will also give you the sequence impedances. If your geometry has more than 3 conductors and you want to see the sequence impedance, define*

&nbsp;

...nconds=whatever nphases=3 Reduce=Yes

&nbsp;

*This will force the impedance matrices to be reduced to a 3x3 and the Show LineConstants command will automatically give the sequence impedances.*

*Note: make sure the phase conductors are defined first in the geometry definition. Sorry, no automatic assembly of bundled conductors is available yet. However, you can specifically define the position of each conductor in the geometry definition and connect them up explicitly in the DSS, for example, for a two conductor bundle:*

&nbsp;

New Line.2Bundled bus1=FromBus.1.1.2.2.3.3 ToBus.1.1.2.2.3.3 ~ Geometry=2BundleGeometry Length= etc. etc.

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Free help authoring tool](<https://www.helpndoc.com/help-authoring-tool>)_
