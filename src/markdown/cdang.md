# cdang

&nbsp;

(read/write)

&nbsp;

This property returns the angle, in degrees, of a complex number specified as two doubles: Realpart and imagpart.

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

% Loads the complex math lib

DSSCmathLib = DSSObject.CmathLib;

% Calculates the phase angle for complex number 1 + 2i

myAng = DSSCmathLib.cdang(1,2)

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your CHM Help File Capabilities with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
