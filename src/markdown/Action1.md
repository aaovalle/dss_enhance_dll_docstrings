# Action

&nbsp;

(read/write)

&nbsp;

This property sets/gets the current state of the active switch. No effect if switch is locked.&nbsp; However, Reset removes any lock and then closes the switch (shelf state).

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

DSSSwtCtrl = DSSCircuit.SwtControls;

% activates the first SW of the list

DSSSwtCtrl.First;

% gets the action programmed for the active SW

mySWState = DSSSwtCtrl.Action;

***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
