# GetRoute

&nbsp;

Returns the GIS coords of the route between 2 buses step by step in a 2-dimension array. For example, consider the route found above, the command GetRoute can be applied as follows:

&nbsp;

set GISCoords=\[35.92209179726962, -84.14211464700368, 35.90779395922772, -84.14752180168537\]

GIS FindRoute

GIS GetRoute

&nbsp;

OpenDSS-GIS will return the coordinates of each segment (2 coordinates per segment) included in this route as follows:

&nbsp;

\[-84.1423200000000000,35.9222830000000000,-84.1411360000000000,35.9219720000000000,-84.1398070000000000,35.9230060000000000,-84.1375080000000000,35.9214170000000000\|-84.1367180000000000,35.9205030000000000,-84.1378340000000000,35.9196210000000000,-84.1421150000000000,35.9173700000000000\|-84.1444060000000000,35.9160410000000000\|-84.1484180000000000,35.9127300000000000\|-84.1506070000000000,35.9110880000000000,-84.1490140000000000,35.9091680000000000\|-84.1480800000000000,35.9083550000000000\|-84.1474460000000000,35.9078590000000000,\]

&nbsp;

In the format shown above the character comma (,) is a vector separator between the same pair latitude-longitude, the character vertical bar (\|) is used as row separator.

&nbsp;

The following conditions need to be fulfilled:

&nbsp;

&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

&#51;. GISFindRoute has been executed at some point before this command (at least once)

&#52;. The model needs to have the correct GISCoords file

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Edit and Export Markdown Documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
