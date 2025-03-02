# PlotPoints

&nbsp;

With this command the user can plot a customized set of shapes on top of the map. The path to the file containing the plot is the argument for this command. The file contains the coordinates, shape, color and thickness for each mark, comma separated values as follows:

&nbsp;

…

myLong1,myLat1,myShape1,myColor1,mySize1

myLong2,myLat2,myShape2,myColor2,mySize2

myLong3,myLat3,myShape3,myColor3,mySize3

…

&nbsp;

Where myLongX and myLatX are longitude and latitude where the mark will be placed. myShapeX is an integer representing the shape that the user wants to draw, it can be one of the following:

&nbsp;

&#48;. Circle

&#49;. Cross

&#50;. Diamond

&#51;. Square

&#52;. Triangle

&#53;. X

&nbsp;

myColorX is the color of the mark and mySizeX is the size expressed in pixels. X refers to the index for differenciating data within the given example. At Figure 28, there is an example for plotting the power flow across the feeder using red as the for the lines with maximum flow and a transition to blue passing thorugh green to display the lines with lower power flow.

&nbsp;

![Image](<lib/NewItem146.png>)

Figure 28. Plotting a costumized set of marks on the map using files

&nbsp;

GIS PlotPoints C:\\myPointsFile.csv

&nbsp;

The content of the file plotted at Figure 28 is as follows:

&nbsp;

\-118.59292195047032692,34.22088014327628969,0,FF0000,13

\-118.59304844439994042,34.22092078111747071,1,00FF00,13

\-118.59292235908066004,34.22123360816988225,2,0000FF,13

\-118.59071510141255601,34.21981100373600526,3,FF00FF,13

\-118.59062557916303149,34.22016247763471597,4,FFFF00,13

\-118.59292209798299211,34.22055454182444834,0,00FFFF,13

\-118.5917951321892474,34.22211120247868621,1,FF000F,13

\-118.59071510141255601,34.21981100373600526,2,FF0F00,13

\-118.59619816989912522,34.22211095793186786,3,FF00F0,13

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Don't Let Unauthorized Users View Your PDFs: Learn How to Set Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
