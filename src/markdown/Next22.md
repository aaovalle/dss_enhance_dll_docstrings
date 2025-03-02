# Next

(read only)

&nbsp;

This property sets the **Next** Storage element active. Returns 0 if none. Otherwise, returns the index of the active Storage device.

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

% Activates the first storage on the list (if any)

DSSES.First;

idx = DSSEs.Next;

if idx \> 0,

myRegValues = DSSES.RegisterValues;

end;


***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of a Help Authoring Tool](<https://www.helpndoc.com>)_
