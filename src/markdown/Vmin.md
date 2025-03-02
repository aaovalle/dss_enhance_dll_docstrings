# Vmin

&nbsp;

(read/write)

&nbsp;

This property get/set the max voltage level at the MonitoredObj for switching ON the capacitor. It requires to set UseVoltOVerride = true.

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

% Checks if the controller uses volt override, if not, enables it (just for this example)

if not(DSSCapCtrls.UseVoltOverride),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSCapCtrls.UseVoltOverride = true;

end;

% gets the min voltage set in volts

myVmin = DSSCapCtrls.Vmin\*DSSCapCtrls.PTRatio;


***
_Created with the Standard Edition of HelpNDoc: [Simplify Your Help Documentation Process with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
