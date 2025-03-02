# JSONRoute

&nbsp;

Exports the JSON script describing the last route calculated between 2 buses into a text file. The output from OpenDSS is the path to the JSON file. The JSON file contains all the details of the route, including steps, hints, and locations, among other information that may results interesting for the user. The following is an extract of the JSON generated for the route calculated above:

&nbsp;

{"code":"Ok","waypoints"\[{"hint":"s1MuhctTLoWZAAAAwgAAAOkAAAA2AAAAPNh\_QjNooUJAxcFCIZ6zQZkAAADCAAAA6QAAADYAAAB8QwAAEBf8-mshJALfF\_z6rCAkAgMATw7FAVHD","distance":28.251245,"location":\[-84.14232,35.922283\],"name":""},{"hint":"r3uQgOl7kIA3AAAAHgAAAAAAAAAAAAAAjseeQujnKEIAAAAAAAAAADcAAAAeAAAAAAAAAAAAAAB8QwAACgP8-hPpIwK-Avz60-gjAgAAbwjFAVHD","distance":9.87283,"location":\[-84.147446,35.907859\],"name":"Lovell Road"}\],"routes":\[{"legs":\[{"steps":\[{"intersections":\[{"out":0,"entry":\[true\],"location":\[-84.14232,35.922283\],"bearings":\[49\]}\],"driving\_side":"right","geometry":"gagzEn\`q\`OkAiBlAuA\\\\Q\\\\Y","duration":44.5,"distance":160.9,"name":"","weight":44.5,"mode":"driving","maneuver":{"bearing\_after":49,"location":\[-84.14232,35.922283\],"type":"depart","bearing\_before":0,"modifier":"right"}},{"intersections":\[{"out":0,"in":2,"entry":\[true,true,false\],"location":\[-84.141136,35.921972\],"bearings":\[45,225,330\]}\],"driving\_side":"right","geometry":"i\_gzEbyp\`OWa@GIkAiBYe@iAmA","duration":26.6,"distance":166.3,"name":"Corridor Park Boulevard","weight":26.6,"mode":"driving","maneu…

&nbsp;

For more information about the JSON string visit [http://project-osrm.org/docs/v5.24.0/api/#.](<http://project-osrm.org/docs/v5.24.0/api/#> "target=\"\_blank\"")

&nbsp;

The following conditions need to be fulfilled:

&nbsp;

&#49;. OpenDSS-GIS must be installed

&#50;. OpenDSS-GIS must be initialized (use GIS Start command)

&#51;. GISFindRoute has been executed at some point before this command (at least once)

&#52;. The model needs to have the correct GISCoords file

***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
