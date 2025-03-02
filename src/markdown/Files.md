# Files

&nbsp;

The OpenDSS Installer will automatically register the COM servers during the installation process. However, you can still do it manually if you prefer, following [these](<Troubleshooting.md>) steps . Although it has gotten a little more complicated, installation of the OpenDSS program is still one of the easiest you will encounter in programs today: Simply copy the program files to a folder of your choosing (such as C:\\OpenDSS or C:\\Users\\MyUserName\\OpenDSS) and start the program.

&nbsp;

The following are the key program files:

&nbsp;

&#49;. OpenDSS.exe (Stand alone executable)

&#50;. OpenDSSEngine.DLL (The in-process COM server version)

&#51;. KLUSolve.DLL (Sparse matrix solver)

&#52;. DSSView.exe (Viewer for DSS graphics output)

&#53;. OpenDSSDirect.DLL (Direct call DLL – alternative to the COM interface)

![Image](<lib/NewItem27.png>)

&nbsp;

The **OpenDSSDirect.DLL** file is a relatively new option for driving OpenDSS without using the COM interface. It is a stdcall DLL that mimics the COM interface in many aspects but has special functions as well. You can use this to basically build OpenDSS into your application or use OpenDSS to do parallel processing on systems with this capability (such as with the Julia language, for example, which does not support COM). For documentation, see OpenDSS[ Direct DLL](<OpenDSSSharedlibrary-DirectDLL1.md>) section of this manual. The **OpenDSSDirect.h** file corresponds to the header file for the DLL

&nbsp;

The **OpenDSSEngine.DLL** is an in-process COM server that will have to be registered if you intend to access it from other programs/languages such as MATLAB and VBA in MS Office. This will occur automatically if you use the installer from the download.

&nbsp;

The **KLUSolve.DLL** corresponds to the solver implemented by OpenDSS

&nbsp;

The **OpenDSS.EXE** corresponds to the standalone EXE file of OpenDSS

&nbsp;

The **DSSView.EXE** corresponds to the plotting utility (see the following section -[*Other Files*](<OtherFiles.md>)- of this help file)

&nbsp;

**ComPorts.ini** is a file containing the TCP communication ports that OpenDSS can use to communicate to other apps such as the progress indicator, OpenDSS-GIS among others. USe it to adjust the TCP port use when coordination with your local firewall or antivirus program require.

&nbsp;

**DSSProgress.exe** is an executable implementing the progress bar for OpenDSS simulations, this application allows users to visualize the simulation progress even when using multiple actors. If not present in the installation folder will NOT trigger any issues.

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Don't Let Unauthorized Users View Your PDFs: Learn How to Set Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
