# COM Interface

&nbsp;

&nbsp;

![Image](<lib/NewItem26.png>)

&nbsp;

A Component Object Model (COM) interface was implemented with the in-process server DLL version of OpenDSS to allow knowledgeable users to use the features of the program to perform new types of studies. The direct function call DLL was added later to provide the features of the COM interface to computer languages or platforms that do not support COM, which is primarily for Microsoft Windows.

&nbsp;

Through the COM interface, the user can design and execute custom solution modes and features from an external program and perform the functions of the simulator, including definition of the model data. Thus, the DSS could be implemented entirely independently of any database or fixed text file circuit definition. For example, it can be driven entirely from a MS Office tool through VBA, or from any other 3rd party analysis program that can handle COM. Users commonly drive the OpenDSS with the familiar Mathworks MATLAB program, Python, C#, R, and other languages. This provides powerful external analytical capabilities as well as excellent graphics for displaying results.

&nbsp;

Many users find the text scripting interface of the stand-alone executable version enough for nearly all their work. As users find themselves repeatedly needing a feature for their work, the feature is implemented within the built-in solution control module and connected to the text-based command interface.

&nbsp;

The COM interface and direct-call DLL interface also provide direct access to the text-based command interface as well as access to numerous methods and properties for accessing many of the properties of the simulator's models. Through the text-based command interface, user-written programs can generate scripts to do several desired functions in sequence.&nbsp; The input may be redirected to a text file to accomplish the same effect as macros in programming environments and provide some database-like characteristics (although the program does not technically have a database). Many of the results can be retrieved through the COM interface as well as from various output files. Many output or export files are written in Comma-Separated Value (CSV) format that be imported easily into other tools such as Microsoft Excel or MATLAB® for post-processing.

&nbsp;

The experienced software developer has two additional options for using the OpenDSS tool:

&nbsp;

1. Downloading the source code and modifying it to suit special needs.
1. Developing DLLs that plug into generic containers the OpenDSS provides. This allows developers to concentrate on the model of the device of interest while letting the DSS executive take care of all other aspects of the distribution system model. Such DLLs can be written in most common programming languages.

&nbsp;

![Image](<lib/NewItem25.png>)

***
_Created with the Standard Edition of HelpNDoc: [Quickly and Easily Convert Your Word Document to an ePub or Kindle eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
