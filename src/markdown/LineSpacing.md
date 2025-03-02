# LineSpacing

&nbsp;

&nbsp;

A LineSpacing object defined the spacing of a group of conductors in a relative coordinate system. These are usually the main phase conductors, but could be any group of conductors such as conductors in a bundle. Simply define the position of each conductor. The LineSpacing object expands the options for defining a library of overhead line data. This object comprises two arrays for X and H (or Y) coordinates, along with a unit specification. This is a subset of the exiting LineGeometry property set. In addition, a string array of wires has been added to the property set for both LineGeometry and Line itself.

&nbsp;

LineSpacing Properties (in addition to like):

&nbsp;

| **Property** | **Description** |
| --- | --- |
| Nconds | Number of wires in this geometry. Default is 3. Triggers memory allocations. Define first\! |
| Nphases | Number of retained phase conductors. If less than the number of wires, list the retained phase coordinates first. |
| Units | Units for x and h: {mi\|kft\|km\|m\|Ft\|in\|cm } Initial default is "ft", but defaults to last unit defined |
| X | Array of wire X coordinates. |
| H | Array of wire Heights. |
| detailed | {Yes/True \| No/False} Default = Yes. Determines whether the spacing uses a detailed cross-section coordinates with x and h arrays (Yes/True), or uses equivalent spacing fields (No/False). The equivalent spacing fields are EqDistPhPh, EqDistPhN, AvgPhaseHeight and AvgNeutralHeight. |
| EqDistPhPh | Equivalent distance between phase conductors. Used for equivalent distance modeling (detailed=yes) as opposed to detailed cross-section coordinates.&nbsp; |
| EqDistPhN | Equivalent distance between phase and neutral conductors. Used for equivalent distance modeling (detailed=yes) as opposed to detailed cross-section coordinates. |
| AvPhaseHeight | Average height of phase conductors. Used for equivalent distance modeling (detailed=yes) as opposed to detailed cross-section coordinates. |
| AvNeutralHeight | Average height of neutral conductors. Used for equivalent distance modeling (detailed=yes) as opposed to detailed cross-section coordinates. |


&nbsp;

Any time a LineSpacing is employed, the program constructs a temporary LineGeometry object to calculate the line parameters. The results would be equivalent; the only difference is in how the inputs are specified.

&nbsp;

The current options for line parameters are:

&nbsp;

&#49;. Define impedances directly on the Line object (no changes).

&nbsp;

&#50;. Use the linecode and length properties on the Line object (no changes).

&nbsp;

&#51;. Use the geometry and length properties on the Line object.

&nbsp;

a. Previously define a LineGeometry, with wire, x, and y specification by conductor number. All WireData objects must be previously defined (no changes).

&nbsp;

b. NEW – Previously define a LineGeometry, with spacing and wires properties. You still specify nconds first, and may also specify nphases and reduce independently. This closely matches the IEEE test feeder definitions, and the data structures of FeederAll, CIMDIST, and some other programs.

&nbsp;

&#52;. NEW – use the spacing, wires, and length properties on the Line object. This closely matches the “by‐phase” wire modeling in CIMDIST and some other programs. The LineSpacing object must be previously defined, and it determines the number of phases, and whether or not neutral

reduction will be used. The number of wire names should match the LineSpacing’s number of conductors (i.e., include the neutral), and the matching WireData objects must have been previously defined.

&nbsp;

Here is an example, from the IEEE 13‐Bus test case, using spacing on the Line object. Note that on the two‐phase line from bus 632 to bus 645, phase C is in the left‐most position (x=‐4), while phase B is in the right‐most position (x=3).

&nbsp;

new WireData.ACSR\_556\_5 DIAM=0.927 GMRac=0.37320 Rdc=0.035227273

\~ Runits=kft Radunits=in gmrunits=in

new WireData.ACSR\_4/0 DIAM=0.563 GMRac=0.09768 Rdc=0.112121212

\~ Runits=kft Radunits=in gmrunits=in

&nbsp;

new WireData.ACSR\_1/0 DIAM=0.398 GMRac=0.05352 Rdc=0.212121212

\~ Runits=kft Radunits=in gmrunits=in

new LineSpacing.500 nconds=4 nphases=3 units=ft x=\[-4 -1 3 0\] h=\[28 28 28 24\]

new LineSpacing.505 nconds=3 nphases=2 units=ft x=\[-4 3 0\] h=\[28 28 24\]

new LineSpacing.510 nconds=2 nphases=1 units=ft x=\[0.5 0\] h=\[29 24\]

&nbsp;

New Line.671680 Bus1=671.1.2.3 Bus2=680.1.2.3

\~ Spacing=500 Wires=\[ACSR\_556\_5 ACSR\_556\_5 ACSR\_556\_5 ACSR\_4/0\] Length=1000 units=ft

New Line.632633 Bus1=632.1.2.3 Bus2=633.1.2.3

\~ Spacing=500 Wires=\[ACSR\_4/0 ACSR\_4/0 ACSR\_4/0 ACSR\_4/0\] Length=500 units=ft

New Line.632645 Bus1=632.3.2 Bus2=645.3.2

\~ Spacing=505 Wires=\[ACSR\_1/0 ACSR\_1/0 ACSR\_1/0\] Length=500 units=ft

&nbsp;

// include the same WireData and LineSpacing definitions from above

new WireData.ACSR\_556\_5 DIAM=0.927 GMRac=0.37320 Rdc=0.035227273

\~ Runits=kft Radunits=in gmrunits=in

new WireData.ACSR\_4/0 DIAM=0.563 GMRac=0.09768 Rdc=0.112121212

\~ Runits=kft Radunits=in gmrunits=in

new WireData.ACSR\_1/0 DIAM=0.398 GMRac=0.05352 Rdc=0.212121212

\~ Runits=kft Radunits=in gmrunits=in

&nbsp;

new LineSpacing.500 nconds=4 nphases=3 units=ft x=\[-4 -1 3 0\] h=\[28 28 28 24\]

new LineSpacing.505 nconds=3 nphases=2 units=ft x=\[-4 3 0\] h=\[28 28 24\]

new LineSpacing.510 nconds=2 nphases=1 units=ft x=\[0.5 0\] h=\[29 24\]

&nbsp;

new LineGeometry.601 nconds=4 nphases=3 reduce=y spacing=500

\~ wires=\[ACSR\_556\_5 ACSR\_556\_5 ACSR\_556\_5 ACSR\_4/0\]

new LineGeometry.602 nconds=4 nphases=3 reduce=y spacing=500

\~ wires=\[ACSR\_4/0 ACSR\_4/0 ACSR\_4/0 ACSR\_4/0\]

new LineGeometry.603 nconds=3 nphases=2 reduce=y spacing=505

\~ wires=\[ACSR\_1/0 ACSR\_1/0 ACSR\_1/0\]

&nbsp;

New Line.671680 Bus1=671.1.2.3 Bus2=680.1.2.3 Geometry=601 Length=1000 units=ft

New Line.632633 Bus1=632.1.2.3 Bus2=633.1.2.3 Geometry=602 Length=500 units=ft

New Line.632645 Bus1=632.3.2 Bus2=645.3.2 Geometry=603 Length=500 units=ft &nbsp; 
***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
