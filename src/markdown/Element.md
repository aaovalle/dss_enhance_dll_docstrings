# Element

&nbsp;

(read/write)

&nbsp;

This property sets/gets the full object name of element being monitored (e.g. load.myLoad).

&nbsp;

Example

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSText.Command = 'solve mode=daily';

DSSMonitors = DSSCircuit.Monitors;

% select the first monitor on the list

DSSMonitors.First

% gets the name of the element monitored

myElement = DSSMonitors.Element;


***
_Created with the Standard Edition of HelpNDoc: [Free CHM Help documentation generator](<https://www.helpndoc.com>)_
