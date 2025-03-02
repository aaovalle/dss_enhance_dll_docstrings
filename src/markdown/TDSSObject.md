# TDSSObject

| ***TDSSObject*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description – (Specific class) otherwise generic* |
| **Property- private** | Get\_PropertyValue | Returns the value of the property given by index. The value is returned as string. |
| **Method- private** | Set\_PropertyValue | Sets the property value (String) for the property given by index in the argument. |
| **Property- private** | Get\_Name | Returns the name of the caller. |
| **Method- private** | Set\_Name | Sets the name of the caller using the string given in the argument. |
| **Property- protected** | GetNextPropertySet | Find next larger property sequence number returns 0 if none found. |
| **Property- public** | GetPropertyValue | Uses dssclass.propertyindex to get index by name, returns the value as string. |
| **Method- public** | InitPropertyValues | Routine for initializing the caller’s property values. |
| **Method- public** | DumpProperties | Implements the routine for writing the local properties down into a plain text file at the end. |
| **Method- public** | SaveWrite | Writes into the given plain text file only properties that were explicitly set in the final order they were actually set. |
| **Method- public** | ClearPropSeqArray | Clears the property array for the caller. |
| **Property- public** | PropertyValue | PA Get\_PropertyValue, Set\_PropertyValue. |
| **Property- public** | Name | PA Get\_Name, Set\_Name. |



***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Review with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
