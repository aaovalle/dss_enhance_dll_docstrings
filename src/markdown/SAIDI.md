# SAIDI

&nbsp;

(read only)

&nbsp;

This property returns the SAIDI for the active meter's zone. Execute DoReliabilityCalc first.

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

% performs the reliability calculations for the model

% assuming automatic restoration

DSSMeters.DoreliabilityCalc(true);

% activates the first EM on the list

i = DSSMeters.First;

% gets the SAIDI for the active EnergyMeter's zone

mySAIDI = DSSMeters.SAIDI;

***
_Created with the Standard Edition of HelpNDoc: [Easy Qt Help documentation editor](<https://www.helpndoc.com>)_
