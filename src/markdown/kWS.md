# kWS

&nbsp;

(read/write)

&nbsp;

This property sets/gets an array of doubles for P measurements. Overwrites Currents with a new estimate using kVARS.

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

% gets the P measurements for the active sensor

mykWs = DSSSensors.kWS;

% reduces the measurements 80%

feature('COM\_SafeArraySingleDim',1);

DSSSensors.kWS = (mykWs.\*0.8)';

***
_Created with the Standard Edition of HelpNDoc: [Streamline your documentation process with HelpNDoc's HTML5 template](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
