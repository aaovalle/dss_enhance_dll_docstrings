# First

&nbsp;

(read only)

&nbsp;

Invoking this property sets the first line element active.&nbsp; Returns 0 if no lines.&nbsp; Otherwise, index of the line element.

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

***
_Created with the Standard Edition of HelpNDoc: [Free EPub producer](<https://www.helpndoc.com/create-epub-ebooks>)_
