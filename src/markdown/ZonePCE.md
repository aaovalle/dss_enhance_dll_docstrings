# ZonePCE

&nbsp;

(read only)

&nbsp;

This property returns the list of all Power Conversion Elements (PCE - Loads, DER, etc.) within the area covered by the active EnergyMeter.

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

DSSMeters = DSSCircuit.Meters;

% activates the first EM on the list

i = DSSMeters.First;

% gets the PCE list within the area of the active EM

myPCEs = DSSMeters.ZonePCE;

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Help Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com>)_
