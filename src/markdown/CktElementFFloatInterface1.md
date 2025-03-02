# CktElementF (Float) Interface

# This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double CktElementF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a float (IEEE 754 64 bits) with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: CktElement.NormalAmps - read

This parameter will deliver the normal ampere rating for the active PDElement.

&nbsp;

### Parameter 1: CktElement.NormalAmps - Write

This parameter allows to fix the normal ampere rating for the active PDElement. The new value must be defined in the variable “Argument”.

&nbsp;

### Parameter 2: CktElement.EmergAmps - read

This parameter will deliver the Emergency ampere rating for the active PDElement.

&nbsp;

### Parameter 3: CktElement.EmergAmps - Write

This parameter allows to fix the Emergency ampere rating for the active PDElement. The new value must be defined in the variable “Argument”.

&nbsp;

### Parameter 4: CktElement.Variablei 

This parameter delivers get the value of a variable by index for the active PCElement.

&nbsp;

### Parameter 5: CktElement.SetActiveVariable

Sets the value given at the Argument into the active state variable for the active circuit element. The variable must be activated by using “ActiveVariableName” (CktElementS) or “ActiveVariableIdx” (CktElementI) before using this function. If the value assignment is successful, the function will return 0, otherwise, it will return -1.

&nbsp;

### Parameter 6: CktElement.GetActiveVariable

Gets the value of the active state variable for the active circuit element. The variable must be activated by using “ActiveVariableName” (CktElementS) or “ActiveVariableIdx” (CktElementI) before using this function, otherwise, the value returned will not correspond to the expected one.


***
_Created with the Standard Edition of HelpNDoc: [Don't be left in the past: convert your WinHelp HLP help files to CHM with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
