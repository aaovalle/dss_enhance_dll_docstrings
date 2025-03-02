# Compile using MSVS (Windows)

&nbsp;

For compiling OpenDSS-C make sure you have the following add-ons installed in your MS VIsual Studio /Code:

&nbsp;

![Image](<lib/NewItem 47.png>)

Figure 1

Add-ons required for compiling OpenDSS-C using MSVS (windows)

&nbsp;

Once ready, open MSVS and select the option *Open a local folder* as indicated in Figure 2.

&nbsp;

![Image](<lib/NewItem 48.png>)

Figure 2

Opening a local folder in MSVS

&nbsp;

A new browsing window will open for the user to select the project’s folder. Please redirect that window to the folder where the OpenDSS-C clone was created (See [cloning the OpenDSS repo](<https://sourceforge.net/p/electricdss/discussion/861976/thread/5b864841/?limit=25#8aa2> "target=\"\_blank\"")). Once you are within that folder select the option “Select folder” as shown in [Figure 3](<OpenDSSDocumentation.md#\_Ref112075475>).

&nbsp;

![Image](<lib/NewItem 49.png>)

Figure 3

Opening the project

&nbsp;

With that, Visual Studio will setup the environment using the CMake files within that folder. The environment should look as shown in [Figure 4](<OpenDSSDocumentation.md#\_Ref112075527>).

&nbsp;

![Image](<lib/NewItem 50.png>)

Figure 4

MSVS environment ready for compilation

&nbsp;

OpenDSS-C can be compiled in 2 forms, DLL/so or command line executable. For telling the compiler the type of output the user is interested in, open the file CMakeLists.txt at the root of the directory as shown in Figure 5.

&nbsp;

![Image](<lib/NewItem 52.png>)

Figure 5

Selecting the output type

&nbsp;

The CMakeLists.txt file is marked with a red arrow in Figure 5. In Figure 5 the CMakeLists.txt file is open, pay special attention to line 21 where the statement *set(MyOutputType "DLL")* is (blue arrow - Figure 5). This statement tells the compiler the output type for the compilation. If the user wants to generate a command line executable modify this statement as follows:

&nbsp;

&nbsp;*set(MyOutputType "EXE")*

&nbsp;

Otherwise, if the user wants to generate a DLL/so use the following statement:

&nbsp;

&nbsp;*set(MyOutputType "DLL")*

&nbsp;

No matter the operating system, the statement DLL indicates that the output will be a shared library and CMake will do the rest. After defining the output type, open the file called CMakePresets.json to define if the compilation is for release or debugging purposes. The content of this file is shown in Figure 6.

&nbsp;

![Image](<lib/NewItem 53.png>)

Figure 6

Declaring the compilation purpose

&nbsp;

The CMakePresets.json file is marked with a red arrow at Figure 6. In this file, look at line 11 (orange arrow) for defining the output purpose, if is Release use the following declaration:

&nbsp;

*"CMAKE\_BUILD\_TYPE": "Release"*

&nbsp;

Otherwise, use the following declaration for debugging:

&nbsp;

*"CMAKE\_BUILD\_TYPE": "Debug"*

&nbsp;

Users can also alter the text in line 15 (blue arrow) to reflect the type of compilation used for the project. This will be shown at the menu bar of MSVS. Depending on the compilation type users need to define the startup item for the compilation. For instance, when compiling a stand alone executable go to the folder CMD within the project folder after configuring the environment. In this folder, right click on the file called OpenDSSC.cpp and select the option *Set as Startup item* as shown in Figure 7.

&nbsp;

![Image](<lib/NewItem 63.png>)

Figure 7

Setting up the startup item for building a stand-alone executable

&nbsp;

Otherwise, if building a DLL go to the folder DLL within the project's folder and right click on the file called OpenDSSCDLL.cpp, then select the option *Set as Startup item* as shown in Figure 8.

&nbsp;

![Image](<lib/NewItem 64.png>)

Figure 8

Setting up the startup item for building a shared library executable

&nbsp;

&nbsp;

With these modifications the next step will be to compile. For this, use the menu option *Build -\> Build all* and the compilation process will start as shown in Figure 9.

&nbsp;

![Image](<lib/NewItem 55.png>)

Figure 9

Building the solution

&nbsp;

Once done, the compiled files can be found within the folder *out* located at the project's folder. There the user will find the executable and/orDLLs generated. The DLL follows the same interfaces as the standard DLL generated in Delphi. See the [DLL documentation](<OpenDSSSharedlibrary-DirectDLL1.md>).

***
_Created with the Standard Edition of HelpNDoc: [Easily convert your WinHelp HLP help files to CHM with HelpNDoc's step-by-step guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
