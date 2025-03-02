# Compile using CMD (Linux)

&nbsp;

&nbsp;

For compiling OpenDSS-C in Linux make sure you have the following add-ons installed:

&nbsp;

![Image](<lib/NewItem 66.png>)

Figure 1

Add-ons required for compiling OpenDSS-C in Linux

&nbsp;

For installing the add-ons required execute the following commands:

&nbsp;

1. &nbsp;
   1. *sudo apt-get install cmake*

&nbsp;

1. &nbsp;
   2. *sudo apt-get install uuid-dev*

&nbsp;

1. &nbsp;
   3. *sudo apt-get install build-essential*

&nbsp;

After installed in your local environment, you are ready to compile the project. This is probably the simplest way to compile the project, however, a couple of requisites must be fulfilled.&nbsp;

&nbsp;

1. &nbsp;
   1. Step out the projects folder to compile from the outside.

&nbsp;

1. &nbsp;
   2. Create a Build folder. This is where the DLL/so/EXE will be stored.

&nbsp;

1. &nbsp;
   3. Set the target, for that enter the following commands (assume that the folder where the source code of OpenDSS is located at the folder OpenDSSC:

&nbsp;

*cmake -DCMAKE\_BUILD\_TYPE=Release -DMyOutputType:STRING=EXE ../OpenDSSC*

&nbsp;

1. &nbsp;
   4. Compile using the following command

&nbsp;

*cmake --build . -j 12*

&nbsp;

As can be seen in step 3, the type of output (EXE/DLL) is specified in the argument -DMyOutputType. If the user wants to generate a command line executable use the value EXE, otherwise, use DLL (no matter the operating system). The build type or compilation purpose must be specified at the argument *-DCMAKE\_BUILD\_TYPE*. At the example presented on step 3 the compilation is for a release version. Otherwise, the user can use Debug if required.

&nbsp;

The C++ version in Linux uses a default in-console editor for displaying reports (like when using the command "Show"). If you are interested in using a text editor, OpenDSS offers compatibility with gedit. For that, users will have to install gedit in their Linux distribution.

&nbsp;

*sudo apt-get install gedit*


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with HelpNDoc's CHM Help File Creation Features](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
