# External

In this mode, the storage state and dispatch values are defined by an external StorageController control element. When a StorageController takes control over a storage element, this mode is auto- matically activated for the storage element. Using StorageController enables further control modes discussed in \[[2](<References1.md#\_bookmark35>)\].

The External mode is also utilized when the user wants to take more direct control over the storage operation, which can be done through the properties *state*, *kW* , *kvar*, %*Charge*, %*Discharge*. The External mode should be selected when there is an external algorithm controlling these properties, which is usually done through COM interface, but could also be performed by scripting the simulation from a script file.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly create a professional-quality documentation website with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
