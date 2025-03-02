# First

&nbsp;

(read only)

&nbsp;

This property sets the first Sensor on the list active. Returns 0 if none.

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

% activates the first sensor on the list

i = DSSSensors.First;

***
_Created with the Standard Edition of HelpNDoc: [Free Qt Help documentation generator](<https://www.helpndoc.com>)_
