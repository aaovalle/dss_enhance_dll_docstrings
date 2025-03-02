# Sensor

&nbsp;

(read only)

&nbsp;

Returns the name o the sensor monitoring the active load (if any).&nbsp;

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

DSSLoads = DSSCircuit.Loads;

% activates the first load on the list

i = DSSLoads.First;

% gets the name if the sensor monitoring this load

mySensor = DSSLoads.sensor;

if mySensor == '',

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('There is no sensor connected to this load');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;
***
_Created with the Standard Edition of HelpNDoc: [Transform Your CHM Help File Creation Process with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
