# BusLevels

&nbsp;

(read only)

&nbsp;

This property gets the bus levels for all the buses in the model. The bus levels are calculated after calculating the incidence branch-to-node (B2N) matrix and they represent the distance from the buses to a reference that goes from the feeder head to the farthest bus in the model. The bus level index matches with the bus list obtained with the circuit interface.

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

% calculates the B2N matrix

DSSText.Command = 'CalcIncMatrix\_O';

% get the bus levels

myBLevels = DSSSolution.BusLevels;

myBusNames = DSSCircuit.AllBusNames;

% creates a table with the data

myBLTable = \[\];

for i = 1:size(myBusNames),

&nbsp; &nbsp; myBLTable = \[myBLTable; \[myBusNames(i,1),num2str(myBLevels(1,i))\]\];

end;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Full-featured Documentation generator](<https://www.helpndoc.com>)_
