# Voltages

&nbsp;

(read only)

&nbsp;

This property returns a complex array of voltages at terminals of the active element.

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

&nbsp; &nbsp; % Gets the voltages

&nbsp; &nbsp; myV = DSSActiveElement.Voltages;

&nbsp; &nbsp; % Formats the array as complex and polar arrays

&nbsp; &nbsp; mySize = size(myV);

&nbsp; &nbsp; myVCmplx = \[\]

&nbsp; &nbsp; myVPolar = \[\]

&nbsp; &nbsp; for a = 1:2:mySize(2),

&nbsp; &nbsp; &nbsp; &nbsp; CNum = myV(a) + i\*myV(a + 1);

&nbsp; &nbsp; &nbsp; &nbsp; myVCmplx = \[myVCmplx;CNum\];

&nbsp; &nbsp; &nbsp; &nbsp; myVPolar = \[myVPolar;\[abs(CNum),angle(CNum)\*180/pi\]\];

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;

***
_Created with the Standard Edition of HelpNDoc: [Converting Word Documents to eBooks: A Step-by-Step Guide with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
