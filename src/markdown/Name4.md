# Name

&nbsp;

(read only)

&nbsp;

This property returns the full name name (class.name, e,g: Load.Load1) of the active element.

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

DSSLines = DSSCircuit.Capacitors;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Sets the first line of the list as the active element

if DSSLines.First \> 0,

&nbsp; &nbsp; % Gets the name of the active element

&nbsp; &nbsp; myName = DSSActiveElement.Name;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;

***
_Created with the Standard Edition of HelpNDoc: [Free EPub producer](<https://www.helpndoc.com/create-epub-ebooks>)_
