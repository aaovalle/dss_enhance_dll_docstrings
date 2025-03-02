# AllBusVmag

&nbsp;

(read only)

&nbsp;

This property returns an array of magnitudes (doubles) of voltages at all buses.

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

% Gets the voltages for all the buses in the model

myNodes = DSSCircuit.AllNodeNames;

myVolt = DSSCircuit.AllBusVmag;

mySize = size(myVolt);

myVmat = \[\];

% Creates a matrix of strings with the node name and V (mag)

for i = 1:mySize(2),

myVmat = \[myVmat;\[myNodes(i), num2str(myVolt(1,i))\]\];

end;


***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
