# VLL

&nbsp;

(read only)

&nbsp;

This property returns for 2- and 3-phase buses, a variant array of complex numbers representing L-L voltages in volts. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3.

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

myVolt = DSSActiveBus.VLL;

mySize = size(myVolt);

myVMagAng = \[\];

% Converts from complex to polar

for i = 1:2:(mySize(2) - 1),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVMagAng = \[myVMagAng;\[abs(myVolt(i) + j\*myVolt(i + 1)),angle(myVolt(i) + j\*myVolt(i + 1))\*180/pi\]\];

end;

***
_Created with the Standard Edition of HelpNDoc: [Keep Your Sensitive PDFs Safe with These Easy Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
