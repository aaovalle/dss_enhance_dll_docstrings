# MonitoredTerm

&nbsp;

(read/write)

&nbsp;

This property get/set the terminal number on the element that PT and CT are connected to. Applies for the active CapControl.

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

DSSCapCtrls = DSSCircuit.CapControls;;

% Sets the first CapControl as the active Obj

DSSCapCtrls.First;

% Gets the terminal number of the object monitored by the CapControl to perform control actions

myMonitoredTerm = DSSCapCtrls.MonitoredTerm;

***
_Created with the Standard Edition of HelpNDoc: [Easily create PDF Help documents](<https://www.helpndoc.com/feature-tour>)_
