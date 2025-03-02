# Next

&nbsp;

(read only)

&nbsp;

This property sets the next energy Meter active.&nbsp; Returns 0 if no more.

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

DSSMeters = DSSCircuit.Meters;

% activates the first EM on the list

i = DSSMeters.First;

% Enumerates EMs by name

myNames = \[\];

while&nbsp; i \> 0,

&nbsp; &nbsp; myNames = \[myNames, DSSMeters.Name\];

i = DSSMeters.Next;

end;

***
_Created with the Standard Edition of HelpNDoc: [Free help authoring environment](<https://www.helpndoc.com/help-authoring-tool>)_
