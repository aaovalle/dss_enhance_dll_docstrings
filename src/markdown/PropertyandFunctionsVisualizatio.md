# Property and Functions Visualization by COM: VBA, Python, and MATLAB

&nbsp;

**Property and Functions Visualization by COM: VBA, Python, and MATLAB**

&nbsp;

This Tech Note introduces the quite often hidden interfaces available in Python, MATLAB, and Excel-VBA to visualize the list of properties and functions of OpenDSS when connected by COM interface. This document is an integration of “OpenDSSComDoc” TechNote and requires the user to be familiar with the basic concepts on the COM interface introduced in the “User Manual” and the “Primer”1.

&nbsp;

The number of properties and functions available by COM interface is so large that is practically impossible to know all of them. Sometimes might be hard to remember the exact name of a property or function (e.g., DSSCircuit.Line.Length or DSSCircuit.Lines.Length?) while other times a user might need to know what properties are available for a specific class even before start coding in (e.g., what properties are available for a Line object?). This Tech Note addresses such problem by explaining how to use the interfaces available in VBA, Python, and MATLAB. Such interfaces might significantly speed up the use and familiarization process with the COM interface, especially for new users. It is worth noticing that, in some software, not all the properties and functions are listed (although most of them are). In doubt the OpenDSSComDoc Tech Note can be used.

&nbsp;

**VBA INTERFACE**

&nbsp;

EXCEL-VBA provides, among the three software here analyzed, the most complete and friendly interface to the OpenDSS object and functions. Indeed, it is not uncommon for users working in MATLAB or Python to use Excel-VBA only as an “OpenDSS dictionary” to have, on a side, all names of property and functions (indeed the name of property and functions are not dependent by the command that is driven OpenDSS). The list of OpenDSS properties and functions can be accessed by following the steps discussed below:

&nbsp;

&#49;) Register the COM interface (Optional): Since version 7.6 OpenDSS is able to automatically register the COM interface for both 32 and 64 bit version2, hence, no user action is usually required. However, if for any reason the COM interface has not been successfully registered, the following steps can be followed:

&nbsp;

a. Go to “Start” in Windows

b. Go to the folder “Accessories”

c. Right Click on “Command Prompt”

d. Click on “Run as administrator” (Figure 1, left)

e. Tape in it “regsvr32 OpenDSSPath\\x64\\OpenDSSEngine.DLL” (Figure 1, right)

f. Press Enter (a confirmation window should appear, Figure 1, right)

g. Tape in it “regsvr32 OpenDSSPath\\x86\\OpenDSSEngine.DLL” (Figure 1, right)

h. Press Enter (a confirmation window should appear, Figure 1, right)

&nbsp;

&#50;) Add OpenDSS library: In this way EXCEL will load all the command to call OpenDSS. The following steps can be adopted:

&nbsp;

a. Open an EXCEL file

b. Press Alt+F11 on the keyboard to open the VBA project window

c. Go on “Tools-References” and tick the “OpenDSS Engine” as shown in Figure 2

&nbsp;

&nbsp;

![Image](<lib/NewItem227.png>)\
Figure 1 Step 1: Register the COM interface (optional after OpenDSS version 7.6)

&nbsp;

![Image](<lib/NewItem228.png>)

Figure 2 Step 2: Add OpenDSS library

&nbsp;

&#51;) Access to the VBA interface: All the classes, properties and functions can be accessed by:

&nbsp;

a. Going to “View” and “Object Browser”

b. On the new opened window, at the place of \<All Libraries\> choose “OpenDSSengine” as shown in Figure 3-a.

&nbsp;

In the “Classes” and “Members” sub-windows the OpenDSS classes and corresponding properties and functions can be respectively found as shown in Figure 3-a and Figure 3-b. Moreover, also a brief explanation on the selected property is shown in the lower window (Figure 3-a).

&nbsp;

Example: To understand how to use this interface, let’s suppose that the length of the first line need to be saved as a variable called “LineLength”. For this purpose, it is first necessary to find the “Lines” class in the class sub-window (left side in Figure 3-a). Then, by looking through all its property in the “Members of Lines” sub-window (right side in Figure 3-b) find the needed property (“First” and “Length” in this case). Consequently, after the OpenDSS COM interface has been instantiated by adopting the code for instance shown in Table 1 (and discussed in more detail in the “Primer”) the line interface can be created with the following command:

&nbsp;

Dim DSSLines As OpenDSSengine.Lines

&nbsp;

Then adopting the same spelling shown by VBA (Figure 3-b) the properties first and length are used:

&nbsp;

DSSLines.First&nbsp;

LinesInterface.First

LineLength =LinesInterface.Length

&nbsp;

The same identical process can be repeated for any other property of any OpenDSS class that can be explored. It is worth noticing that in VBA (differently from MATLAB and Python) it is not necessary to write and run the initialization code shown in Table 1 to only see the names of the property and functions.

&nbsp;

![Image](<lib/NewItem229.png>)

Figure 3 a) Step 3: Access to the VBA interface b) List of properties for the Lines class (“First” and “Length” highlighted)

&nbsp;

| Table 1 Instantiated COM interface in VBA |
| --- |
| ' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*&nbsp; ' \* Initialize OpenDSS&nbsp; ' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*&nbsp; ' Declare the OpenDSS related variables&nbsp; Dim DSSObj As OpenDSSengine.DSS&nbsp; Dim DSSText As OpenDSSengine.Text&nbsp; Dim DSSCircuit As OpenDSSengine.Circuit&nbsp; Dim DSSSolution As OpenDSSengine.Solution &nbsp; ' Instantiate the OpenDSS Object&nbsp; DSSObj = New OpenDSSengine.DSS &nbsp; ' Start up the Solver&nbsp; If Not DSSObj.Start(0) Then MsgBox("Unable to start the OpenDSS Engine")&nbsp; Return&nbsp; End If&nbsp; ' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*&nbsp; ' \* Define Circuit – Solve Power Flow&nbsp; ' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*&nbsp; Etc… &nbsp; ' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*&nbsp; ' \* Create the Line Interface&nbsp; ' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*&nbsp; Dim Length as double&nbsp; Dim DSSLines As OpenDSSengine.Lines |


&nbsp;

**PYTHON INTERFACE**

&nbsp;

To visualize the Python interface a compiler is needed. More precisely, in this TechNote the free version of PyCharm is adopted. It is worth noticing, that differently from the previous discussed EXCEL VBA interface, in Python it is needed to run the instantiation code for the OpenDSS COM. In other words, it is first necessary to write a code as reported for simplicity in Table 1Table 2.

&nbsp;

| Table 2 Instantiated COM interface in Python |
| --- |
| import win32com.client # ----------------------------------------------------------&nbsp; # Initialize OpenDSS&nbsp; # ----------------------------------------------------------&nbsp; try:&nbsp; # Instantiate the OpenDSS Object&nbsp; DSSObj=win32com.client.Dispatch("OpenDSSEngine.DSS")&nbsp; except:&nbsp; print "Unable to start the OpenDSS Engine"&nbsp; raise SystemExit &nbsp; # ----------------------------------------------------------&nbsp; # Create the Line Interface&nbsp; # ---------------------------------------------------------- &nbsp; # Instantiate some OpenDSS Classes by creating some interfaces&nbsp; DSSText=DSSObj.Text&nbsp; DSSCircuit=DSSObj.ActiveCircuit&nbsp; DSSLines=DSSCircuit.Lines |


&nbsp;

It is then possible to access to the list of properties by following the steps described below:

&nbsp;

&#49;. Insert a debug breakpoint at any point after the OpenDSS initialization (red dot in Figure 4-a)

&nbsp;

&#50;. Run the code in Debug mode (by pressing the ![Image](<lib/NewItem230.png>) button on the top of the screen, in red in Figure 4-a)

&nbsp;

&#51;. Once the code stopped open the “Evaluate Expression” window (by pressing the ![Image](<lib/NewItem231.png>) button, in red in Figure 4-b ). Tape the name of one of the interface created in the initialization (such as DSSLines) and press “Evaluate” button (in Figure 4-c)

&nbsp;

&#52;. On the “Result” area select the “\_prop\_map\_get” (shown in Figure 4-c)and all the properties corresponding to DSSLines (in this case) will be displayed (shown in Figure 4-d)

&nbsp;

It is worth noticing that the properties are divided in two categories. Those that can be read (displayed by “\_prop\_map\_get”) and those at which a value can be assigned (displayed by “\_prop\_map\_put”).

![Image](<lib/NewItem232.png>)

Figure 4 a) Step 1: Insert a debug breakpoint b) Step 2: Run in Debug Mode c) Step 3: Select “\_prop\_map\_get” \
d) Step 4: List of all the properties of the class Lines with “First” and “Length” highlighted

&nbsp;

Consequently, by the name of the properties visualized by the Python compiler in Figure 4-d it is possible to know the exact spelling (as well the whole list) of the commands necessary (for this example) to select the first line and extract the length as shown below:

&nbsp;

DSSLines.First

LineLength=DSSLines.Length

&nbsp;

**MATLAB INTERFACE**

&nbsp;

Similarly to Python, MATLAB3 provides an interface to see all the properties associated with a class object in OpenDSS. However, before writing any code it is necessary unlocking a feature of MATLAB (if not already activated) called “Tab Completion”. For this purpose, within the tab “home” (1 in Figure 5), it is necessary to access the “Preferences” section (2 in Figure 5). Then, in the sub-section “Keyboard” (3 in Figure 5) the options “Enable in Command Window” and “Enable in Editor/Debugger” can be activated (tick them as shown in 4. in Figure 5).

&nbsp;

![Image](<lib/NewItem233.png>)

Figure 5 Activation of the feature “Tap Completion” in MATLAB

&nbsp;

&nbsp;

Once the “Tab Completion” feature is activated it is then necessary to initialize the COM interface (as in Python) writing and running the code reported in Table 3.

&nbsp;

Once the interfaces have been created (i.e., the initialization code has been run and the interfaces so produced can be seen in the Workspace, 1 in Figure 6) in the “command window” it is necessary to insert the name of the class (whose properties list is needed to know) followed by a dot (“DSSLines.” in this example as shown in 2 in Figure 6). The dot at the end tells MATLAB that, associated to this class, there might be properties. Then, leveraging the “Tab Completion” functionality previously activated, it is sufficient to press the “Tab” button on the keyboard and all the corresponding properties are visualized as shown in 3 in Figure 6. Consequently, it is possible to know what commands are available and (for this example) necessary to select the first line and extract the length of it as shown below:

&nbsp;

DSSLines.First&nbsp;

LineLength=DSSLines.Length

&nbsp;

| Table 3 Instantiated COM interface in MATLAB |
| --- |
| % ---------------------------------------------------------- % Initialize OpenDSS&nbsp; % ----------------------------------------------------------&nbsp; % Instantiate the OpenDSS Object&nbsp; DSSobj = actxserver('OpenDSSEngine.DSS');&nbsp; % Start up the Solver&nbsp; if ~DSSobj.Start(0),&nbsp; disp('Unable to start the OpenDSS Engine')&nbsp; return&nbsp; end &nbsp; % ----------------------------------------------------------&nbsp; % Create the Line Interface&nbsp; % ---------------------------------------------------------- &nbsp; % Instantiate some OpenDSS Classes by creating some interfaces&nbsp; DSSText = DSSobj.Text;&nbsp; DSSCircuit = DSSobj.ActiveCircuit;&nbsp; DSSLines=DSSCircuit.Lines; |


&nbsp;

&nbsp;

&nbsp;

![Image](<lib/NewItem234.png>)

Figure 6 Visualization in MATLAB of the List of properties for the Lines class (with “First” and “Length” highlighted)

&nbsp;

&nbsp;

&nbsp;

&#49; Both documents are available in either the computer Doc folder in which OpenDSS is installed and in the SourceForger repository at [https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Doc/](<https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Doc/>)

&#50; Both versions are required as the COM server used is function of the calling program. Moreover, in a Windows PC it is not uncommon to have both 32 and 64 bit programs making the need to have 32 and 64 bit of OpenDSS installed as well

&#51; In this TechNote the version 2012b is adopted. However, similar commands should be present also in previous and next release of the software

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Free Qt Help documentation generator](<https://www.helpndoc.com>)_
