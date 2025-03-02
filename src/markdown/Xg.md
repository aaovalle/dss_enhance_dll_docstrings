# Xg

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Carson earth return reactance per unit length used to compute impedance values at base frequency.&nbsp; For making better frequency adjustments. Default is 0.155081 = 60 Hz value in ohms per kft (matches default line impedance). This value is required for harmonic solutions if you wish to adjust the earth return impedance for frequency. If not, set both Rg and Xg = 0.

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

DSSLines = DSSCircuit.Lines;

% activates the first line on the list

DSSLines.First;

% Gets Xg for the active line

myXg = DSSLines.Xg;

***
_Created with the Standard Edition of HelpNDoc: [Easily create Help documents](<https://www.helpndoc.com/feature-tour>)_
