# Specific classes

| ***Specific classes*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description – (Specific class) otherwise generic* |
| **Method- protected** | InterpretConnection | Interprets the connection string provided when declaring a load connection type (wye/delta). –(TLoad, TGenerator, TPVSystem, TStorage) |
| **Method- protected** | SetNcondsForConnection | Sets the number of conductors for the load depending on the connection type. –(TLoad, TIndMach012, TGenerator, TPVSystem, TStorage) |
| **Property- protected** | MakeLike | Copy the properties from another element within the same class. |
| **Method- protected** | DefineProperties | Add Properties of this class to for this object. It also initializes the more generic class properties. |
| **Method- public** | Edit | Overrides the method at the more generic class definition, it implements the routine for editing the properties of the element when declared/edit. |
| **Method- public** | Init | Overrides the method at the more generic class definition, it implements the routine for initializing the properties of the element when declared/edit. |
| **Method- public** | NewObject | Overrides the method at the more generic class definition, it implements the routine for adding a new object to the list of elements within the active class. |
| **Method- private** | IsourceSetBus1 | Sets the name and terminals for bus 1 of this element. – (TISource) |
| **Method- private** | VsourceSetBus1 | Sets the name and terminals for bus 1 of this element. –(TVSource) |
| **Method- protected** | GICLineSetBus1 | Sets the name and terminals for bus 1 of this element. –(TGICLine) |
| **Method- public** | ResetRegistersAll | Resets the registers (Local energy meter) for this element. – (TGenerator, YPVSystem) |
| **Method- public** | SampleAll | Force all registers (local energy meter) for this element take a sample. – (TGenerator) |
| **Method- public** | UpdateAll | Intended to update all enabled energy system levels, not implemented to date for TPVSystem. – (TPVSystem, TStorage) |
| **Method- private** | VscSetBus1 | Sets the name and terminals for bus 1 of this element. – (TVSConveter) |


&nbsp;

&nbsp;

![Diagram

Description automatically generated](<lib/NewItem607.png>)

**Figure 1. PCE object inheritance tree**

***
_Created with the Standard Edition of HelpNDoc: [Full-featured Documentation generator](<https://www.helpndoc.com>)_
