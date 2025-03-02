# puVmagAngle

&nbsp;

(read only)

&nbsp;

This property returns a Variant array of doubles containing voltage magnitude, angle pairs in per unit.

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

mypuVolt = DSSActiveBus.puVamgAngle;

mySize = size(mypuVolt);

myVMagAng = \[\];

% Sorts data into a matrix

for i = 1:2:(mySize(2) - 1),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVMagAng = \[myVMagAng;\[mypuVolt(i), mypuVolt(i + 1)\]\];

end;

***
_Created with the Standard Edition of HelpNDoc: [Make CHM Help File Creation a Breeze with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
