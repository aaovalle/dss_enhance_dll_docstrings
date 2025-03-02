# AmpLimitGain

(read/write)

&nbsp;

Set/Get the fine tuning the current limiter when active for the active storage device, by default is 0.8,&nbsp;

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

IsALim = DSSES.AmpLimit

IsAG&nbsp; &nbsp; &nbsp; = DSSES.AmpLimitGain

&nbsp;

DSSSolution.Solve;

***
_Created with the Standard Edition of HelpNDoc: [Transform your help documentation into a stunning website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
