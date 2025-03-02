# OpenDSS GUI

&nbsp;

OpenDSS is packaged with a Graphical User Interface (GUI) which provides a structured environment for the creation and analysis of power system cases. The GUI is one of two primary methods users can interact with the OpenDSS solution engine; the other is via the COM interface which is discussed in the section[ Introduction to the COM Interface](<COMInterface.md>) of this manual.

&nbsp;

It should be noted that the GUI is more of a tool to aid with analysis of OpenDSS circuits and the creation and debugging of scripts (see The[ Basics of the OpenDSS Scripting Language](<BasicsoftheOpenDSSScriptingLangu.md>)) rather than a replacement for scripting. Communication to the DSS is fundamentally accomplished through text strings passed to the OpenDSS command processor. Scripts or script fragments are executed by:

&nbsp;

&#49;. Selecting the script lines to be executed.

&#50;. The user can then right-click on the selection and then click on the Do Selected option, which has a short-cut key of Ctrl‐D.

&#51;. The selection may also be executed from the Do menu or the speed button directly below the Do menu item.

&nbsp;

All commands executed via the GUI have a counterpart in the OpenDSS scripting language. it can be acceded thought the Command and Element Properties Reference, accessible with the GUI through Help \> OpenDSS Help. One can also record the actions performed in the GUI to a .dss file using the record commands tool under Edit \> Record Script.

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Help Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com>)_
