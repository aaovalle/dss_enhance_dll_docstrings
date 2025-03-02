# Parent

&nbsp;

(read only)

&nbsp;

This property sets Parent of the active Line to be the active line. Returns 0 if no parent or action fails..

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

DSSLines.First;

myName = DSSLines.Name;

% sets Parent of the active Line to be the active line

i = DSSLines.Parent;

if i == 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp(\['No parent upstream Line ',myName\]);

end;

***
_Created with the Standard Edition of HelpNDoc: [Keep Your PDFs Safe from Unauthorized Access with These Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
