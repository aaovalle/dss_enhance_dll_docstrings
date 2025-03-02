# ControlTrace

&nbsp;

(read/write)

&nbsp;

This property sets/gets {True \| False\*} to denote whether to trace the control actions to a file.

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

DSSSettings = DSSCircuit.Settings;

% Check if ControTrace is ON

if DSSSettings.ControlTrace,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('ControlTrace is ON');

end;

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Review with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
