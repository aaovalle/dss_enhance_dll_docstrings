# CurrentsMagAng

&nbsp;

(read only)

&nbsp;

This property returns the currents in magnitude, angle format as a variant array of doubles.

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

&nbsp; &nbsp; % Gets the currents

&nbsp; &nbsp; myCurr = DSSActiveElement.CurrentsMagAng;

&nbsp; &nbsp; % Formats the array as matrix (col 1 mag, col 2 angle)

&nbsp; &nbsp; mySize = size(myCurr);

&nbsp; &nbsp; myCurrMat = \[\]

&nbsp; &nbsp; for a = 1:2:mySize(2),

&nbsp; &nbsp; &nbsp; &nbsp; CNum = \[myCurr(a), myCurr(a + 1)\];

&nbsp; &nbsp; &nbsp; &nbsp; myCurrMat = \[myCurrMat;CNum\];

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;

***
_Created with the Standard Edition of HelpNDoc: [Easily Add Encryption and Password Protection to Your PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
