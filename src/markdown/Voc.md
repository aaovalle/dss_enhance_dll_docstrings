# Voc

&nbsp;

(read only)

&nbsp;

This property returns a Complex Array of doubles containing the Open circuit voltage at the active bus.

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

DSSActiveBus = DSSCircuit.ActiveBus;

% Sets bus "myBus" as the active Bus

DSSCircuit.SetActiveBus('myBus')

myVolt = DSSActiveBus.Voc;

mySize = size(myVolt);

myVMagAng = \[\];

% Converts from complex to polar

for i = 1:2:(mySize(2) - 1),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVMagAng = \[myVMagAng;\[abs(myVolt(i) + j\*myVolt(i + 1)),angle(myVolt(i) + j\*myVolt(i + 1))\*180/pi\]\];

end;

***
_Created with the Standard Edition of HelpNDoc: [Easily create CHM Help documents](<https://www.helpndoc.com/feature-tour>)_
