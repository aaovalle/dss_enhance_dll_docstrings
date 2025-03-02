# GISCoords

&nbsp;

The first step before using OpenDSS-GIS is to define the GIS coordinates for the active model in OpenDSS. The GIS coordinates can be defined using the GISCoords command in the same way the BusCoords are defined, this is, by typing the commands and using the path to the file containing the GIS coordinates as argument:

&nbsp;

GISCoords myFilePath

&nbsp;

The GIScoords file format is like the BusCoords file, it is composed by comma separated values that include the name of the bus, the latitude and longitude.

&nbsp;

…

MyNode1,xx.xxxxxxxx,-xx.xxxxxxxx

MyNode2,xx.xxxxxxxx,-xx.xxxxxxxx

MyNode3,xx.xxxxxxxx,-xx.xxxxxxxx

MyNode4,xx.xxxxxxxx,-xx.xxxxxxxx

…

&nbsp;

If this file is not defined in the model, the model’s schematic cannot be displayed on the map.

***
_Created with the Standard Edition of HelpNDoc: [Why Microsoft Word Isn't Cut Out for Documentation: The Benefits of a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
