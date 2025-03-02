# Vminpu

&nbsp;

(read/write)

&nbsp;

This property sets/gets the minimum per unit voltage for which the Model is assumed to apply. Below this value, the load model reverts to a constant impedance model. For model 7, the current is limited to the value computed for constant power at Vminpu. Default = 0.90.

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

DSSGen = DSSCircuit.Generators;

% Selects the first Generator from the list

DSSGen.First;

% gets the minimum pu voltage for the active Generator

myVmax = DSSGen.Vminpu;

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your CHM Help File Output with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
