# StartPDElement

&nbsp;

(read/write)

&nbsp;

This property sets/gets the full name of the first PDelement for the BranchRemove command (class.name -\> e.g. Line.myLine).

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

DSSReduceCkt = DSSCircuit.ReduceCkt;

DSSLines = DSSCircuit.Lines;

% activates the first line on the list

i = DSSLines.First;

myLine = DSSLines.Name

&nbsp;

% set the PDE name for the reduction

DSSReduceCkt.StartPDElement = myLine;

% breaks loops first

DSSReduceCkt.DoLoopBreak();

% merge parallel lines

DSSReduceCkt.DoParallelLines();

% reduce&nbsp;

DSSReduceCkt.DoDefault();

&nbsp;

% get the OpenDSS command

myStr = DSSReduceCkt.EditString;

***
_Created with the Standard Edition of HelpNDoc: [Protect Your Confidential PDFs with These Simple Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
