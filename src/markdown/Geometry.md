# Geometry

&nbsp;

(read/write)

&nbsp;

This property sets/gets the line geometry code of the active Line.

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

% Gets the line geometry/code assigned to all the lines in the model

myGeometries = \[\];

while&nbsp; i \> 0,

&nbsp; &nbsp; myCode = DSSLines.Geometry;

&nbsp; &nbsp; myPreFx = 'Geometry=';

if myCode == '',

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myCode = DSSLines.LineCode;

&nbsp; &nbsp; myPreFx = 'LineCode=';

end; &nbsp; &nbsp;

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myGeometries = \[myGeometries;\[myPreFx, myCode\]\];

i = DSSLines.Next;

end;


***
_Created with the Standard Edition of HelpNDoc: [Easily Add Encryption and Password Protection to Your PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
