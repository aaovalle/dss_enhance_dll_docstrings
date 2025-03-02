# TechNote CommandLine

\
The DSS EXE version has long had the capability to load a script from the command line:

&nbsp;

OpenDSS filename.dss

&nbsp;

Be sure to add a QUIT command at the end of your script to close the program down. You can now also add the nogui switch to turn off an forms (windows) that might pop up. This will allow you to run OpenDSS under Apache, for example.

&nbsp;

Opendss Myfilescript.DSS /nogui

&nbsp;

Thus, you can now make a batch file that will execute a series of scripts from the command line.

&nbsp;

Be sure to export some of your results to some file that you can later retrieve by using a Show or Export command in your script. Also, make sure each script has a unique circuit name or are in separate folders so that all the exported files are saved uniquely.

&nbsp;

The Quit command has no effect in the DLL version since it is the responsibility of the parent program to terminate

things.

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Support Your Windows Applications with HelpNDoc's CHM Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
