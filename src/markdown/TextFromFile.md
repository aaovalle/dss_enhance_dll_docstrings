# TextFromFile

&nbsp;

Prints the text within a file given in the argument on the map. The text features as coordinates, color and font size are specified within the file. The command must be used as follows:

&nbsp;

GIS TextFromFile C:\\MyFilepath\\myGISText.txt

&nbsp;

The file extension is not relevant. The file’s content must follow the following order:

…

myLong1,myLat1,myText1,myColor1,myFontSize1

myLong2,myLat2,myText2,myColor2,myFontSize2

myLong3,myLat3,myText3,myColor3,myFontSize3

…

For example, assume that the content of the file mentioned in the example above is as follows:

&nbsp;

&#51;5.92209179726962,-84.14211464700368,my Location 1,FF0000,20

&#51;5.90779395922772,-84.14752180168537,my Location 2,FFFF00,14

&nbsp;

The result in OpenDSS-GIS will be as shown in Figure 38.

&nbsp;

![Image](<lib/NewItem156.png>)\
Figure 38. Printing text from a file on the map

***
_Created with the Standard Edition of HelpNDoc: [Experience a User-Friendly Interface with HelpNDoc's Documentation Tool](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
