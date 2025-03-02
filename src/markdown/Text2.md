# Text

&nbsp;

Prints the text given at the argument at the coordinates specified in GISCoords. The coordinates must be defined using GISCoords, LoadBus can also be used with this command. The text color will match the color defined at GISColor, and the font size must be specified at GISThickness. This command requires the user to previously define the coordinates for the point of interest, the text color and size (if desired) as follows:

&nbsp;

set GISCoords = \[35.92209179726962,-84.14211464700368\]

set GISColor = FF0000

set GISThickness=20

GIS Text "Electric Power Research Institute (EPRI)"

GIS GoTo

&nbsp;

The previous example will show the location displayed at Figure 37, the text will be overimposed at the location.\
&nbsp;

![Image](<lib/NewItem155.png>)\
Figure 37. Writing text on the map

***
_Created with the Standard Edition of HelpNDoc: [Make Documentation Review a Breeze with HelpNDoc's Advanced Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
