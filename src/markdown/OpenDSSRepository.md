# OpenDSS Repository

OpenDSS is an electric power distribution system simulator (DSS) designed to support distributed energy resource (DER) grid integration and grid modernization. It enables engineers to perform complex analyses using a flexible, customization, and easy to use platform intended specifically to meet current and future distribution system challenges and provides a foundation for understanding and integrating new technologies and resources. This power system analysis software tool was translated from the Delphi computer language into C++ to make it accessible to a larger community of software developers and used as a core library upon which to build new capabilities.&nbsp;

&nbsp;

The OpenDSS software repository has a file distribution as shown in Figure 1.&nbsp;

![A picture containing text

Description automatically generated](<lib/NewItem609.png>)

**Figure 1. Snapshot of the OpenDSS-X copy obtained from the repository**

&nbsp;

The content of the folders contained in the project structure is as indicated in Table 1.&nbsp;

&nbsp;

**Table 1. Contents of OpenDSS-X software repository**

| ***Folder name*** | ***Description*** |
| --- | --- |
| **CMD** | Contains the main project files. The project was designed for compatibility with CMake, facilitating the cross-platform adoption without losing some of the C++ semantics introduced by other vendors. In this folder the user will find the main project file (OpenDSSX.cpp), the CMake configuration files and the external libraries such as KLUSolve.dll and its Linux equivalents. |
| **Common** | Contains the routines and objects commonly used across the program for simulation purposes. Utilities, Solution and Circuit are some examples of the units that can be found in this folder. |
| **Controls** | Contains the objects implemented as controls in the simulation. Controls are objects that can modify the behavior of a set of elements (it can be 1) using the feedback from a monitored part of the circuit model. Regulators, capacitor controls, smart inverters are some examples of the control that can be found in this folder. |
| **Executive** | Contains all the routines and objects that interpret commands given using the OpenDSS-X scripting language, redirecting the program internally to perform the actions commanded by the user using this language. |
| **Forms** | Contains the routines for returning messages to the user. The messages can be confirmation, warnings, or errors. This is the equivalent for command line of the VCL forms implemented in the original OpenDSS written in Delphi. |
| **General** | Contains the objects representing libraries that can be use to simplify the elements’ description within a script. LineCodes, LineGeometries, TransformerCodes and XYCurves are examples of these objects. |
| **GISCommands** | Contains the commands for interacting with OpenDSS-GIS. Not available in OpenDSS-X but is in the repository to mimic the file distribution in the original version (Delphi). |
| **Meters** | Contains the code for the objects representing meters, monitors and sensor like elements that can be deployed across the circuit model for capturing simulation values.&nbsp; |
| **MyOpenDSS** | Contains a set of files that can be used as template for external user models.&nbsp; |
| **Parallel\_Lib** | Implements the routines and objects needed for performing parallel processing related operations. |
| **Parser** | Contains the objects implementing parsers and RPN for interpreting numbers and mathematical expressions when processing commands in OpenDSS-X scripting language. |
| **PCElements** | Contains the code for the objects describing Power Conversion Elements (PCEs). These are normally connected in shunt across the model. Loads, capacitors, energy storage are some examples of PCEs. |
| **PDElements** | Contains the code for the objects describing Power Delivery Elements (PDEs). These can have 2 terminals and are normally connected in series across the model for energy transport. Transformers, lines, and series connected capacitors are some examples of PDEs. |
| **Shared** | Contains routines shared by multiple objects across the program. They are vital for the program operation. |
| **Support** | Contains the routines implemented for reproducing the operation of Delphi specialized commands in C++. These routines are fundamental for the program operation since many of the commands that can be fund across the code are not C++ native. |



***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Support Your Windows Applications with HelpNDoc's CHM Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
