# cabs

&nbsp;

(read/write)

&nbsp;

This property returns abs value of complex number given in real and imag doubles.

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

% Calculates the magnitude for complex number 1 + 2i

myAbs = DSSCmathLib.cabs(1,2)


***
_Created with the Standard Edition of HelpNDoc: [Ensure High-Quality Documentation with HelpNDoc's Hyperlink and Library Item Reports](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
