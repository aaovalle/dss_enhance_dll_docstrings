# Introduction to OpenDSS

&nbsp;

**What is OpenDSS ?**

&nbsp;

![Image](<lib/NewItem26.png>)

&nbsp;

The Open-Source Distribution System Simulator (*OpenDSS*, previously known as simply *DSS*) is a comprehensive electrical system simulation tool for electric utility distribution systems. OpenDSS refers to the open-source implementation of the DSS program originally developed in 1997 and made open source by EPRI in 2008. In its fundamental form, the program&nbsp; is implemented as a fairly straightforward stand-alone executable (.exe) program that may be installed simply by copying to a disk. On the Windows platform, it is also implemented in a DLL that is registered as an *in-process COM server* upon installation. This allows the program to be driven from a variety of other software programs used in power system analysis, including user-written software. On platforms that do not support COM, DLLs are provided that duplicate the COM interface with standard function call interfaces.&nbsp;

The executable version adds a basic text-based scripting interface to the solution engine to assist users in developing scripts and viewing solutions. The scripting commands are available in all forms of the program, including OpenDSS-G, which provides a graphical interface.

The program supports nearly all RMS steady‐state (i.e., frequency domain) analyses commonly performed for utility distribution systems planning and analysis. In addition, it supports many new types of analyses that are designed to meet future needs, many of which are being dictated by the deregulation of utilities worldwide and the advent of the “smart grid”. Many of the features found in the program were originally intended to support distributed generation analysis needs. Other features support energy efficiency analysis of power delivery, smart grid applications, and harmonics analysis. The DSS is designed to be indefinitely expandable so that it can be easily modified to meet future needs.

&nbsp;

The OpenDSS program has been used for:&nbsp;

• Distribution Planning and Analysis&nbsp;

• General Multi-phase AC Circuit Analysis&nbsp;

• Analysis of Distributed Generation Interconnections&nbsp;

• Annual Load and Generation Simulations &nbsp;

• Wind Plant Simulations&nbsp;

• Analysis of Unusual Transformer Configurations&nbsp;

• Harmonics and Interharmonics analysis&nbsp;

• Neutral-to-earth Voltage Simulations&nbsp;

• Development of IEEE Test feeder cases&nbsp;

• And more ….&nbsp;

&nbsp;

Another major strength of OpenDSS is in its “quasi‐static” solution modes which lend themselves well to sequential time simulations, like analyzing how a circuit will perform over an entire year. The program has several built‐in solution modes, such as

&nbsp;

• Snapshot Power Flow

• Daily Power Flow

• Yearly Power Flow

• Harmonics

• Dynamics

• Fault study

• Monte Carlo Fault study

• And others …

&nbsp;

These modes were added as the program evolved to meet the analysis needs of specific projects the authors were involved with. However, the program was designed with the recognition that developers would never be able to anticipate everything users will want to do with it. A Component Object Model (COM) interface was implemented on the in-process server DLL version of the program to allow knowledgeable users to use the features of the program to perform new types of studies.

&nbsp;

Through the [COM interface](<COMInterface.md>), the user is able to design and execute custom solution modes and features from an external program and perform the functions of the simulator, including definition of the model data. Thus, the DSS could be implemented entirely independently of any database or fixed text file circuit definition. For example, it can be driven entirely from a MS Office tool through VBA, or from any other 3rd party analysis program that can handle COM. Users commonly drive the OpenDSS with the familiar Mathworks MATLAB program, Python, C#, R, and other languages. This provides powerful external analytical capabilities as well as excellent graphics for displaying results.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily Add Encryption and Password Protection to Your PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
