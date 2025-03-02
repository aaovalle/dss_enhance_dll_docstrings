# Loads S (String) Interface

&nbsp;

This interface can be used to read/modify the properties of the Loads Class where the values are strings. The structure of the interface is as follows:

&nbsp;

CStr DSSLoadsS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string, the variable “parameter” (Integer) is used to specify the property of the class to be used and the variable “argument” (string) can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

### Parameter 0: Loads.Name – Read

This parameter allows to read the Name property of the active load. The parameter argument can be filled with an empty string.

&nbsp;

### Parameter 1: Loads.Name – Write

This parameter allows to set the active load by specifying the Name load. The parameter argument must contain the Name of the load to activate. The return value will be equal to empty.

&nbsp;

### Parameter 2: Loads.CVRCurve – Read

This parameter allows to read the CVRCUrve property of the active load. The parameter argument can be filled with an empty string.

&nbsp;

### Parameter 3: Loads.CVRCurve – Write

This parameter allows to set the CVRCurve property for the active load. The parameter argument must contain the Name of the new CVRCurve to be linked to the active load. The return value will be equal to empty.

&nbsp;

### Parameter 4: Loads.daily – Read

This parameter allows to read the daily property of the active load. The parameter argument can be filled with an empty string.

&nbsp;

### Parameter 5: Loads.daily – Write

This parameter allows to set the daily property for the active load. The parameter argument must contain the Name of the new daily to be linked to the active load. The return value will be equal to empty.

&nbsp;

### Parameter 6: Loads.duty – Read

This parameter allows to read the duty property of the active load. The parameter argument can be filled with an empty string.

&nbsp;

### Parameter 7: Loads.duty – Write

This parameter allows to set the duty property for the active load. The parameter argument must contain the Name of the new duty to be linked to the active load. The return value will be equal to empty.

&nbsp;

### Parameter 8: Loads.Spectrum – Read

This parameter allows to read the Spectrum property of the active load. The parameter argument can be filled with an empty string.

&nbsp;

### Parameter 9: Loads.Spectrum – Write

This parameter allows to set the Spectrum property for the active load. The parameter argument must contain the Name of the new Spectrum to be linked to the active load. The return value will be equal to empty.

&nbsp;

### Parameter 10: Loads.Yearly – Read

This parameter allows to read the Yearly property of the active load. The parameter argument can be filled with an empty string.

&nbsp;

### Parameter 11: Loads.Yearly – Write

This parameter allows to set the Yearly property for the active load. The parameter argument must contain the Name of the new Yearly to be linked to the active load. The return value will be equal to empty.

&nbsp;

### Parameter 12: Loads.Growth – Read

This parameter allows to read the Growth property of the active load. The parameter argument can be filled with an empty string.

&nbsp;

### Parameter 13: Loads.Growth – Write

This parameter allows to set the Growth property for the active load. The parameter argument must contain the Name of the new Growth to be linked to the active load. The return value will be equal to empty.

&nbsp;

### Parameter 14: Loads.Sensor

This parameter returns the name of the sensor monitoring the active load.


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
