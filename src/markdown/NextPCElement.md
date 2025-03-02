# NextPCElement

&nbsp;

(read only)

&nbsp;

This property gets the next Power Conversion (PC) element to be the active element.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

DSSElement = DSSCircuit.ActiveCktElement;

% Sets the first PCE on the list as the active element

i = DSSCircuit.FirstPCElement;

myList = \[\];

% Creates a list with all the PCE names

while i \> 0,

&nbsp; &nbsp; myList = \[myList;{DSSElement.Name}\];

&nbsp; &nbsp; i = DSSCircuit.NextPCElement;

end;


***
_Created with the Standard Edition of HelpNDoc: [News and information about help authoring tools and software](<https://www.helpauthoringsoftware.com>)_
