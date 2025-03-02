# IncMatrix

&nbsp;

(read only)

&nbsp;

This property returns the incidence branch-to-node (B2N) matrix calculated for the model as a vector of integers. The vector represents a sparse matrix (non-zero values are the only ones delivered) and can be interpreted as follows: The first element is the row number, the second one is the column and the third is the value, this way, by dividing the number of elements in the array by 3 the user can obtain the number of rows in case of wanting to sort the vector values within a matrix.

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


***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of HelpNDoc for CHM Help File Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
