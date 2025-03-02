# OpenDSS Parallel Processing Suite

&nbsp;

&nbsp;

&nbsp;

The classic OpenDSS program is a simulation platform built for execution in a single, sequential process. Each procedure/function is called from each object sequentially to perform a QSTS simulation. The performance that can be achieved is based on the structure of the low-level routines, the simplicity of the routines and the efficiency of the compiler.

&nbsp;

EPRI has explored several methods to accomplish parallel processing in OpenDSS, including the parallelization of the whole program using a different interface (the Direct DLL API) and the modification of the solver using other programming languages, among other methods. However, these approaches demand significant extra work for the user and will be always tied to an interface. Consequently, desirable features that users are accustomed to, such as the COM interface, would be at risk of being deprecated for this type of processing.

&nbsp;

EPRI has evolved OpenDSS into a more modular, flexible and scalable parallel processing platform with the following guidelines:

&nbsp;

&#49;. The parallel processing machine will be interface-independent

&#50;. Each component of the parallel machine should be able to work independently

&#51;. The simulation environment should deliver information consistently

&#52;. The data exchange between the components of the parallel machine should respect the interface rules and procedures

&#53;. The user handle of the parallel machine should be easy and support the already acquired knowledge of OpenDSS users

***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
