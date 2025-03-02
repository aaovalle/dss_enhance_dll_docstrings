# Laplacian

&nbsp;

(read only)

&nbsp;

This property returns the Laplacian matrix calculated in OpenDSS based on the latest B2N matrix. The vector represents a sparse matrix (non-zero values are the only ones delivered) and can be interpreted as follows: The first element is the row number, the second one is the column and the third is the value, this way, by dividing the number of elements in the array by 3 the user can obtain the number of rows in case of wanting to sort the vector values within a matrix. The tables for the columns and rows are the same as the columns for the B2N columns (square matrix).

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

% calculate the Laplacian matrix

DSSText.Command = 'CalcLaplacian';

% gets the B2N matrix as vector

myLapV = DSSSolution.Laplacian;

mySize = size(myLapV);

% gets the number of rows

myLaplacian = \[\]

for i = 1:3:(mySize(2) - 1),

&nbsp; &nbsp; myLaplacian = \[myLaplacian;myLapV(i:i+2)\];

end;

% gets the col/row labels for the Laplacian matrix

myLapNames = DSSSolution.IncMatrixCols;


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
