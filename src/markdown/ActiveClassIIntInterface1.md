# ActiveClassI (Int) Interface

&nbsp;

This interface can be used to read/modify the properties of the ActiveClass Class where the values are integers. The structure of the interface is as follows:

&nbsp;

int32\_t ActiveClassI(int32\_t Parameter, int32\_t argument);

&nbsp;

This interface returns an integer (signed 32 bits), the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: ActiveClass.First

This parameter sets first element in the active class to be the active DSS object. If object is a CktElement, ActiveCktElement also points to this element. Returns 0 if none.

&nbsp;

### Parameter 1: ActiveClass.Next

This parameter sets next element in the active class to be the active DSS object. If object is a CktElement, ActiveCktElement also points to this element. Returns 0 if none.

&nbsp;

### Parameter 2: ActiveClass.NumElements

This parameter gets the number of elements in this class. Same as Count Property.

&nbsp;

### Parameter 3: ActiveClass.Count

This parameter gets the number of elements in this class. Same as NumElements Property.


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Intuitive Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
