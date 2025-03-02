# UpdateStorage

&nbsp;

(method)

&nbsp;

This method forces update to all storage classes. Typically done after a solution. Done automatically in intrinsic solution modes.

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

% Solves the circuit in snap mode (meters and monitors don't sample automatically)

DSSText.Command = 'Solve mode=snap';

% Forces update to all storage classes

DSSCircuit.UpdateStorage();

***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
