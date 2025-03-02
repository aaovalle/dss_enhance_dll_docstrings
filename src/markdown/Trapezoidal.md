# Trapezoidal

&nbsp;

(read/write)

&nbsp;

This property sets/gets {True \| False \*} the value of trapezoidal integration flag in energy meters.

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

% Check if the EMs do trapezoidal integration

if DSSSettings.Trapezoidal,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('The trapezoidal integration is active for the Energy Meters');

end;

***
_Created with the Standard Edition of HelpNDoc: [Experience the power of a responsive website for your documentation](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
