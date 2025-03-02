# kVS

&nbsp;

(read/write)

&nbsp;

This property sets/gets an array of doubles for the LL or LN (depending on Delta connection) voltage measurements.

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

% gets the voltage measurements for the active sensor

mykVs = DSSSensors.kVS;

***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
