# PlotFile

&nbsp;

With this command the user can plot a customized graph on top of the map. The path to the file containing the plot is the argument for this command. The file contains the coordinates, color and thickness for each line that composes the draw in a comma separated values file as follows:

&nbsp;

…

myLong11,myLat11,myLong12,myLat12,myColor1,myThickness1

myLong21,myLat21,myLong22,myLat22,myColor2,myThickness2

myLong31,myLat31,myLong32,myLat32,myColor3,myThickness3

…

&nbsp;

Where myLongXX and myLatXX are longitude and latitude for describing the beginning and end of the line, myColorX is the color of the line and myThicknessX is the thickness expressed in pixels. X refers to the index for differenciating data within the given example.

&nbsp;

At Figure 27, there is an example for plotting the power flow across the feeder using red as the for the lines with maximum flow and a transition to blue passing through green to display the lines with lower power flow.

&nbsp;

GIS PlotFile C:\\myFile.csv

&nbsp;

![Image](<lib/NewItem145.png>)

Figure 27. Plotting a costumized plot on the map using files

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly bring your documentation online with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
