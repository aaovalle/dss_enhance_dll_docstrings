# Command

&nbsp;

(read/write)

&nbsp;

This property sets/gets the command string to be executed by OpenDSS.

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

DSSSwtCtrl = DSSCircuit.SwtControls;

% gets the names of all SwtControls in the model

mySW = DSSSwtCtrl.AllNames;

% get the time

DSSText.Command = 'get time';

myTimeStr = DSSText.Result;

***
_Created with the Standard Edition of HelpNDoc: [Full-featured multi-format Help generator](<https://www.helpndoc.com/help-authoring-tool>)_
