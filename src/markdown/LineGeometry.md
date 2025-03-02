# LineGeometry

&nbsp;

This class of data is used to define the conductors and positions of the conductors in a type of line construction.

&nbsp;

Nconds= Number of conductors in this geometry. Default is 3. Triggers memory allocations. So, define this first\!

&nbsp;

Nphases= Number of phases. Default =3; All other conductors are considered neutrals and might be reduced out by Kron reduction.

&nbsp;

Cond= Set this to number of the conductor you wish to define. Default is 1.

&nbsp;

Wire= Code for a WireData-class object. MUST BE PREVIOUSLY DEFINED. no default.

&nbsp;

X= x coordinate. This is a relative coordinate value and can have an arbitrary reference point. For convenience, one of the conductors is uaually assigned the X=0 position.

&nbsp;

H= Height of conductor above earth.

&nbsp;

Units= Units for x and h: {mi\|kft\|km\|m\|Ft\|in\|cm } Initial default is "ft", but defaults to last unit defined.

&nbsp;

Normamps= Normal ampacity, amperes for the line. Defaults to first conductor if not specified.

&nbsp;

Emergamps= Emergency ampacity, amperes. Defaults to first conductor if not specified.

&nbsp;

Reduce= {Yes \| No} Default = no. Reduce from Nconds to Nphases by Kron Reduction. Reduce out neutral conductors assumed to be grounded.

&nbsp;

Spacing= Reference to a LineSpacing object for use in a line constants calculation. Alternative to x, h, and units. MUST BE PREVIOUSLY DEFINED. Must match "nconds" as previously defined for this geometry. Must be used in conjunction with the Wires property.

&nbsp;

Wires= Array of WireData names for use in a line constants calculation. Alternative to individual wire inputs. ALL MUST BE PREVIOUSLY DEFINED. Must match "nconds" as previously defined for this geometry, unless TSData or CNData were previously assigned to phases, and these wires are neutrals. Must be used in conjunction with the Spacing property.

&nbsp;

CNcable= Code from CNData. MUST BE PREVIOUSLY DEFINED. no default. Specifies use of Concentric Neutral cable parameter calculation.

&nbsp;

TSCable= Code from TSData. MUST BE PREVIOUSLY DEFINED. no default. Specifies use of Tape Shield cable parameter calculation.

&nbsp;

CNCables= Array of CNData names for cable parameter calculation. All must be previously defined, and match "nphases" for this geometry. You can later define "nconds-nphases" wires for bare neutral conductors.

&nbsp;

TSCables= Array of TSData names for cable parameter calculation. All must be previously defined, and match "nphases" for this geometry. You can later define "nconds-nphases" wires for bare neutral conductors.

&nbsp;

Seasons= Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

&nbsp;

Ratings= An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

&nbsp;

LineType= Code designating the type of line. One of: OH, UG, UG\_TS, UG\_CN, SWT\_LDBRK, SWT\_FUSE, SWT\_SECT, SWT\_REC, SWT\_DISC, SWT\_BRK, SWT\_ELBOW, BUSBAR. OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

&nbsp;

conductors= Array of conductor names for use in line constants calculation. Must be used in conjunction with the Spacing property. Specify the Spacing first, and "ncond" wires. Specify the conductor type followed by the conductor name. e.g., "conductors=\[cndata.cncablename, tsdata.tscablename, wiredata.wirename\]". If a given position in the spacing is not to be used in the line, use "none" in the entry of the conductors array.

&nbsp;

Like= Make like another object, e.g.: New Capacitor.C2 like=c1 ...

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Convert Your Word Doc to an eBook: A Step-by-Step Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
