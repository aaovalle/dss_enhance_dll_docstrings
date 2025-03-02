# MonitorsV (variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void  MonitorsV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

&nbsp;

In this version of the DLL the API requires 4 arguments Some of these arguments are informative while others provide data access through memory address. This avoids creating unnecessary copies of the same data across the system. The 4 arguments used in this API are:

&nbsp;

* Parameter: Indicates the data array that wants to be accessed/written.
* Pointer: Is the pointer to the array structure.
* Type: Is the type of data contained in the structure, it can be one of: 0 - Boolean, 1- Integer (32 bit), 2- double (64 bit), 3- Complex, 4- String.
* Size: Is the size in Bytes of the structure, it only considers the elements inside the structure without the identifiers added by DSS. In the case of array of strings includes the null byte (0) between the elements of the array.  

&nbsp;

The return values depend on the given Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Monitors.AllNames

This parameter returns a pointer to an array of bytes containing the names of all the existing monitors in the project. Each string is separated by a NULL (0) character. 

&nbsp;

### Parameter 1: Monitors.ByteStream

This parameter returns a pointer to an array of bytes containing monitor stream values. Make sure a "save" is done first (standard solution modes do this automatically). In this case, the Type argument will signal to String type, but the data is not separated by Null (0) characters.

&nbsp;

### Parameter 2: Monitors.Header

This parameter returns a pointer to an array of bytes containing the header string; Each string is separated by a NULL (0) character. 

&nbsp;

### Parameter 3: Monitors.dblHour

This parameter returns a pointer to an array of double containing the time value in hours for the time-sampled monitor values; empty if frequency-sampled values for harmonics solution (see dblFreq).

&nbsp;

### Parameter 4: Monitors.dblFreq

This parameter returns a pointer to an array of doubles containing the time values for harmonics mode solutions; empty for time mode solutions (use dblHour).

&nbsp;

### Parameter 5: Monitors.Channel

This parameter returns a pointer to an array of doubles containing the values for the channel specified in the argument Pointer (usage: MyArray = DSSmonitor.Channel(i)) A save or SaveAll should be executed first. Done automatically by most standard solution modes. The pointer provided by the caller in the argument "Pointer", must be directed to an integer containing the channel number of interest.


***
_Created with the Standard Edition of HelpNDoc: [Create Professional CHM Help Files with HelpNDoc's Easy-to-Use Tool](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
