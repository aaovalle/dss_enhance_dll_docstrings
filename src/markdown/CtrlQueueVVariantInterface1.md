# CtrlQueueV (Variant) Interface

&nbsp;

This interface can be used to read/modify the properties of the CtrlQueue Class where the values are array-based. The structure of the interface is as follows:

&nbsp;

void CtrlQueueV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: CtrlQueue.CtrlQueue

This parameter returns a pointer to an array of string with the control actions contained in the CtrlQueue after the latest solve command. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 1: CtrlQueue.Push

This parameter pushes a control action onto the DSS control queue by time, action code, and device handle. The caller must provide a pointer to the array of doubles containing the hour, seconds, ActionCode and device handle in the argument "Pointer". After the control action is pushed into the queue, the control action handle will be returned in the argument Size. In case of an error, this argument will be updated with one of the following codes:

&nbsp;

&#49;. -10001 : The input array is incomplete


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
