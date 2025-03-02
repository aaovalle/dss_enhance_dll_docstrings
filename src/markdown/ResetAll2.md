# ResetAll

&nbsp;

(method)

&nbsp;

This method clears all Sensors in the Active Circuit.

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

DSSSensors = DSSCircuit.Sensors;

% Clear all sensors

DSSSensors.ResetAll();

***
_Created with the Standard Edition of HelpNDoc: [Easy to use tool to create HTML Help files and Help web sites](<https://www.helpndoc.com/help-authoring-tool>)_
