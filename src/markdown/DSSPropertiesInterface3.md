# DSSProperties Interface

&nbsp;

This interface can be used to read/write certain properties of DSS objects. The structure of the interface is as follows:

&nbsp;

CStr DSSProperties(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string pointer (ANSI) with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

## Parameter 0: DSSProperties.Name

This parameter will deliver the name of the active property. This parameter will deliver the name of the active property. The index of the property must be specified in the argument. The index minimum value is 1. This value must be entered as string.

&nbsp;

## Parameter 1: DSSProperties.Description

This parameter will deliver the description of the active property. This parameter will deliver the name of the active property. The index of the property must be specified in the argument. The index minimum value is 1. This value must be entered as string.

&nbsp;

## Parameter 2: DSSProperties.Value - read

This parameter will deliver the value of the active property. This parameter will deliver the name of the active property. The index of the property must be specified in the argument. The index minimum value is 1. This value must be entered as string.

&nbsp;

## Parameter 3: DSSProperties.Value - Write

This parameter will allow to set the value of the active property. The new value must be specified in the variable “argument” as string. This parameter will deliver the name of the active property. The index of the property must be specified in the argument. The index minimum value is 1. This value must be entered as string.


***
_Created with the Standard Edition of HelpNDoc: [Make Help Documentation a Breeze with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
