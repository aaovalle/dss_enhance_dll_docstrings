# Next

&nbsp;

(read only)

&nbsp;

This property Iterate to the next recloser in the circuit. Returns zero if no more.

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

DSSReclosers = DSSCircuit.Reclosers;

% Activates the first recloser on the list

i = DSSReclosers.First;

% Enumerates reclosers by name

myNames = \[\];

while&nbsp; i \> 0,

&nbsp; &nbsp; myNames = \[myNames, DSSReclosers.Name\];

i = DSSReclosers.Next;

end;


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
