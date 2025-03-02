# First

&nbsp;

(read only)

&nbsp;

This property sets the first RegControl active. Returns 0 if none.

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

DSSRegCtrls = DSSCircuit.RegControls;

% Activates the first RegControl of the list

i = DSSRegCtrls.First;

***
_Created with the Standard Edition of HelpNDoc: [Single source CHM, PDF, DOC and HTML Help creation](<https://www.helpndoc.com/help-authoring-tool>)_
