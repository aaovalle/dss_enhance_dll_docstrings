# GICSourcesF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double GICSourcesF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: GICSources.EN read

This parameter returns the Northward E Field V/km of the active GICSource.

&nbsp;

### Parameter 1: GICSources.EN write

This parameter allows to specify the Northward E Field V/km for the active GICSource.

&nbsp;

### Parameter 2: GICSources.EE read

This parameter returns the Eastward E Field, V/km for the active GICSource.

&nbsp;

### Parameter 3: GICSources.EE write

This parameter allows to specify the Eastward E Field V/km for the active GICSource.

&nbsp;

### Parameter 4: GICSources.Lat1 read

This parameter returns the Latitude of Bus1 (degrees) of the active GICSource.

&nbsp;

### Parameter 5: GICSources.Lat1 write

This parameter allows to specify the Latitude of Bus1 (degrees) for the active GICSource.

&nbsp;

### Parameter 6: GICSources.Lat2 read

This parameter returns the Latitude of Bus2 (degrees) of the active GICSource.

&nbsp;

### Parameter 7: GICSources.Lat2 write

This parameter allows to specify the Latitude of Bus2 (degrees) for the active GICSource.

&nbsp;

### Parameter 8: GICSources.Lon1 read

This parameter returns the Longitude of Bus1 of the active GICSource.

&nbsp;

### Parameter 9: GICSources.Lon1 write

This parameter allows to specify the Longitude of Bus1 for the active GICSource.

&nbsp;

### Parameter 10: GICSources.Lon2 read

This parameter returns the Longitude of Bus2 of the active GICSource.

&nbsp;

### Parameter 11: GICSources.Lon2 write

This parameter allows to specify the Longitude of Bus2 for the active GICSource.

&nbsp;

### Parameter 12: GICSources.Volts read

This parameter returns the Specify dc voltage of the active GICSource.

&nbsp;

### Parameter 13: GICSources.Volts write

This parameter allows to specify the Specify dc voltage directly for the active GICSource.


***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of HelpNDoc for CHM Help File Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
