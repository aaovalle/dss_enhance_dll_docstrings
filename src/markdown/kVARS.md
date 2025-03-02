# kVARS

&nbsp;

(read/write)

&nbsp;

This property sets/gets an array of doubles for Q measurements. Overwrites Currents with a new estimate using kWS.

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

% gets the array of Q measurements for the active sensor

myQs = DSSSensors.kVARS;

***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
