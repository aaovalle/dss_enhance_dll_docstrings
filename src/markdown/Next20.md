# Next

&nbsp;

(read only)

&nbsp;

This property sets the next VSOURCE object to be active; returns zero if no more.

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

DSSVSources = DSSCircuit.VSources;

% Activates the first VSource on the list

i = DSSVSources.First;

% Enumerates VSources by name

myNames = \[\];

while&nbsp; i \> 0,

&nbsp; &nbsp; myNames = \[myNames, DSSVSources.Name\];

i = DSSVSources.Next;

end;

***
_Created with the Standard Edition of HelpNDoc: [Make Your PDFs More Secure with Encryption and Password Protection](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
