# IncMatrixCols

&nbsp;

(read only)

&nbsp;

This property returns the an array of strings with the name of the columns of the B2N matrix.

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

DSSSolution = DSSCircuit.Solution;

&nbsp;

% Solve the model

DSSSolution.Solve();&nbsp;

% calculate the B2N matrix, requires an Energy meter at the feeder head

DSSText.Command = 'CalcIncMatrix\_O';

% gets the B2N matrix as vector

myB2NV = DSSSolution.IncMatrix;

mySize = size(myB2NV);

% gets the number of rows

myB2N = \[\]

for i = 1:3:(mySize(2) - 1),

&nbsp; &nbsp; myB2N = \[myB2N;myB2NV(i:i+2)\];

end;

% gets the column names of the B2N matrix

myB2NColN = DSSSolution.IncMatrixCols;

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
