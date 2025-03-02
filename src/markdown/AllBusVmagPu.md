# AllBusVmagPu

&nbsp;

(read only)

&nbsp;

This property returns a double Array of all bus voltages (each node) magnitudes in Per unit.

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

% Gets the voltages (pu) for all the buses in the model

myNodes = DSSCircuit.AllNodeNames;

myVolt = DSSCircuit.AllBusVmagPu;

mySize = size(myVolt);

myVmat = \[\];

% Creates a matrix of strings with the node name and V (mag)

for i = 1:mySize(2),

myVmat = \[myVmat;\[myNodes(i), num2str(myVolt(1,i))\]\];

end;

***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of a Help Authoring Tool](<https://www.helpndoc.com>)_
