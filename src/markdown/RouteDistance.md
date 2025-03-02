# RouteDistance

&nbsp;

Returns the total distance in meters of the last route calculated between 2 buses. For example, consider the route presented above, this route has 6 segments from the orgin to the destination completing 2.841 km:

&nbsp;

set GISCoords=\[35.92209179726962, -84.14211464700368, 35.90779395922772, -84.14752180168537\]

GIS FindRoute

GIS RouteDistance

&nbsp;

With this command OpenDSS-GIS will return the total distances of the route calculated:

&nbsp;

\[2841.40,\]

&nbsp;

The following conditions need to be fulfilled:

&nbsp;

&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

&#51;. GISFindRoute has been executed at some point before this command (at least once)

&#52;. The model needs to have the correct GISCoords file

***
_Created with the Standard Edition of HelpNDoc: [Full-featured Documentation generator](<https://www.helpndoc.com>)_
