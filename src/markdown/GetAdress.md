# GetAdress

&nbsp;

Returns the address at the given coordinates. The coordinates must be defined using GISCoords, LoadBus can also be used with this command. This command doesn’t have arguments, but it requires the user to previously define the coordinates for the point of interest as follows:

&nbsp;

set GISCoords = \[35.92214527098195, -84.14210580168506\]

GIS GetAddress

&nbsp;

The answer from OpenDSSiGIS is a JSON string describing the address details. Using the commands above, the response from OpenDSS-GIS will be as follows:

&nbsp;

{ "address": { "Match\_addr": "900-998 Corridor Park Blvd, Knoxville, Tennessee, 37932", "LongLabel": "900-998 Corridor Park Blvd, Knoxville, TN, 37932, USA", "ShortLabel": "900-998 Corridor Park Blvd", "Addr\_type": "StreetAddress", "Type": "", "PlaceName": "", "AddNum": "970", "Address": "970 Corridor Park Blvd", "Block": "", "Sector": "", "Neighborhood": "", "District": "", "City": "Knoxville", "MetroArea": "", "Subregion": "Knox County", "Region": "Tennessee", "Territory": "", "Postal": "37932", "PostalExt": "", "CountryCode": "USA" }, "location": { "x": -84.14173410620927, "y": 35.921630248787075, "spatialReference": { "wkid": 4326, "latestWkid": 4326 } } }

&nbsp;

The following conditions need to be fulfilled:

&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly optimize your documentation website for search engines](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
