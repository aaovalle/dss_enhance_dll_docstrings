# cdiv

&nbsp;

(read/write)

&nbsp;

This property divides two complex number: (a1, b1)/(a2, b2). Returns variant array of two doubles representing complex result.

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

% Divides 1 + 2i / 2 + 3i

myResult = DSSCmathLib.cdiv(1,2,2,3);

% Converts the array into a complex number

myCmplx = myResult(1) + i\*myResult(2);

***
_Created with the Standard Edition of HelpNDoc: [Easily convert your WinHelp HLP help files to CHM with HelpNDoc's step-by-step guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
