# Mode

&nbsp;

(read/write)

&nbsp;

This property get/set the control mode in which the active CapControl is operating. If defined as string, it can be one of the following:

&nbsp;

\- dssCapControlCurrent

\- dssCapControlVoltage

\- dssCapControlKvar

\- dssCapControlTime

\- dssCapControlPF

&nbsp;

Otherwise it can be a number between 0 and 4 following the same order presented above.

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

% Sets the CapControl to operate in current mode

DSSCapCtrls.Mode = 'dssCapControlCurrent';

***
_Created with the Standard Edition of HelpNDoc: [Create HTML Help, DOC, PDF and print manuals from 1 single source](<https://www.helpndoc.com/help-authoring-tool>)_
