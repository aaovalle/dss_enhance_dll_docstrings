# CplxSeqVoltages

&nbsp;

(read only)

&nbsp;

This property returns a complex double array of Sequence Voltage for all terminals of active circuit element.

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

&nbsp; &nbsp; % Gets the complex sequence voltages

&nbsp; &nbsp; mySeqV = DSSActiveElement.CplxSeqVoltages;

&nbsp; &nbsp; % Formats the array as complex and polar arrays

&nbsp; &nbsp; mySize = size(mySeqV);

&nbsp; &nbsp; myVCmplx = \[\]

&nbsp; &nbsp; myVPolar = \[\]

&nbsp; &nbsp; for a = 1:2:mySize(2),

&nbsp; &nbsp; &nbsp; &nbsp; CNum = mySeqV(a) + i\*mySeqV(a + 1);

&nbsp; &nbsp; &nbsp; &nbsp; myVCmplx = \[myVCmplx;CNum\];

&nbsp; &nbsp; &nbsp; &nbsp; myVPolar = \[myVPolar;\[abs(CNum),angle(CNum)\*180/pi\]\];

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;

***
_Created with the Standard Edition of HelpNDoc: [Quickly and Easily Convert Your Word Document to an ePub or Kindle eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
