# IsOpen

&nbsp;

(read only)

&nbsp;

This method returns a boolean indicating if the specified terminal and, optionally, phase is open.

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

&nbsp; &nbsp; % Check if the active element is open or closed at terminal 1, phase 1

&nbsp; &nbsp; if DSSActiveElement.IsOpen(1,1),

&nbsp; &nbsp; &nbsp; &nbsp; disp('Open\!');

&nbsp; &nbsp; else

&nbsp; &nbsp; &nbsp; &nbsp; disp('Closed');

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;

***
_Created with the Standard Edition of HelpNDoc: [Make Help Documentation a Breeze with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
