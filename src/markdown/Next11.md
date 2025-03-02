# Next

&nbsp;

(read only)

&nbsp;

This property advances to the next PD element in the circuit. Enabled elements only (enabled = true/yes). Returns 0 when no more elements.

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

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

% Handler for PDelements interface

DSSPDE = DSSObject.PDElements;

% Activates the first PDE on the list

i = DSSPDE.First;

% Enumerates PDE by name

myNames = \[\];

while&nbsp; i \> 0,

&nbsp; &nbsp; myNames = \[myNames, DSSPDE.Name\];

i = DSSPDE.Next;

end;

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your CHM Help File Capabilities with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
