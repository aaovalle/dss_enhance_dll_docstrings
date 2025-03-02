# BatchFormat

&nbsp;

Formats the coordinates within the file specified. The first argument indicates the original format and the second argument the destination format. The third argument is the path to the source file containing the coordinates, which should be organized in 2 columns comma separated. The format can be one of the following:

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

For example, consider a file containing the following coordinates in Latitude-Longitude format (WGS84):

&nbsp;

&#51;6.28711454\|-83.49819683

&#51;6.30546503\|-83.43104901

&#51;6.30477455\|-83.43186156

&#51;6.30477455\|-83.43186156

&#51;6.30643529\|-83.4312484

&nbsp;

The command for converting this file to UTM format, located at C:\\Temp\\myFile.txt, will be as follows:

&nbsp;

GIS BatchFormat latlong utm C:\\Temp\\myFile.txt

&nbsp;

The converted file will be saved as myFileutm.txt at the same folder and will look as follows:

&nbsp;

&#49;7N 275640 4018690

&#49;7N 281723 4020572

&#49;7N 281648 4020497

&#49;7N 281648 4020497

&#49;7N 281708 4020680

&nbsp;

The following conditions need to be fulfilled:

&nbsp;

&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

&#51;. The model needs to have the correct GISCoords file

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Streamline your documentation process with HelpNDoc's WinHelp HLP to CHM conversion feature](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
