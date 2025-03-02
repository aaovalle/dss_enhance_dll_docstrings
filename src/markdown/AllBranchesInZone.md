# AllBranchesInZone

&nbsp;

(read only)

&nbsp;

This property returns a wide string list of all branches (lines, transformer, etc.) in zone of the active EnergyMeter object.

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

% gets the list of PDE downstream the active EM

myZonePDE = DSSMeters.AllBranchesInZone;

***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
