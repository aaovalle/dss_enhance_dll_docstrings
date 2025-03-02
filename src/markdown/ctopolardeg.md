# ctopolardeg

&nbsp;

(read/write)

&nbsp;

This property converts complex number to magnitude and angle, degrees. Returns variant array of two doubles.

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

% Converts complex 1 + 2i into polar

myResult = DSSCmathLib.ctopolardeg(1,2);

disp(\['magnitude= ',num2str(myResult(1)),' Angle= ',num2str(myResult(1))\]);


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Publish Your Word Document as an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
