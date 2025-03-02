# DeadTime

&nbsp;

(read/write)

&nbsp;

This property get/set the Dead time after capacitor is turned OFF before it can be turned back ON for the active CapControl. Default is 300 sec.&nbsp;

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

DSSCapCtrls = DSSCircuit.CapControls;

% Sets the first CapControl as the active Obj

DSSCapCtrls.First;

% Returns the DeadTime for the active CapControl

myDeadTime = DSSCapCtrls.DeadTime;

***
_Created with the Standard Edition of HelpNDoc: [Easy to use tool to create HTML Help files and Help web sites](<https://www.helpndoc.com/help-authoring-tool>)_
