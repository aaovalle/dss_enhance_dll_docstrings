# Getting Started

&nbsp;

***COM Automation***

&nbsp;

The COM Server in OpenDSSEngine.DLL may be automated.&nbsp; The installer will register either or both versions, depending on your selection.&nbsp; Even though the file names and registration commands match, they are in separate locations and Windows will activate the correct version required by the calling program.&nbsp; For example, 64-bit MATLAB will call the 64-bit OpenDSSEngine.DLL and 32-bit Microsoft Excel will call the 32-bit version. &nbsp;

(Note: In corporate IT implementations of Microsoft Office, it is common for only the 32-bit version to be installed.)

Files

&nbsp;

The OpenDSS Installer will automatically register the COM servers during the installation process. However, you can still do it manually if you prefer. Although it has gotten a little more complicated, installation of the OpenDSS program is still one of the easiest you will encounter in programs today: Simply copy the program files to a folder of your choosing (such as C:\\OpenDSS or C:\\Users\\MyUserName\\OpenDSS) and start the program.

&nbsp;

The following are the key program files:

&nbsp;

1. OpenDSS.exe&nbsp; &nbsp; (Stand alone executable)
1. OpenDSSEngine.DLL&nbsp; &nbsp; (The in-process COM server version)
1. KLUSolve.DLL&nbsp; &nbsp; (Sparse matrix solver)
1. DSSView.exe&nbsp; &nbsp; (Viewer for DSS graphics output)
1. OpenDSSDirect.DLL&nbsp; &nbsp; (Direct call DLL – alternative to the COM interface)

&nbsp;

The **OpenDSSDirect.DLL** file is a relatively new option for driving OpenDSS without using the COM interface.&nbsp; It is a stdcall DLL that mimics the COM interface in many aspects but has special functions as well. You can use this to basically build OpenDSS into your application or use OpenDSS to do parallel processing on systems with this capability (such as with the Julia language, for example, which does not support COM). For documentation, see **OpenDSS\_Direct\_DLL.pdf** in the ..\\Doc directory where OpenDSS was installed.

The **OpenDSSEngine.DLL** is an *in-process* COM server that will have to be registered if you intend to access it from other programs/languages such as MATLAB and VBA in MS Office. This will occur automatically if you use the installer from the download.&nbsp;

Manual Registration of COM Server

&nbsp;

If you do not intend to automate OpenDSS, and simply use the OpenDSS.EXE stand-alone version, you could skip this step and simply copy the EXE and DLL files to some convenient location on your disk. Afterward, you can manually register the server by issuing the following command to the (DOS) command prompt when in the folder you have placed the files:

Regsvr32&nbsp; OpenDSSEngine.DLL

&nbsp;

The **RegisterDSSEngine.BAT** file provided within the standard zip file download to perform this action. Registration need only be done once.&nbsp; You may simply double-click on the .BAT file and it will execute the registration.&nbsp;

**Note**: You may need Administrator privileges on your computer to do this. This applies more to Windows 10, 8, 7 and Vista than previous versions of Windows.&nbsp;

On Windows Vista, 7, 8, and 10 you will have to execute the .BAT file from an elevated Admin status.&nbsp; One way to do this is right click on the Windows buttonand select **Command Prompt (Admin)**.&nbsp; Then run the .BAT file from the command window, or DOS window. Some corporate IT policies may require you to go through additional steps. It may be necessary to have an administrator install the intial copy of OpenDSS.&nbsp; Once installed, you can simply update by copying the newer EXE or DLL over the older one in most cases.

After registration, if you start the Windows registry editor (Type ‘regedit’ in the command box on the start menu) you will find the OpenDSSEngine listed under Classes as shown in [Figure 2](<OpenDSSDocumentation.md#\_Ref244918339>). If you then look up the GUID in the registry, it should point to the OpenDSSEngine.DLL file in the folder where you installed it ([Figure 3](<OpenDSSDocumentation.md#\_Ref244918407>)).

The OpenDSSEngine will show up as “OpenDSS Engine” or “OpenDSSEngine.DSS” in the list of available object references in most development environments. For example, to instantiate an OpenDSSEngine object in MATLAB, you would issue the following statement:

&nbsp;

&nbsp; &nbsp; %instantiate the DSS Object

&nbsp; &nbsp; Obj = actxserver('OpenDSSEngine.DSS');

&nbsp;

When both the 32-bit and 64-bit versions are available, Windows will automagically load the appropriate one for your application.


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Review with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
