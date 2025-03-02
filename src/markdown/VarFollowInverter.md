# VarFollowInverter

(read/write)

&nbsp;

Set/Get the Boolean variable (Yes = 1) or (No = 0). Defaults to False (0), which indicates that the reactive power generation/absorption does not respect the inverter status.

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

mySOC&nbsp; = DSSES.puSOC;

myVFIv = DSSES.VarFollowInverter

&nbsp;

DSSSolution.Solve;

***
_Created with the Standard Edition of HelpNDoc: [Simplify Your Help Documentation Process with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
