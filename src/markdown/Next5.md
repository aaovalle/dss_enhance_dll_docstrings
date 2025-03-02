# Next

&nbsp;

(read only)

&nbsp;

Invoking this property advances to the next Line element active.&nbsp; Returns 0 if no more lines.&nbsp; Otherwise, index of the line element.

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

DSSLines = DSSCircuit.Lines;

% activates the first line on the list

i = DSSLines.First;

% Gets the line names using First/next commands

myNames = \[\];

while&nbsp; i \> 0,

&nbsp; &nbsp; myNames = \[myNames, DSSLines.Name\];

i = DSSLines.Next;

end;

***
_Created with the Standard Edition of HelpNDoc: [Easily create Web Help sites](<https://www.helpndoc.com/feature-tour>)_
