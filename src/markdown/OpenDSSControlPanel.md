# OpenDSS Control Panel

&nbsp;

There is a "Control Panel" with tabbed windows for constructing and testing scripts and executing them. The main access to scripts and results is generally through script files and output files or the [COM interface](<COMInterface.md>). However, you may put large scripts into a window on the Control Panel if you wish.

&nbsp;

Communication to the DSS is fundamentally accomplished through text strings passed to the OpenDSS command processor. However, if you are driving the program through the in-process COM or the [DirectDLL](<OpenDSSSharedlibrary-DirectDLL1.md>) library from another program, there are many functions provided in the to directly execute common commands (like "solve") and set properties of circuit elements without going through the command language. That might be a little faster for some operations that are executed repeatedly, although the OpenDSS command processor’s text parsing is often more than fast enough for most applications.

&nbsp;

Simulation results can be returned as arrays of values in the [COM interface](<COMInterface.md>) or in text through CSV files. A few standard text file reports are provided by the base OpenDSS software component (see Show and Export commands). The intent for users demanding more sophisticated reports is for users to design them through Excel worksheets, MATLAB plot, Python Plots or whatever application is being used to control the OpenDSS in special ways.

&nbsp;

The OpenDSS control panel automatically appears in the EXE version. The panel may also be invoked from the OpenDSS [COM interface](<COMInterface.md>) using the Panel or Show Panel commands or the ShowPanel method in the [COM interface](<COMInterface.md>).

&nbsp;

(***Caveat**: When invoked from a MS Excel application, Excel may trap some of the keystrokes, so it doesn't always work as smoothly as it does in the standalone EXE application. This may happen in other programs as well but seems to work OK in user-written software that is not trapping keystrokes.*)

&nbsp;

The control panel (Figure 1) is a typical Windows tabbed control. In Figure 3, the tabs are along the bottom of the main window. The user may execute a script, or a portion of a script, in any of the open window tabs at any time. This allows the user to organize scripts in a logical manner and have them available at any time. All scripts operate on the presently active circuit, or they may define a new circuit that becomes active.

&nbsp;

![Image](<lib/NewItem11.png>)

Figure 1.Example of the Control panel window for the DSS&nbsp;

&nbsp;

Scripts or script fragments are executed by selecting the script lines to be executed. The user can right-click on the selection and then click on the **Do Selected** option, which has a short-cut key (**ctrl-d**). The selection may also be executed from the Do menu or the speed button directly below the Do menu item (Figure 2).&nbsp;

&nbsp;

Of course, the script in the windows can redirect the OpenDSS command input to a file, which can, in turn, redirect to another file. Thus, scripts can be quite voluminous without having to appear in a window on the control panel.&nbsp;

&nbsp;

![Image](<lib/NewItem12.png>)

Figure 2.“Do command” and speed buttons.

&nbsp;

Each script window on the Control panel implements a Windows RichEdit text form. Thus, it has many of the standard text editing features one might expect. However, third party text editors (such as Editplus or Notepad++) can provide substantially more capability. It is recommended that one of the first commands to issue after starting the DSS for the first time is

&nbsp;

Set Editor= *filename*

&nbsp;

Where filename is the full path name of the text editor you wish to use. This should be a plain text editor. Currently, the program accepts only plain ANSI text from files. The RichEdit windows are actually Unicode but are converted to ANSI when they are saved.Editors such as Word or Wordpad may add text that is not properly interpreted by OpenDSS. You may reformat the text in a window while the program is running, but these formatting commands are not saved to the DSS file. Many modern editors can save in a variety of text formats. Set options for ANSI text when saving DSS files for OpenDSS.

&nbsp;

It is generally necessary to issue the Set Editor command only one time. The program will remember this value in the Windows Registry after the program shuts down. Likewise, the default base frequency (50 or 60 Hz) is set one time. The assumed default base frequency is displayed at the top of the main screen. If you work on both types of systems (as we do), always make sure it is set to the correct value\! Some users always insert the command to set the default base frequency immediately after the Clear command in the Master file.

&nbsp;

When a user right-clicks on a file name in one of the script windows, the popup menu gives the user the option of “Open” or “Edit” for the selected file (Figure 3). “Open” will open the selected file in another script window in the DSS program. “Edit” will open the selected file in the Editor of the user’s choosing. If no Editor was specified, the program will attempt to open the Notepad editor supplied with Windows.&nbsp;

&nbsp;

If the file name contains no blanks, one need only click anywhere within the file name to execute the Open or Edit commands.

&nbsp;

![Image](<lib/NewItem13.png>)

Figure 3. Compiling a File containing a circuit description script from a script window in the control panel.

&nbsp;

&nbsp;

You may change the font for a window by clicking the “Font…” button. The size of the font most recently used is remembered by the program. Font information is not kept with the script files: these are simple plain text files.

***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Simplicity of HelpNDoc's User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
