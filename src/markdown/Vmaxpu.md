# Vmaxpu

&nbsp;

(read/write)

&nbsp;

This property sets/gets the maximum per unit voltage for which the Model is assumed to apply. Above this value, the load model reverts to a constant impedance model. Default = 1.10.

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

% gets the maximum pu voltage for the active Generator

myVmax = DSSGen.Vmaxpu;

***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation Process with HelpNDoc's Advanced Features](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
