# ShowRoute

&nbsp;

Shows the last route calculated between 2 buses in the OpenDSS-GIS map. For example, consider the route calculated in previous examples, for visualizing the route in OpenDSS-GIS use the following commands:

&nbsp;

set GISCoords=\[35.92209179726962, -84.14211464700368, 35.90779395922772, -84.14752180168537\]

GIS FindRoute

set GISColor = 0000FF \! the color for the route (blue)

set GISThickness=4 \! the thickness for the line (4 pix)

GIS ShowRoute

&nbsp;

The result in OpenDSS-GIS will look as shown in Figure 22.

&nbsp;

![Image](<lib/NewItem140.png>)

Figure 22. Showing route in OpenDSS-GIS

&nbsp;

The following conditions need to be fulfilled:

\
&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

&#51;. GISFindRoute has been executed at some point before this command (at least once)

&#52;. The model needs to have the correct GISCoords file

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Support Your Windows Applications with HelpNDoc's CHM Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
