# RegisterValues

(read only)

&nbsp;

This property returns a variant array of double values with the active Storage Element registers.

&nbsp;

Example

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

DSSES = DSSCircuit.Storages;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSSolution.Solve;

&nbsp;

% gets the values within the energy meter register for the active storage

DSSES.First;

myRegValues = DSSES.RegisterValues;

***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation with HelpNDoc's Project Analyzer Features](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
