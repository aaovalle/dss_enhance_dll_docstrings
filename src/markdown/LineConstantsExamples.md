# Line Constants Examples

&nbsp;

&nbsp;

This section contains different examples of the line Code and Geometry implementation&nbsp;

&nbsp;

Define the wire data:

&nbsp;

New Wiredata.ACSR336 GMR=0.0255000 DIAM=0.7410000 RAC=0.3060000

\~ NormAmps=530.0000

\~ Runits=mi radunits=in gmrunits=ft

New Wiredata.ACSR1/0 GMR=0.0044600 DIAM=0.3980000 RAC=1.120000

\~ NormAmps=230.0000

\~ Runits=mi radunits=in gmrunits=ft

&nbsp;

Define the Geometry data:

&nbsp;

New Linegeometry.HC2\_336\_1neut\_0Mess nconds=4 nphases=3

\~ cond=1 Wire=acsr336 x=-1.2909 h=13.716 units=m

\~ cond=2 Wire=acsr336 x=-0.502 h=13.716 \!units=m

\~ cond=3 Wire=acsr336 x=0.5737 h=13.716 \!units=m

\~ cond=4 Wire= ACSR1/0 x=0 h=14.648 \! units=m \! neutral

&nbsp;

Define a 300-ft line section:

&nbsp;

New Line.Line1 Bus1=xxx Bus2=yyy

\~ Geometry= HC2\_336\_1neut\_0Mess

\~ Length=300 units=ft

&nbsp;

Check out the line constants at 60 and 600 Hz in per km values. This command shows line constants for all defined geometries:

&nbsp;

Show lineconstants freq=60 units=km

Show lineconstants freq=600 units=km

&nbsp;

If the number of conductors = 3, this Show command will also give you the sequence impedances. If your geometry has more than 3 conductors and you want to see the sequence impedance, define

&nbsp;

nconds = (...whatever...)

nphases = 3

Reduce=Yes

&nbsp;

This will force the impedance matrices to be reduced to 3x3 and the Show LineConstants command will automatically give the sequence impedances. Note: make sure the phase conductors are defined first in the geometry definition.

&nbsp;

No automatic assembly of bundled conductors is available yet. However, you can specifically define the position of each conductor in the geometry definition and connect them up explicitly in the DSS, for example, for a two conductor bundle:

&nbsp;

New Line.2Bundled bus1=FromBus.1.1.2.2.3.3 ToBus.1.1.2.2.3.3

\~ Geometry=2BundleGeometry Length= etc.


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
