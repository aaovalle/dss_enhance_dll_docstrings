# LoadBus

&nbsp;

Uploads the coordinates of the bus specified in the argument to the coordinates buffer (GISCoords) by pushing the previous down. The coordinates buffer has 4 positions, the coordinates of the bus specified will be at the first 2 positions. This functionality can be useful for bringing back GIS coordinates of a bus or a pair of buses, and in combination with other commands, can facilitate the command execution.

&nbsp;

For example, consider the example given at DrawLine, in this example for drawing a line on the map it is necessary to specify the coordinates of both ends of the line. Assum that the first pair of coordinates correspond to bus myBus1 and the second pair to bu myBus2. Then, drawing the line using GISLoadBus will be as follows:

&nbsp;

GIS LoadBus myBus1 \!uploads bus1 coords into the buffer

GIS LoadBus myBus2 \!uploads bus2 coords into the buffer

GIS DrawLine \!draws the line

&nbsp;

In combination with GoTo, GISLoadBus has the same effect. Consider the example given at GoTo, assume that the coordinates given correspond to bus myBus, then, using GISLoadBus the example will be as follows:

&nbsp;

GIS LoadBus myBus

GIS GoTo

&nbsp;

Finally, suppose the user wants to draw a blue X at the bus location, the list of commands including PlotPoint will be as follows:

&nbsp;

GIS LoadBus myBus

set GISThickness = 15 GISColor=0000FF

GIS PlotPoint x

&nbsp;

The following conditions need to be fulfilled:

&nbsp;

&#49;. OpenDSS-GIS must be installed

&nbsp;

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

***
_Created with the Standard Edition of HelpNDoc: [Easy to use tool to create HTML Help files and Help web sites](<https://www.helpndoc.com/help-authoring-tool>)_
