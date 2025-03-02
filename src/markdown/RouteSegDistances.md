# RouteSegDistances

&nbsp;

Returns the distances in meters for each segment within the route previously estimated. For example, consider the route presented above, this route has 6 segments from the orgin to the destination completing 2.841 km:

&nbsp;

set GISCoords=\[35.92209179726962, -84.14211464700368, 35.90779395922772, -84.14752180168537\]

GIS FindRoute

GIS RouteSegDistances

&nbsp;

With this command OpenDSS-GIS will return the distances of each segment included in this route as follows:

&nbsp;

\[160.90,166.30,408.20,141.60,1504.10,460.20,0.00,\]

&nbsp;

The following conditions need to be fulfilled:

&nbsp;

&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

&#51;. The model needs to have the correct GISCoords file

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
