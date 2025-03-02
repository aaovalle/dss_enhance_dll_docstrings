# Isc

&nbsp;

(read only)

&nbsp;

This property returns the short circuit currents at the active bus. The values are returned as a complex Array.

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

myIsc = DSSActiveBus.Isc;

mySize = size(myIsc);

myIMagAng = \[\];

% Converts from complex to polar

for i = 1:2:(mySize(2) - 1),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myIMagAng = \[myIMagAng;\[abs(myIsc(i) + j\*myIsc(i + 1)),angle(myIsc(i) + j\*myIsc(i + 1))\*180/pi\]\];

end;

***
_Created with the Standard Edition of HelpNDoc: [Generate Kindle eBooks with ease](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
