# TechNote Adding Custom Classes

&nbsp;

*The OpenDSS has a large number of classes that implement many types of power system components and controls. Some examples of class types are:*

&nbsp;

•*Line*

•*Transformer*

•*Load*

•*Loadshape*

•*Storage element*

•*Control classes such as the*

*\-capacitor control,*

*\-regulator control, and*

*\-storage control*

&nbsp;

New class types are being added to the open source version of OpenDSS as needs arise and in response to user feedback. However, if a feature is not presently available, a user with coding experience can program classes to implement virtually any desired power system component and/or control.

&nbsp;

Recently, the MyOpenDSS project was added to the OpenDSS code base was updated to allow a programmer to more easily add custom classes that implement desired characteristics and behavior. It is also easier co create your own private version of the program while still having access to the lastest OpenDSS updates via simple SVN updating.

&nbsp;

The rest of this document shows the steps that a programmer can follow to prepare a local copy of the OpenDSS source for implementation of the custom class. The details of the implementation (or functionality) of the custom class are left to the programmer.

&nbsp;

***Preparation***

&nbsp;

If you have not already obtained the latest version of the source code, follow these steps:

&nbsp;

•Obtain a copy of the latest OpenDSS source code from sourceforge

\-Go to http://sourceforge.net/projects/electricdss/develop

Either:

\-Browse code and download a GNU tarball of the source code

\-Preform a check-out of the source coude using a sudversion client such as [TortoiseSVN](<https://tortoisesvn.net/>). Point the client to:&nbsp;

&nbsp;

http://electricdss.svn.sourceforge.net/svnroot/electricdss

&nbsp;

•There will be a folder called MyOpenDSS. Navigate to one level above this subdirectory

\-The MyOpenDSS folder is typically at ..\\opendss\\Source\\MyOpenDSS

&nbsp;

&nbsp;

***Making Your Own OpenDSS***

&nbsp;

•Create a new directory, with a name of your choosing, preferably at the same subdirectory level as MyOpenDSS

•Copy the contents of the MyOpenDSS directory into to the new directory you created

•Open the MyOpenDSS project with Delphi from the new directory and save it under your own project name (e.g., MyCustomOpenDSS.dproj)

\-The same can be done for the MyOpenDSSEngine project if you wish to build the .dll in addition to the executable

•Delete all the files in your new directory that begin with "MyOpenDSS"

\-(Note: don't delete the MyDSSClassDefs.pas file or the ImplGlobals.pas file. The latter is a stub for the event sinks used in the COM Server, but not in the EXE version)

•Add the custom class code (.pas file) to the project.

\-This will be a FileNewUnit command in Delphi.

\-You may want to save the new unit in the same directory as your new project file, although you can place it anywhere you find convenient.

\-Once you save the file, the unit will be named the same.

\-This file can be empty at this point. Generally, you will want to start with an existing DSS class file that is similar to what you want to do and edit it.

•Add the class instantiation code to MyDSSClassDefs.pas

\-This involves defining a unique identifier for the new class in the INTERFACE section of the unit.

\-In the IMPLEMENTATION section of the unit, add your custom class name to the USES subsection.

•In your custom class file, add references in the Uses clause in the Implementation to any core OpenDSS classes that you would like to use, or refer to (e.g., the Circuit class)

&nbsp;

These are the steps to adding in a custom class to your own copy of the OpenDSS source code. The steps are written with Embarcadero's Delphi in mind as the IDE, but can be duplicated with a compatible Pascal compiler and IDE (if any). However, you may have to do more tasks manually.

&nbsp;

The details of your class implementation are left to your imagination and coding ability\!

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of HelpNDoc for CHM Help File Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
