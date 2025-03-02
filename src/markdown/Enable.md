# Enable

&nbsp;

(method)

&nbsp;

This method Enables a circuit element by name (removes from circuit but leave in database).

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

% Disables load 'myLoad'

DSSCircuit.Disable('Load.myLoad');

DSSText.Command = 'Solve'

% Enables load 'myLoad'

DSSCircuit.Enable('Load.myLoad');

***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of a Help Authoring Tool](<https://www.helpndoc.com>)_
