# Distance

&nbsp;

Returns the linear distance in meters between two coordinates. The coordinates must be defined using GISCoords. This command doesn’t have arguments, but it requires the user to previously define the coordinates for the area of interest as follows:

&nbsp;

set GISCoords = \[40.50007607834282197,-80.01294794446681635, 40.50019376002214955, -80.01323963543782725\]

GIS Distance

&nbsp;

When combined with the command LoadBus, if the first coordinates in the previous example correspond to myBus1 and the second pair to myBus2, GISDistance will look as follows:

&nbsp;

GIS LoadBus myBus1 \!uploads bus1 coords into the buffer

GIS LoadBus myBus2 \!uploads bus2 coords into the buffer

GIS Distance

&nbsp;

The following conditions need to be fulfilled:

&nbsp;

&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

***
_Created with the Standard Edition of HelpNDoc: [Elevate your documentation to new heights with HelpNDoc's built-in SEO](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
