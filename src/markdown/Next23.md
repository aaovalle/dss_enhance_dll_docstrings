# Next

(read only)

&nbsp;

This property sets the **Next** Storage element active; returns 0 if none.

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

DSSWG = DSSCircuit.WingGens;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSSolution.Solve;

&nbsp;

% gets the names of all wind generators in the model

myWGs = DSSWG.AllNames;

% Activates the first WG on the list

idx = DSSWG.First;

&nbsp;

% Activates the next WG on the list (if any)

idx = DSSWG.Next;

&nbsp;

if idx \> 0,

% Checks if there WG in the model

myRegValues = DSSWG.RegisterValues;

end;

***
_Created with the Standard Edition of HelpNDoc: [Free help authoring tool](<https://www.helpndoc.com/help-authoring-tool>)_
