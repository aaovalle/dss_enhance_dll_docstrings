# PlotPoint

&nbsp;

With this command the user can plot a mark on the map. The name of the shape for the mark must be specified in the argument and can be one of the following:

&nbsp;

&#49;. Circle

&#50;. Cross

&#51;. Diamond

&#52;. Square

&#53;. Triangle

&#54;. X

&nbsp;

The size of the mark can be specified in pixels using the option GISThickness, the color of the mark can be specified using the option GISColor. By default, the size is 3 pix and color red (0xFF0000).\
\
For example, assume that the user wants to plot a blue triangle at -118.59292195047032692, 34.22088014327628969, then, the OpenDSS code will be as follows:

&nbsp;

set GISCoords = \[-118.59292195047032692,34.22088014327628969\]

set GISThickness = 15 GISColor=0000FF

GIS PlotPoint triangle

***
_Created with the Standard Edition of HelpNDoc: [Make Your PDFs More Secure with Encryption and Password Protection](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
