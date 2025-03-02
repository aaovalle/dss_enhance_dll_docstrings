# kVA

(read/write)

&nbsp;

Get/set the inverter nameplate capability (in kVA). Used as the base for Dynamics mode and Harmonics mode values.&nbsp;

&nbsp;

Example

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

DSSES = DSSCircuit.Storages;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSSolution.Solve;

&nbsp;

% Activates the storage device by name

DSSES.Name = 'myStorage';

&nbsp;

% First, check the ES present state

myState = DSSES.State;

if myState = 0,

% if idling, setup the ES to discharge

DSS.State = 1,

end;

mySOC = DSSES.puSOC;

mykVA = DSSES.kVA

&nbsp;

DSSSolution.Solve;

***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
