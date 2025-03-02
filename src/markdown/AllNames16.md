# AllNames

&nbsp;

(read only)

&nbsp;

This property returns a variant array of strings with names of all sensors in the active circuit.

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

% gets the names of all sensors in the model

mySensors = DSSSensors.AllNames;

***
_Created with the Standard Edition of HelpNDoc: [Free CHM Help documentation generator](<https://www.helpndoc.com>)_
