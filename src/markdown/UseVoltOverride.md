# UseVoltOverride

&nbsp;

(read/write)

&nbsp;

This property get/set the active CapControl for using Vmin and Vmax to override the control Mode.

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


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your CHM Help Files with HelpNDoc's Advanced Customization Options](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
