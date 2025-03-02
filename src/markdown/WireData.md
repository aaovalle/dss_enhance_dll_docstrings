# WireData

&nbsp;

This class of data defines the raw conductor data that is used to compute the impedance for a line geometry.

&nbsp;

Note that you can use whatever units you want for any of the dimensional data – be sure to declare the units. Otherwise, the units are all assumed to match, which would be very rare for conductor data. Conductor data is usually supplied in a hodge-podge of units. Everything is converted to meters internally to the DSS

&nbsp;

Rdc= dc Resistance, ohms per unit length (see Runits). Defaults to Rac if not specified.

&nbsp;

Rac= Resistance at 60 Hz per unit length. Defaults to Rdc if not specified.

&nbsp;

Runits= Length units for resistance: ohms per {mi\|kft\|km\|m\|Ft\|in\|cm } Default=none.

&nbsp;

GMRac= GMR at 60 Hz. Defaults to .7788\*radius if not specified.

&nbsp;

GMRunits= Units for GMR: {mi\|kft\|km\|m\|Ft\|in\|cm } Default=none.

&nbsp;

Radius= Outside radius of conductor. Defaults to GMR/0.7788 if not specified.

&nbsp;

Capradius- Equivalent conductor radius for capacitor calcs. Specify this for bundled conductors. Defaults to same value as radius.

&nbsp;

Radunits= Units for outside radius: {mi\|kft\|km\|m\|Ft\|in\|cm } Default=none.

&nbsp;

Normamps= Normal ampacity, amperes. Defaults to Emergency amps/1.5 if not specified.

&nbsp;

Emergamps= Emergency ampacity, amperes. Defaults to 1.5 \* Normal Amps if not specified.

&nbsp;

Diam= Diameter; Alternative method for entering radius.

&nbsp;

Like= Make like another object of this class:

&nbsp;

For bundled conductors, you define an equivalent conductor with

&nbsp;

GMRB = \[N(GMRC)A(N-1)\]1/N

&nbsp;

Where

&nbsp;

N = number of conductors in the bundle

GMRC = GMR of each subconductor

A = bundle radius

&nbsp;

For capacitive reactance calculations, the effective radius (Capradius) of the bundle is

&nbsp;

rB = (NrAN-1)1/N

&nbsp;

Where

&nbsp;

N = number of conductors in the bundle

&nbsp;

r = radius of each conductor

&nbsp;

A = bundle radius

&nbsp;

When the bundle size is specified by the bundle spacing (distance between adjacent conductors in the bundle, S)

&nbsp;

A = S / \[2 sin(π/N)\] for N\>1

A = 0 for N=1 (recall that 00 = 1)

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
