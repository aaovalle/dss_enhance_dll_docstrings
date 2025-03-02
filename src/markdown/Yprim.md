# Yprim

&nbsp;

(read only)

&nbsp;

This property returns the YPrim matrix, column order, complex numbers (paired).

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

&nbsp; &nbsp; % Gets the Y prim matrix (vector)

&nbsp; &nbsp; myYPrim = DSSActiveElement.YPrim;

&nbsp; &nbsp; % Formats the vector as a complex matrix (dense)

&nbsp; &nbsp; mySize = size(myYPrim);

&nbsp; &nbsp; myYPMat = \[\]

&nbsp; &nbsp; for a = 1:2:mySize(2),

&nbsp; &nbsp; &nbsp; &nbsp; CNum = myYPrim(a) + i\* myYPrim(a + 1);

&nbsp; &nbsp; &nbsp; &nbsp; myYPMat = \[myYPMat;CNum\];

&nbsp; &nbsp; end;

&nbsp; &nbsp; myMatSize = mySize(2)/2/(DSSActiveElement.NumPhases \* DSSActiveElement.NumTerminals);

&nbsp; &nbsp; myYPMat = reshape(myYPMat,myMatSize,myMatSize);

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;


***
_Created with the Standard Edition of HelpNDoc: [Free help authoring environment](<https://www.helpndoc.com/help-authoring-tool>)_
