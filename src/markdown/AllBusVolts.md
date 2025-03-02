# AllBusVolts

&nbsp;

(read only)

&nbsp;

This property returns a complex array of all bus, node voltages from most recent solution.

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

% Gets the voltages for all the nodes in the model

myNodes = DSSCircuit.AllNodeNames;

myVolt = DSSCircuit.AllBusVolts;

mySize = size(myVolt);

myVMagAng = \[\];

% Translates the complex values into polar pairs (magnitude, angle)

for i = 1:2:(mySize(2) - 1),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVMagAng = \[myVMagAng;\[abs(myVolt(i) + j\*myVolt(i + 1)),angle(myVolt(i) + j\*myVolt(i + 1))\*180/pi\]\];

end;

% Links the node names to the polar values

myVoltMat = \[\];

for i = 1:size(myNodes),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVoltMat = \[myVoltMat;\[myNodes(i),num2str(myVMagAng(i,1)),num2str(myVMagAng(i,2))\]\];

end;


***
_Created with the Standard Edition of HelpNDoc: [Easily Add Encryption and Password Protection to Your PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
