# Seasonal rating simulation in OpenDSS

&nbsp;

&nbsp;

&nbsp;

Quasi-Static-Time-Series (QSTS) simulations are increasingly being applied to simulate system performance with time dependent distributed energy resources and system controls. Often, QSTS simulations span multiple periods where different thermal ratings may be defined. Most often, asset ratings are adjusted to reflect changes in ambient conditions that in part define the level to which assets to be loaded before experiencing thermal impacts.

&nbsp;

Capturing this practice within the QSTS simulation requires a dynamic approach for evaluating the overload level across the distribution system. As such, a couple of new properties have been added to Power Delivery Elements (PDElements) that allow ratings across the circuit to be set dynamically. This is recognized by the different QSTS based analysis modes included in OpenDSS.

&nbsp;

**Setting up the ratings**

&nbsp;

The new properties added to PDElements are Seasons and Ratings. Seasons refers to the number of ratings that the PDElement will have and Ratings refers to a numerical array for the rating values for the different Seasons. Both values (Seasons and Ratings) need to agree, otherwise the simulation will just take the default value for the rating when needed (the same as NormAmps). The new properties added apply for the following OpenDSS objects:

&nbsp;

&#49;. Line

&#50;. LineCode

&#51;. WireData

&#52;. LineGeometry

&#53;. CNData

&#54;. TSData

&nbsp;

If not defined, Seasons will be set to one and Ratings will be set to a numerical array of one element containing the NormAmps value. For example, consider a case where there are two seasons (seasons zero and one), the two seasons will be introduced into a LineGeometry as follows:

&nbsp;

New "LineGeometry.556-4/0n" nphases=3 nconds=4 Cond=1 wire=ACSR556 X=-1.243584 h=10.3632 units=m Cond=2 wire=ACSR556 X=0 h=10.52194 units=m Cond=3 wire=ACSR556 X=1.014984 h=10.3632 units=m Cond=4 wire=ACSR4 X=0 h=9.09319 units=m Reduce=Yes Seasons=2 Ratings=\[658 924\]

&nbsp;

In the previous example the LineGeometry has two different ratings for two different seasons, 658 is the rating for season zero and 924 is the rating for season one. The index number of the rating within the Ratings array defines the season.

&nbsp;

**The season signal**

&nbsp;

As mentioned before in the Ratings array of a PDElement the index value of the rating defines the season. The season number across the simulation is defined using an XYCurve object. The XYCurve is expected to describe the edges of a curve that changes its value in time. The X axis represents time and the Y axis represents the season. Consider the previous example, in this case both seasons are summer and winter. The winter season goes from November to April, the other months are considered as summer. The XYCurve for describing these seasons on a simulation will be as follows:

&nbsp;

New XYCurve.seasonsrat npts=6 xarray=\[0,2880,2881,7296,7297,8760\] yarray=\[1,1,0,0,1,1\]

&nbsp;

The definition presented above is for one year with one-hour time intervals. As can be seen in the XYCurve definition, only the seasonal changes need to be signaled in the season signal, in this case, winter is number one (1) and summer is number zero (0). As shown in Figure 1.

&nbsp;

![Image](<lib/NewItem225.png>)

Figure 1. XYCurve definition for season signaling

&nbsp;

The XYCurve will be extrapolated using the last pair (X, Y) defined for the curve if the time exceeds the time defined for the Curve. This means that if your simulation takes more than 1 year and your season signal curve considers only 1 year, the user will have to redefine the season signal curve to cover all the years as shown in Figure 2.

&nbsp;

![Image](<lib/NewItem226.png>)

Figure 2. Season signal for 2-year simulation

&nbsp;

**Applying the seasonal ratings into the active circuit**

&nbsp;

It is necessary to activate the season settings previously described to take effect on the current circuit. To activate it, the user needs to define what is the season signal name and activate seasonal ratings. The activation can be done using the following OpenDSS commands:

&nbsp;

set SeasonSignal=seasonsrat

set SeasonRating=true

&nbsp;

String ‘seasonsrat’ is the name of the XYCurve previously defined. By setting “SeasonRating=true” the seasonal ratings will be used when generating the overloads report in OpenDSS.

&nbsp;

**References**

&nbsp;

[https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Doc/OpenDSS%20XYCurve%20Object.pdf](<https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Doc/OpenDSS%20XYCurve%20Object.pdf>)

&nbsp;

[https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Doc/PCElementEssentials.pdf](<https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Doc/PCElementEssentials.pdf>)

&nbsp;

[https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Doc/TechNotes/EnergyMeter%20EEN%20and%20UE%20-%20OpenDSSWiki.pdf](<https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Doc/TechNotes/EnergyMeter%20EEN%20and%20UE%20-%20OpenDSSWiki.pdf>)

&nbsp;

[https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Doc/TechNotes/TechNote%20EnergyMeter%20-%20OpenDSSWiki.pdf](<https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Doc/TechNotes/TechNote%20EnergyMeter%20-%20OpenDSSWiki.pdf>)

***
_Created with the Standard Edition of HelpNDoc: [Create cross-platform Qt Help files](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
