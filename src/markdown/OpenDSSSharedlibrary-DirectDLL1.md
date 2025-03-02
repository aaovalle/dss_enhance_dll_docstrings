# OpenDSS Shared library - DirectDLL

&nbsp;

The Open-Source Distribution System Simulator (OpenDSS, or simply, DSS) is a comprehensive electrical system simulation tool for electric utility distribution systems. OpenDSS refers to the open-source implementation of the DSS. It is implemented in three forms:

&nbsp;

&#49;. A stand-alone executable program. (OpenDSS.exe)

&#50;. An in-process COM server DLL designed to be driven from a variety of existing software platforms. (OpenDSSEngine.DLL)

&#51;. A Stdcall DLL that provides all the functions of the COM server, but can be used from languages that do not support COM or that require Thread-safe execution such as on a Cloud server. (OpenDSSDirect.DLL)

&nbsp;

The direct connection shared library is a DLL that implements the same classes, properties and methods of the EPRI - OpenDSS COM interface. This alternative was generated to accelerate the In-process co-simulation between OpenDSS and external software when the client software does not support early bindings connection to COM servers/controls.

Normally, high level programming languages do not support early bindings, which make them use late bindings for data exchanging with COM servers. Late bindings procedures add an important overhead to the co-simulation process specially when executing loops.


***
_Created with the Standard Edition of HelpNDoc: [HelpNDoc's Project Analyzer: Incredible documentation assistant](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
