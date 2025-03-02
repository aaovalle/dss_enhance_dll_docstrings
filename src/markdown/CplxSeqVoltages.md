# CplxSeqVoltages

&nbsp;

(read only)

&nbsp;

This property returns a complex Double array of Sequence Voltages (0, 1, 2) at this Bus.

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

mySeqVolt = DSSActiveBus.CplxSeqVoltages;

mySize = size(mySeqVolt);

myVMagAng = \[\];

% Converts from complex to polar

for i = 1:2:(mySize(2) - 1),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVMagAng = \[myVMagAng;\[abs(mySeqVolt(i) + j\*mySeqVolt(i + 1)),angle(mySeqVolt(i) + j\*mySeqVolt(i + 1))\*180/pi\]\];

end;


***
_Created with the Standard Edition of HelpNDoc: [Make Documentation a Breeze with HelpNDoc's Clean and Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
