# RegisterNames

(read only)

&nbsp;

This property returns a variant array of strings containing names of all storage device energy meter register names.

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

% gets the names of all energy meter register for storage

myRegNames = DSSES.RegisterNames;

***
_Created with the Standard Edition of HelpNDoc: [iPhone web sites made easy](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
