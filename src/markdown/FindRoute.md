# FindRoute

&nbsp;

Finds a route between the given buses using roads and geographical information. The buses are defined using the GISCoords buffer. This command is also compatible with LoadBus. In the following example, the route between two given coordinates will be calculated. The calculation takes place by following streets and intersections. The router used in OpenDSS-GIS is OSRM (http://project-osrm.org/).

&nbsp;

set GISCoords=\[35.92209179726962, -84.14211464700368, 35.90779395922772, -84.14752180168537\]

GIS FindRoute

&nbsp;

Using the LoadBus command, if Bus1 and Bus2 correspond to the coordinates presented above respectively:

&nbsp;

GIS LoadBus Bus1

GIS LoadBus Bus2

GIS FindRoute

&nbsp;

The following conditions need to be fulfilled:

&nbsp;

&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

&#51;. The model needs to have the correct GISCoords file

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Help Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com>)_
