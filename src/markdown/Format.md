# Format

&nbsp;

Formats the coordinates located at the first 2 places of the coordinates buffer. The first argument indicates the original format and the second argument the destination format. The format can be one of the following:

&nbsp;

\- LatLong (latitude, Longitude - WGS84))

\- DMS (Degrees, minutes, seconds)

\- UTM (Universal Transverse Mercator)

\- USNG

&nbsp;

The data needs to be entered in the file following a strict convention:

&nbsp;

LatLong: Latitude\|Longitude. E.g. 36.28711454\|-83.49819683

DMS: DegreeMinuteSecondNDegreeMinuteSecondW. E.g. 361713.6N0832953.5W

UTM: ZoneLatitudeLongitude. E.g. 17N2756404018690

USNG: ZoneCoords. E.g. 17SKA75641869

&nbsp;

For example, consider converting the coordinates 35.07053683, -85.15665416 (latitude, longitude WGS84) to UTM format, then the command will be as follows:

&nbsp;

GIS Format latlong utm 35.07053683\|-85.15665416

&nbsp;

The output will be displayed at the results tab of the executable panel in OpenDSS.

&nbsp;

The following conditions need to be fulfilled:

&nbsp;

&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

&#51;. The model needs to have the correct GISCoords file

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize your documentation process with HelpNDoc's online capabilities](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
