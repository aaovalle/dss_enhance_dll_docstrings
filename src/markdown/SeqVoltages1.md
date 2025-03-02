# SeqVoltages

&nbsp;

(read only)

&nbsp;

This property returns a double array of symmetrical component voltages at each 3-phase terminal of the active element.

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

DSSLines = DSSCircuit.Lines;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Sets the first line of the list as the active element

if DSSLines.First \> 0,

&nbsp; &nbsp; % Gets the sequence voltages

&nbsp; &nbsp; mySeqV = DSSActiveElement.SeqVoltages;

&nbsp; &nbsp; mySize = size(mySeqV);

&nbsp; &nbsp; % organizes the array in complex pairs

&nbsp; &nbsp; mySeqVMat = \[\]

&nbsp; &nbsp; for a = 1:2:mySize(2),

&nbsp; &nbsp; &nbsp; &nbsp; mySeqVMat = \[mySeqVMat;\[mySeqV(a), mySeqV(a + 1)\]\];

&nbsp; &nbsp; end; &nbsp;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;


***
_Created with the Standard Edition of HelpNDoc: [Keep Your PDFs Safe from Unauthorized Access with These Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
