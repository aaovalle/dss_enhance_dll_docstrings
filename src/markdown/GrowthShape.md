# GrowthShape

&nbsp;

A GrowthShape object is like a Loadshape object. However, it is intended to represent the growth in load year-by-year and the way the curve is specified is entirely different. You must enter the growth for the first year. Thereafter, only the years where there is a change must be entered. Otherwise it is assumed the growth stays the same.

&nbsp;

Growth rate is specified by specifying the multiplier for the previous year's load. Thus, if the load grows 2.5% in 1999, the multiplier for that year will be specified as 1.025.

&nbsp;

(If no growth shape is specified, the load growth defaults to the circuit's default growth rate -- see Set %Growth command).

&nbsp;

The parameters are:

&nbsp;

Npts= Number of points to expect when defining the curve.

&nbsp;

Year= Array of year values corresponding to the multiplier values. Enter only those years in which the multiplier changes. Year data may be any integer sequence -- just so it's consistent for all growth curves. Setting the global solution variable Year=0 causes the growth factor to default to 1.0, effectively neglecting growth. This is what you would do for all base year analyses.

&nbsp;

You may also use the syntax: year=(file=filename.ext) in which the array values are entered one per line in the text file referenced.

&nbsp;

Mult= Array of Multiplier values corresponding to the year values. Enter multiplier by which the load will grow in this year.

&nbsp;

Example:&nbsp;

&nbsp;

New growthshape.name npts=3 year="1999 2003 2007" mult="1.10 1.05 1.025"

&nbsp;

This defines a growthshape the a 10% growth rate for 1999-2002. Beginning in 2003, the growth tapers off to 5% and then to 2.5% for 2007 and beyond.

&nbsp;

Normally, only a few points need be entered and the above parameters will be quite sufficient. However, provision has been made to enter the (year, multiplier) points from files just like the LoadShape objects. You may also use the syntax: mult=(file=filename.ext) in which the array values are entered one per line in the text file referenced.

&nbsp;

Csvfile= Name of a csv file containing one (year, mult) point per line. Separate the year from the multiplier by a comma.

&nbsp;

Sngfile= Name of a file of single-precision numbers containing (year, mult) points packed.

&nbsp;

Dblfile= Name of a file of single-precision numbers containing (year, mult) points packed.

&nbsp;

Like= Name of an existing GrowthShape object to base this one on.


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation with HelpNDoc's Project Analyzer Features](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
