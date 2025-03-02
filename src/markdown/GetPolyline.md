# GetPolyline

&nbsp;

This command returns the coordinates of the polyline drawn by the user after using the command StopDraw. The coordinates will be returned in WGS 84 format in a JSON string containing all the vertices describing the form. For example:

&nbsp;

{paths:\[\[\[-83.523235799526304,36.211851362079948\],

\[-83.522507458110596,36.212900759076554\],

\[-83.520912020397404,36.21320859009181\],

\[-83.520270368033351,36.212564972457137\],

\[-83.519663414327567,36.213222591374503\],

\[-83.519004431288977,36.213530413962665\],

\[-83.519576712729815,36.21383822592572\]\]\],

spatialReference:{wkid:4326}}

&nbsp;

The following conditions need to be fulfilled:

&nbsp;

&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

***
_Created with the Standard Edition of HelpNDoc: [Bring your WinHelp HLP help files into the present with HelpNDoc's easy CHM conversion](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
