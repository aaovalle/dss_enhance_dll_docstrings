# GUID

&nbsp;

(read only)

&nbsp;

This property returns the globally unique identifier for the active object.

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

&nbsp; &nbsp; % Gets the GUID for the active element

&nbsp; &nbsp; myGUID = DSSActiveElement.GUID;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;

***
_Created with the Standard Edition of HelpNDoc: [Free EBook and documentation generator](<https://www.helpndoc.com>)_
