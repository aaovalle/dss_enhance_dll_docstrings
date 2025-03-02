# Count

(read only)

&nbsp;

This property resturns . Returns 0 if none.

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

% gets the number of ES in the model

myNumES = DSSES.Count

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Help Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com>)_
